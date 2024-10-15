import logging
from functools import lru_cache
from typing import Literal

import dash
import dash_bootstrap_components as dbc
import storyboard as sb
from dash.dcc import Graph
from dash_bootstrap_components import Col, Row

logger = logging.getLogger(__name__)

dash.register_page(
    __name__,
    path="/climate-change",
    title="Climate Change - Climate Change Adaptation Studies",
)

app = dash.get_app()


def introduction():
    # 2. INTRODUCTION
    introduction = dbc.Container(
        Row(
            [
                Col(sb.text.from_file("text/climate_change/introduction")),
                Col(
                    id="g-intro",
                    children=Row(
                        dbc.Spinner(color="primary"),
                        justify="center",
                    ),
                    align="center",
                ),
            ]
        ),
    )

    return introduction


def reservoir_storage():
    # 3. IMPACTS TO RESERVOIR STORAGE
    impacts = sb.features.Parallax(
        [
            dbc.Container(
                sb.text.from_file("text/climate_change/impacts_storage_1"),
                className="bg-body p-4",
            ),
            dbc.Container(
                [
                    Row(
                        dash.html.H3("Oroville", className="mt-1"),
                        class_name="border-top border-secondary",
                    ),
                    Row(
                        [
                            Col(
                                id="g-cc-storage-oroville-2043",
                                children=Row(
                                    dbc.Spinner(color="primary"),
                                    justify="center",
                                ),
                                align="center",
                                sm=12,
                                lg=6,
                            ),
                            Col(
                                id="g-cc-storage-oroville-2085",
                                children=Row(
                                    dbc.Spinner(color="primary"),
                                    justify="center",
                                ),
                                align="center",
                                sm=12,
                                lg=6,
                            ),
                        ],
                        class_name="my-2",
                    ),
                    Row(
                        dash.html.H3("San Luis (SWP)", className="mt-1"),
                        class_name="border-top border-secondary",
                    ),
                    Row(
                        [
                            Col(
                                id="g-cc-storage-san-luis-2043",
                                children=Row(
                                    dbc.Spinner(color="primary"),
                                    justify="center",
                                ),
                                align="center",
                                sm=12,
                                lg=6,
                            ),
                            Col(
                                id="g-cc-storage-san-luis-2085",
                                children=Row(
                                    dbc.Spinner(color="primary"),
                                    justify="center",
                                ),
                                align="center",
                                sm=12,
                                lg=6,
                            ),
                        ],
                        class_name="my-2",
                    ),
                ],
                className="bg-body py-3",
            ),
        ],
        id="section-storage",
        background="images/climate_change/2022_08_02_JW_107_Oroville_Lake_Levels.jpg",
    )
    return impacts


def river_flows():
    # 4. IMPACTS TO RIVER FLOWS
    impacts = sb.features.Parallax(
        [
            dbc.Container(
                sb.text.from_file("text/climate_change/impacts_river_flows_1"),
                className="bg-body p-4",
            ),
            dbc.Container(
                Row(
                    [
                        Col(id="g-cc-river-flows-2043", sm=12, lg=6),
                        Col(id="g-cc-river-flows-2085", sm=12, lg=6),
                    ]
                ),
                className="bg-body p-4",
            ),
            dbc.Container(
                Row(
                    [
                        Col(
                            id="g-cc-river-flows-wyt-2043",
                            children=Row(
                                dbc.Spinner(color="primary"),
                                justify="center",
                            ),
                            align="center",
                            sm=12,
                            lg=6,
                        ),
                        Col(
                            id="g-cc-river-flows-wyt-2085",
                            children=Row(
                                dbc.Spinner(color="primary"),
                                justify="center",
                            ),
                            align="center",
                            sm=12,
                            lg=6,
                        ),
                    ]
                ),
                className="bg-body p-4",
            ),
        ],
        id="section-river-flows",
        background="images/climate_change/KG_Jan_storm_north_9403.jpg",
    )
    return impacts


