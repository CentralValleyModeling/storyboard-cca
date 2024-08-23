import logging

import numpy as np
import pandas as pd
from csrs import schemas
from plotly import graph_objects as go

logger = logging.getLogger(__name__)


def monthly(
    timeseries: dict[str, schemas.Timeseries],
    y_label: str = "Value",
    **layout_kwargs,
) -> str:
    logger.info(f"creating monthly chart for {len(timeseries)} timeseries")
    all_series = dict()
    month_key = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec",
    }
    for k, ts in timeseries.items():
        df = ts.to_frame()
        months: pd.Series = df.index.month
        df = df.groupby(months).agg("mean")
        df.index = [month_key[i] for i in df.index]
        all_series[k] = df.iloc[:, 0]
    return _line(
        series=all_series,
        y_label=y_label,
        **layout_kwargs,
    )


def exceedance(
    timeseries: dict[str, schemas.Timeseries],
    y_label: str = "y",
    **layout_kwargs,
) -> str:
    logger.info(f"creating exceedance chart for {len(timeseries)} timeseries")
    all_series = dict()
    for k, ts in timeseries.items():
        df = ts.to_frame()
        sorted = df.iloc[:, 0].sort_values().values
        exceedance = (np.arange(1.0, len(sorted) + 1.0) / len(sorted)) * 100.0
        series = pd.Series(sorted, index=exceedance)
        all_series[k] = series
    return _line(
        series=all_series,
        y_label=y_label,
        x_label="Non-Exceedance Probability (%)",
        **layout_kwargs,
    )


def _line(
    series: dict[str, pd.Series],
    y_label: str = "Value",
    x_label: str | None = None,
    **layout_kwargs,
) -> str:
    fig = go.Figure()
    for name, s in series.items():
        if isinstance(s, pd.DataFrame):
            s = s.iloc[:, 0]
        fig.add_trace(go.Scatter(x=s.index, y=s, mode="lines", name=name))
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
    logger.debug(f"{layout_kwargs=}")
    fig.update_layout(**layout_kwargs)
    config = {
        "responsive": True,
        "displaylogo": False,
    }

    return fig.to_html(
        include_plotlyjs=False,
        full_html=False,
        config=config,
    )
