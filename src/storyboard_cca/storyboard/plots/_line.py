import pandas as pd
from plotly import graph_objects as go

from .colors import ASSIGNED_COLORS


def line(
    series: dict[str, pd.Series],
    y_label: str = "Value",
    x_label: str | None = None,
    **layout_kwargs,
) -> go.Figure:
    fig = go.Figure()
    for name, s in series.items():
        if isinstance(s, pd.DataFrame):
            s = s.iloc[:, 0]
        fig.add_trace(
            go.Scatter(
                x=s.index,
                y=s,
                mode="lines",
                name=name,
                line=dict(color=ASSIGNED_COLORS[name]),
            )
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
