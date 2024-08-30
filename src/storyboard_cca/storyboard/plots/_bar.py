from typing import Literal

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from csrs import schemas

from ..database import DB
from .colors import ASSIGNED_COLORS
from .conversions import cfs_to_taf


def average_annual_bar(
    timeseries: dict[str, schemas.Timeseries],
    y_label: str = "y",
    x_label: str = "x",
    conversion: Literal["cfs_to_taf"] | None = None,
    **layout_kwargs,
) -> go.Figure:
    data = list()
    for k, ts in timeseries.items():
        df = ts.to_frame()
        if conversion == "cfs_to_taf":
            df = cfs_to_taf(df)
        df = df.resample(pd.offsets.YearEnd(n=1)).sum()
        data.append((k, float(df.mean().values[0])))
    df_mean = pd.DataFrame.from_records(data, columns=[x_label, y_label])
    return _bar(df_mean, y_label=y_label, x_label=x_label, **layout_kwargs)


def wyt_bar(
    timeseries: dict[str, schemas.Timeseries],
    y_label: str = "y",
    x_label: str = "x",
    conversion: Literal["cfs_to_taf"] | None = None,
    **layout_kwargs,
) -> go.Figure:
    frames = list()
    wyt = DB.get_timeseries("/.*/WYT_SAC_/WATERYEARTYPE/.*/.*/.*/")
    df_wyt = wyt[list(wyt.keys())[0]].to_frame()
    for k, ts in timeseries.items():
        df = ts.to_frame()
        if conversion == "cfs_to_taf":
            df = cfs_to_taf(df)
        df = df.groupby(df_wyt.iloc[:, 0].values).mean() * 12
        print(df)
        df[x_label] = k
        frames.append(df)
    df_all = pd.concat(frames, axis=1)
    print(df_all)
    return _bar(df_all, y_label=y_label, x_label=x_label, **layout_kwargs)


def _bar(
    df: pd.DataFrame,
    y_label: str = "Value",
    x_label: str | None = None,
    **layout_kwargs,
) -> go.Figure:
    colors = {k: ASSIGNED_COLORS[k] for k in df[x_label]}
    fig: go.Figure = px.bar(
        df,
        y=y_label,
        x=x_label,
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
