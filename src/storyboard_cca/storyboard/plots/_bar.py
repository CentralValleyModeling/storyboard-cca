from typing import Literal

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from csrs import schemas

from ..database import DB
from .colors import ASSIGNED_COLORS
from .conversions import cfs_to_taf


def get_wyt_assignments() -> pd.Series:
    wyt = DB.get_timeseries("/.*/WYT_SAC_/WATERYEARTYPE/.*/.*/.*/")
    df_wyt = wyt.popitem()[-1].to_frame()
    s_wyt: pd.Series = df_wyt.iloc[df_wyt.index.month == 5, 0]
    s_wyt.index = s_wyt.index.year
    s_wyt.name = "WYT"
    s_wyt = s_wyt.round(0).astype(int)
    return s_wyt


def wyt_bar(
    timeseries: dict[str, schemas.Timeseries],
    y_label: str = "y",
    x_label: str = "Water Year Type",
    group_label: str = "group",
    conversion: Literal["cfs_to_taf", "portion_to_percent"] | None = None,
    only_use_month: int | None = None,
    agg_method: Literal["mean", "sum"] = "mean",
    **layout_kwargs,
) -> go.Figure:
    frames = list()
    # Get WYT assignments
    wyt = get_wyt_assignments()
    for k, ts in timeseries.items():
        df = ts.to_frame()
        if conversion == "cfs_to_taf":
            df = cfs_to_taf(df)
        elif conversion == "portion_to_percent":
            df.iloc[:, 0] = df.iloc[:, 0] * 100
        if only_use_month:
            df = df.loc[df.index.month == only_use_month, :].copy()
        if agg_method == "sum":
            df: pd.DataFrame = df.groupby(df.index.year).agg("mean") * 12
        elif agg_method == "mean":
            df: pd.DataFrame = df.groupby(df.index.year).agg("mean")
        else:
            raise NotImplementedError(f"{agg_method=}")
        df.columns = [y_label]
        df: pd.DataFrame = df.join(wyt)
        df = df.groupby(df["WYT"]).mean().reset_index()
        df[group_label] = k
        frames.append(df)
    df_all = pd.concat(frames, axis=0)
    df_all[x_label] = df_all["WYT"].map(
        {
            5: "Critical",
            4: "Dry",
            3: "Below Normal",
            2: "Above Normal",
            1: "Wet",
        }
    )
    df_all = df_all.sort_values("WYT")
    return _bar(
        df_all,
        y_label=y_label,
        x_label=x_label,
        color=group_label,
        **layout_kwargs,
    )


def _bar(
    df: pd.DataFrame,
    y_label: str = "Value",
    x_label: str | None = None,
    color: str | None = None,
    **layout_kwargs,
) -> go.Figure:
    colors = {k: ASSIGNED_COLORS[k] for k in df[color].unique()}
    fig: go.Figure = px.bar(
        df,
        y=y_label,
        x=x_label,
        color=color,
        barmode="group",
        color_discrete_map=colors,
    )
    fig.update_xaxes(
        fixedrange=True,
    )
    fig.update_yaxes(
        visible=True,
        fixedrange=True,
        rangemode="tozero",
        title_text=y_label,
    )
    if x_label:
        fig.update_xaxes(
            visible=True,
            fixedrange=True,
            title_text=x_label,
        )
    # strip down the rest of the plot
    layout_kwargs = (
        dict(
            template="plotly_white",
            # plot_bgcolor="white",
            margin=dict(t=0, l=0, b=0, r=0),
            autosize=True,
            height=max(240, len(y_label) * 10 + 2),  # These are made up
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
            ),
        )
        | layout_kwargs
    )
    fig.update_layout(**layout_kwargs)

    return fig