def deliveries():
    # 4. IMPACTS TO DELIVERIES
    impacts = sb.features.Parallax(
        [
            dbc.Container(
                sb.text.from_file("text/climate_change/impacts_deliveries_1"),
                className="bg-body p-4",
            ),
            dbc.Container(
                Row(
                    [
                        Col(
                            id="g-cc-banks-wyt-2043",
                            children=Row(
                                dbc.Spinner(color="primary"),
                                justify="center",
                            ),
                            align="center",
                            sm=12,
                            lg=6,
                        ),
                        Col(
                            id="g-cc-banks-wyt-2085",
                            children=Row(
                                dbc.Spinner(color="primary"),
                                justify="center",
                            ),
                            align="center",
                            sm=12,
                            lg=6,
                        ),
                    ]
                ),
                className="bg-body p-4",
            ),
            dbc.Container(
                Row(
                    [
                        Col(
                            id="g-cc-perdel-wyt-2043",
                            children=Row(
                                dbc.Spinner(color="primary"),
                                justify="center",
                            ),
                            align="center",
                            sm=12,
                            lg=6,
                        ),
                        Col(
                            id="g-cc-perdel-wyt-2085",
                            children=Row(
                                dbc.Spinner(color="primary"),
                                justify="center",
                            ),
                            align="center",
                            sm=12,
                            lg=6,
                        ),
                    ]
                ),
                className="bg-body p-4",
            ),
            dbc.Container(
                Row(
                    [
                        Col(
                            id="g-cc-totaldel-wyt-2043",
                            children=Row(
                                dbc.Spinner(color="primary"),
                                justify="center",
                            ),
                            align="center",
                            sm=12,
                            lg=6,
                        ),
                        Col(
                            id="g-cc-totaldel-wyt-2085",
                            children=Row(
                                dbc.Spinner(color="primary"),
                                justify="center",
                            ),
                            align="center",
                            sm=12,
                            lg=6,
                        ),
                    ]
                ),
                className="bg-body p-4",
            ),
        ],
        id="section-deliveries",
        background="images/climate_change/2023_05_13_ZZ_0037_CVP_SWP_Aqueduct.jpg",
    )
    return impacts


def salinity():
    # 4. IMPACTS TO SALINITY
    impacts = sb.features.Parallax(
        [
            dbc.Container(
                sb.text.from_file("text/climate_change/impacts_salinity_1"),
                className="bg-body p-4",
            ),
            dbc.Container(
                Row(
                    [
                        Col(
                            id="g-cc-emmaton-2043",
                            children=Row(
                                dbc.Spinner(color="primary"),
                                justify="center",
                            ),
                            align="center",
                            sm=12,
                            lg=6,
                        ),
                        Col(
                            id="g-cc-emmaton-2085",
                            children=Row(
                                dbc.Spinner(color="primary"),
                                justify="center",
                            ),
                            align="center",
                            sm=12,
                            lg=6,
                        ),
                    ]
                ),
                className="bg-body p-4",
            ),
        ],
        id="section-salinity",
        background="images/climate_change/2023_05_11_ZZ_0098_Delta.jpg",
    )
    return impacts


