from typing import Literal

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def climate_scenario_scatter():
    data = pd.DataFrame(
        data=[
            {
                "Scenario": "2043 50% LOC",
                "Change in Average Temperature": 1.5,  # deg C
                "Change in Average Precipitation": 1.5,  # Percent
                "Change in Precipitation Intensity": 10.5,  # Percent
                "SLR": 0.5,  # ft
            },
            {
                "Scenario": "2043 95% LOC",
                "Change in Average Temperature": 1.8,  # deg C
                "Change in Average Precipitation": -1.8,  # Percent
                "Change in Precipitation Intensity": 12.6,  # Percent
                "SLR": 1.0,  # ft
            },
            {
                "Scenario": "2085 50% LOC",
                "Change in Average Temperature": 3.4,  # deg C
                "Change in Average Precipitation": 3.3,  # Percent
                "Change in Precipitation Intensity": 23.8,  # Percent
                "SLR": 1.8,  # ft
            },
            {
                "Scenario": "2085 75% LOC",
                "Change in Average Temperature": 3.9,  # deg C
                "Change in Average Precipitation": 0.4,  # Percent
                "Change in Precipitation Intensity": 27.3,  # Percent
                "SLR": 3.5,  # ft
            },
        ],
    )
    fig = None
    fig = go.Figure(
        [
            go.Scatter(
                # name="Climate Change Scenario Parameters",
                mode="markers",
                x=(data.loc[idx, "Change in Average Precipitation"],),
                y=(data.loc[idx, "Change in Average Temperature"],),
                marker_symbol="circle",
                hovertemplate="\u0394T: %{y}\u00B0C<br>\u0394P: %{x}%<br>",
                # text=["Scenario: {}".format(j) for j in data["Scenario"]],
                marker_line_width=1,
                marker_size=12,
                name=data.loc[idx, "Scenario"],
            )
            for idx in data.index
        ]
    )
    fig.update_layout(
        template="plotly_white",
        xaxis_title="Change in Precipitation (%)",
        yaxis_title="Change in Temperature (\u00B0C)",
        legend=dict(
            yanchor="top",
            y=-0.25,
            xanchor="center",
            x=0.5,
            orientation="h",
        ),
    )
    fig.update_xaxes(
        mirror=True,
        ticks="outside",
        fixedrange=True,
        range=(-5, 5),
    )
    fig.update_yaxes(
        mirror=True,
        ticks="outside",
        fixedrange=True,
        range=(0, 5),
    )
    return fig