def layout():
    """Create the layout of the climate-change page.

    Returns
    -------
    sb.typing.Child
        The html component that will be rendered, may have nested children.
    """
    # 1. Introduction
    # 2. Impacts to Reservoir Storage
    # 3. Impacts to River Flows
    # 4. Impacts to Deliveries
    # 5. Impacts to Salinity

    return sb.Page(
        children=[
            sb.obj_to_div(
                {
                    "paths": {
                        "path-oroville": "/.*/S_OROVL/STORAGE/.*/.*/.*/",
                        "path-san-luis": "/.*/S_SLUIS_SWP/STORAGE/.*/.*/.*/",
                        "path-ndoi": "/.*/NDOI/FLOW/.*/.*/.*/",
                        "path-perdel": "/.*/SWP_PERDELDV/SWP-DELIVERY/.*/.*/.*/",
                        "path-totaldel": "/.*/SWPTOTALDEL/FLOW-DELIVERY/.*/.*/.*/",
                        "path-banks": "/.*/C_CAA003_SWP/FLOW-DELIVERY/.*/.*/.*/",
                        "path-emmaton": "/.*/EM_EC_MONTH/SALINITY/.*/.*/.*/",
                    },
                    "y-labels": {
                        "y-label-oroville": "Oroville Storage (TAF)",
                        "y-label-san-luis": "San Luis Storage (TAF)",
                        "y-label-ndoi": "Net Delta Outflow Index (cfs)",
                        "y-label-banks": "Banks Exports (TAF)",
                        "y-label-perdel": "Average SWP Delivery (%)",
                        "y-label-totaldel": "Total Deliveries (TAF)",
                        "y-label-emmaton": "EC at Emmaton (UMHOS/CM)",
                    },
                    "group-labels": {
                        "g-label-ndoi": "Scenario",
                        "g-label-banks": "Scenario",
                        "g-label-perdel": "Scenario",
                        "g-label-totaldel": "Scenario",
                    },
                    "conversions": {
                        "conversion-banks": "cfs_to_taf",
                        "conversion-totaldel": "cfs_to_taf",
                        "conversion-perdel": None,
                    },
                    "agg-methods": {
                        "agg-banks": "sum",
                        "agg-perdel": "mean",
                        "agg-totaldel": "sum",
                    },
                    "scenarios-2043": [
                        "Maintenance without Adaptation (2023)",
                        "Maintenance without Adaptation (2043 50% LOC)",
                        "Maintenance without Adaptation (2043 95% LOC)",
                    ],
                    "scenarios-2085": [
                        "Maintenance without Adaptation (2023)",
                        "Maintenance without Adaptation (2085 50% LOC)",
                        "Maintenance without Adaptation (2085 75% LOC)",
                    ],
                },
            ),
            introduction(),
            Col(
                children=[
                    reservoir_storage(),
                    river_flows(),
                    deliveries(),
                    salinity(),
                ],
            ),
        ],
    )


@lru_cache
def endpoint_is(pathname: str, endpoint: str) -> bool:
    return pathname.endswith(endpoint)


@app.callback(
    dash.Output("scroll-to-hash", "data"),
    dash.Input("url", "href"),
)
def update_hash(href: str):
    if href and "#" in href:
        return href.split("#")[-1]
    return None


def plot_monthly_to_loading_div(
    url: str,
    path: str,
    scenarios: list[str],
    y_label: str = "Value",
    conversion: Literal["cfs_to_taf"] | None = None,
) -> Graph:
    if not endpoint_is(url, "climate-change"):
        return dash.no_update
    data = {
        s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path) for s in scenarios
    }
    figure = sb.plots.monthly(
        data,
        y_label=y_label,
        conversion=conversion,
    )
    return Graph(figure=figure)


def plot_wyt_bar_to_loading_div(
    url: str,
    path: str,
    scenarios: list[str],
    y_label: str = "y",
    group_label: str = "group",
    conversion: Literal["cfs_to_taf", "portion_to_percent"] | None = None,
    only_use_month: int | None = None,
    agg_method: Literal["mean", "sum"] = "mean",
) -> Graph:
    if not endpoint_is(url, "climate-change"):
        return dash.no_update
    data = {
        s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path) for s in scenarios
    }
    figure = sb.plots.wyt_bar(
        data,
        y_label=y_label,
        group_label=group_label,
        conversion=conversion,
        only_use_month=only_use_month,
        agg_method=agg_method,
    )
    return Graph(figure=figure)


# Establish callbacks for the graphs
@dash.callback(
    output=dash.Output("g-intro", "children"),
    inputs=[dash.Input("url", "href")],
)
def callback_graph_intro(_: str):
    return Graph(
        figure=sb.plots.pre_packed.climate_scenario_scatter(),
        config={"displayModeBar": False},
    )


dash.callback(
    output=dash.Output("g-cc-storage-oroville-2043", "children"),
    inputs=dict(
        url=dash.Input("url", "href"),
        path=dash.State("path-oroville", "children"),
        scenarios=dash.State("scenarios-2043", "children"),
        y_label=dash.State("y-label-oroville", "children"),
    ),
)(plot_monthly_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-storage-oroville-2085", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-oroville", "children"),
        scenarios=dash.State("scenarios-2085", "children"),
        y_label=dash.State("y-label-oroville", "children"),
    ),
)(plot_monthly_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-storage-san-luis-2043", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-san-luis", "children"),
        scenarios=dash.State("scenarios-2043", "children"),
        y_label=dash.State("y-label-san-luis", "children"),
    ),
)(plot_monthly_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-storage-san-luis-2085", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-san-luis", "children"),
        scenarios=dash.State("scenarios-2085", "children"),
        y_label=dash.State("y-label-san-luis", "children"),
    ),
)(plot_monthly_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-river-flows-2043", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-ndoi", "children"),
        scenarios=dash.State("scenarios-2043", "children"),
        y_label=dash.State("y-label-ndoi", "children"),
    ),
)(plot_monthly_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-river-flows-2085", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-ndoi", "children"),
        scenarios=dash.State("scenarios-2085", "children"),
        y_label=dash.State("y-label-ndoi", "children"),
    ),
)(plot_monthly_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-river-flows-wyt-2043", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-ndoi", "children"),
        scenarios=dash.State("scenarios-2043", "children"),
        group_label=dash.State("g-label-ndoi", "children"),
        y_label=dash.State("y-label-ndoi", "children"),
    ),
)(plot_wyt_bar_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-river-flows-wyt-2085", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-ndoi", "children"),
        scenarios=dash.State("scenarios-2085", "children"),
        group_label=dash.State("g-label-ndoi", "children"),
        y_label=dash.State("y-label-ndoi", "children"),
    ),
)(plot_wyt_bar_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-banks-wyt-2043", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-banks", "children"),
        scenarios=dash.State("scenarios-2043", "children"),
        group_label=dash.State("g-label-banks", "children"),
        y_label=dash.State("y-label-banks", "children"),
        agg_method=dash.State("agg-banks", "children"),
        conversion=dash.State("conversion-banks", "children"),
    ),
)(plot_wyt_bar_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-banks-wyt-2085", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-banks", "children"),
        scenarios=dash.State("scenarios-2085", "children"),
        group_label=dash.State("g-label-banks", "children"),
        y_label=dash.State("y-label-banks", "children"),
        agg_method=dash.State("agg-banks", "children"),
        conversion=dash.State("conversion-banks", "children"),
    ),
)(plot_wyt_bar_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-perdel-wyt-2043", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-perdel", "children"),
        scenarios=dash.State("scenarios-2043", "children"),
        group_label=dash.State("g-label-perdel", "children"),
        y_label=dash.State("y-label-perdel", "children"),
        agg_method=dash.State("agg-perdel", "children"),
        conversion=dash.State("conversion-perdel", "children"),
    ),
)(plot_wyt_bar_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-perdel-wyt-2085", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-perdel", "children"),
        scenarios=dash.State("scenarios-2085", "children"),
        group_label=dash.State("g-label-perdel", "children"),
        y_label=dash.State("y-label-perdel", "children"),
        agg_method=dash.State("agg-perdel", "children"),
        conversion=dash.State("conversion-perdel", "children"),
    ),
)(plot_wyt_bar_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-totaldel-wyt-2043", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-totaldel", "children"),
        scenarios=dash.State("scenarios-2043", "children"),
        group_label=dash.State("g-label-totaldel", "children"),
        y_label=dash.State("y-label-totaldel", "children"),
        agg_method=dash.State("agg-totaldel", "children"),
        conversion=dash.State("conversion-totaldel", "children"),
    ),
)(plot_wyt_bar_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-totaldel-wyt-2085", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-totaldel", "children"),
        scenarios=dash.State("scenarios-2085", "children"),
        group_label=dash.State("g-label-totaldel", "children"),
        y_label=dash.State("y-label-totaldel", "children"),
        agg_method=dash.State("agg-totaldel", "children"),
        conversion=dash.State("conversion-totaldel", "children"),
    ),
)(plot_wyt_bar_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-emmaton-2043", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-emmaton", "children"),
        scenarios=dash.State("scenarios-2043", "children"),
        y_label=dash.State("y-label-emmaton", "children"),
    ),
)(plot_monthly_to_loading_div)

dash.callback(
    output=dash.Output("g-cc-emmaton-2085", "children"),
    inputs=dict(
        url=dash.Input("url", "pathname"),
        path=dash.State("path-emmaton", "children"),
        scenarios=dash.State("scenarios-2085", "children"),
        y_label=dash.State("y-label-emmaton", "children"),
    ),
)(plot_monthly_to_loading_div)
