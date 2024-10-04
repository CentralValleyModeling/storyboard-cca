import dash
import dash_bootstrap_components as dbc
import storyboard as sb

dash.register_page(
    __name__,
    path="/climate-change",
    title="Climate Change - Climate Change Adaptation Studies",
)

app = dash.get_app()


def introduction():
    # 2. INTRODUCTION
    fig = sb.plots.pre_packed.climate_scenario_scatter()
    introduction = dbc.Container(
        dbc.Row(
            [
                dbc.Col(sb.text.from_file("text/climate_change/introduction")),
                dbc.Col(dash.dcc.Graph(figure=fig)),
            ]
        ),
    )

    return introduction


def reservoir_storage():
    # 3. IMPACTS TO RESERVOIR STORAGE
    path_oro = "/.*/S_OROVL/STORAGE/.*/.*/.*/"
    path_sl = "/.*/S_SLUIS_SWP/STORAGE/.*/.*/.*/"

    scenarios_2043 = [
        "Maintenance without Adaptation (2023)",
        "Maintenance without Adaptation (2043 50% LOC)",
        "Maintenance without Adaptation (2043 95% LOC)",
    ]

    scenarios_2085 = [
        "Maintenance without Adaptation (2023)",
        "Maintenance without Adaptation (2085 50% LOC)",
        "Maintenance without Adaptation (2085 75% LOC)",
    ]

    data_2043 = {
        "oroville": {
            s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path_oro)
            for s in scenarios_2043
        },
        "san_luis": {
            s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path_sl)
            for s in scenarios_2043
        },
    }
    data_2085 = {
        "oroville": {
            s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path_oro)
            for s in scenarios_2085
        },
        "san_luis": {
            s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path_sl)
            for s in scenarios_2085
        },
    }

    impacts = sb.features.Parallax(
        [
            dbc.Container(
                sb.text.from_file("text/climate_change/impacts_storage_1"),
                className="bg-body p-4",
            ),
            dbc.Container(
                [
                    dbc.Row(
                        dash.html.H3("Oroville", className="mt-1"),
                        class_name="border-top border-secondary",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dash.dcc.Graph(
                                    "graph-climate-change-storage-oroville-2043",
                                    figure=sb.plots.monthly(
                                        data_2043["oroville"],
                                        y_label="Oroville Storage (TAF)",
                                    ),
                                ),
                                sm=12,
                                lg=6,
                            ),
                            dbc.Col(
                                dash.dcc.Graph(
                                    "graph-climate-change-storage-oroville-2085",
                                    figure=sb.plots.monthly(
                                        data_2085["oroville"],
                                        y_label="Oroville Storage (TAF)",
                                    ),
                                ),
                                sm=12,
                                lg=6,
                            ),
                        ],
                        class_name="my-2",
                    ),
                    dbc.Row(
                        dash.html.H3("San Luis (SWP)", className="mt-1"),
                        class_name="border-top border-secondary",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dash.dcc.Graph(
                                    "graph-climate-change-storage-san-luis-2043",
                                    figure=sb.plots.monthly(
                                        data_2043["san_luis"],
                                        y_label="San Luis (SWP) Storage (TAF)",
                                    ),
                                ),
                                sm=12,
                                lg=6,
                            ),
                            dbc.Col(
                                dash.dcc.Graph(
                                    "graph-climate-change-storage-san-luis-2085",
                                    figure=sb.plots.monthly(
                                        data_2085["san_luis"],
                                        y_label="San Luis (SWP) Storage (TAF)",
                                    ),
                                ),
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
    path_ndoi = "/.*/NDOI/FLOW/.*/.*/.*/"

    scenarios_2043 = [
        "Maintenance without Adaptation (2023)",
        "Maintenance without Adaptation (2043 50% LOC)",
        "Maintenance without Adaptation (2043 95% LOC)",
    ]

    scenarios_2085 = [
        "Maintenance without Adaptation (2023)",
        "Maintenance without Adaptation (2085 50% LOC)",
        "Maintenance without Adaptation (2085 75% LOC)",
    ]

    data_2043 = {
        "ndoi": {
            s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path_ndoi)
            for s in scenarios_2043
        },
    }
    data_2085 = {
        "ndoi": {
            s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path_ndoi)
            for s in scenarios_2085
        },
    }
    impacts = sb.features.Parallax(
        [
            dbc.Container(
                sb.text.from_file("text/climate_change/impacts_river_flows_1"),
                className="bg-body p-4",
            ),
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            dash.dcc.Graph(
                                "graph-climate-change-river-flows-2043",
                                figure=sb.plots.monthly(
                                    data_2043["ndoi"],
                                    y_label="Delta Outflow (cfs)",
                                ),
                            ),
                            sm=12,
                            lg=6,
                        ),
                        dbc.Col(
                            dash.dcc.Graph(
                                "graph-climate-change-river-flows-2085",
                                figure=sb.plots.monthly(
                                    data_2085["ndoi"],
                                    y_label="Delta Outflow (cfs)",
                                ),
                            ),
                            sm=12,
                            lg=6,
                        ),
                    ]
                ),
                className="bg-body p-4",
            ),
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            dash.dcc.Graph(
                                "graph-climate-change-delivery-2043",
                                figure=sb.plots.wyt_bar(
                                    data_2043["ndoi"],
                                    y_label="Delta Outflow (cfs)",
                                    group_label="Scenario",
                                ),
                            ),
                            sm=12,
                            lg=6,
                        ),
                        dbc.Col(
                            dash.dcc.Graph(
                                "graph-climate-change-delivery-2085",
                                figure=sb.plots.wyt_bar(
                                    data_2085["ndoi"],
                                    y_label="Delta Outflow (cfs)",
                                    group_label="Scenario",
                                ),
                            ),
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
    path_perdel = "/.*/SWP_PERDELDV/SWP-DELIVERY/.*/.*/.*/"
    path_totaldel = "/.*/SWPTOTALDEL/FLOW-DELIVERY/.*/.*/.*/"
    path_banks = "/.*/C_CAA003_SWP/FLOW-DELIVERY/.*/.*/.*/"

    scenarios_2043 = [
        "Maintenance without Adaptation (2023)",
        "Maintenance without Adaptation (2043 50% LOC)",
        "Maintenance without Adaptation (2043 95% LOC)",
    ]

    scenarios_2085 = [
        "Maintenance without Adaptation (2023)",
        "Maintenance without Adaptation (2085 50% LOC)",
        "Maintenance without Adaptation (2085 75% LOC)",
    ]

    data_2043 = {
        "perdel": {
            s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path_perdel)
            for s in scenarios_2043
        },
        "totaldel": {
            s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path_totaldel)
            for s in scenarios_2043
        },
        "banks": {
            s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path_banks)
            for s in scenarios_2043
        },
    }
    data_2085 = {
        "perdel": {
            s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path_perdel)
            for s in scenarios_2085
        },
        "totaldel": {
            s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path_totaldel)
            for s in scenarios_2085
        },
        "banks": {
            s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path_banks)
            for s in scenarios_2085
        },
    }

    impacts = sb.features.Parallax(
        [
            dbc.Container(
                sb.text.from_file("text/climate_change/impacts_deliveries_1"),
                className="bg-body p-4",
            ),
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            dash.dcc.Graph(
                                "graph-climate-change-delivery-2043",
                                figure=sb.plots.wyt_bar(
                                    data_2043["banks"],
                                    y_label="Banks Exports (TAF)",
                                    group_label="Scenario",
                                    conversion="cfs_to_taf",
                                    agg_method="sum",
                                ),
                            ),
                            sm=12,
                            lg=6,
                        ),
                        dbc.Col(
                            dash.dcc.Graph(
                                "graph-climate-change-delivery-2085",
                                figure=sb.plots.wyt_bar(
                                    data_2085["banks"],
                                    y_label="Banks Exports (TAF)",
                                    group_label="Scenario",
                                    conversion="cfs_to_taf",
                                    agg_method="sum",
                                ),
                            ),
                            sm=12,
                            lg=6,
                        ),
                    ]
                ),
                className="bg-body p-4",
            ),
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            dash.dcc.Graph(
                                "graph-climate-change-delivery-2043",
                                figure=sb.plots.wyt_bar(
                                    data_2043["perdel"],
                                    y_label="Average SWP Delivery (%)",
                                    group_label="Scenario",
                                ),
                            ),
                            sm=12,
                            lg=6,
                        ),
                        dbc.Col(
                            dash.dcc.Graph(
                                "graph-climate-change-delivery-2085",
                                figure=sb.plots.wyt_bar(
                                    data_2085["perdel"],
                                    y_label="Average SWP Delivery (%)",
                                    group_label="Scenario",
                                ),
                            ),
                            sm=12,
                            lg=6,
                        ),
                    ]
                ),
                className="bg-body p-4",
            ),
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            dash.dcc.Graph(
                                "graph-climate-change-delivery-2043",
                                figure=sb.plots.wyt_bar(
                                    data_2043["totaldel"],
                                    y_label="Total Deliveries (TAF)",
                                    group_label="Scenario",
                                    conversion="cfs_to_taf",
                                    agg_method="sum",
                                ),
                            ),
                            sm=12,
                            lg=6,
                        ),
                        dbc.Col(
                            dash.dcc.Graph(
                                "graph-climate-change-delivery-2085",
                                figure=sb.plots.wyt_bar(
                                    data_2085["totaldel"],
                                    y_label="Total Deliveries (TAF)",
                                    group_label="Scenario",
                                    conversion="cfs_to_taf",
                                    agg_method="sum",
                                ),
                            ),
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

    path_emmaton = "/.*/EM_EC_MONTH/SALINITY/.*/.*/.*/"

    scenarios_2043 = [
        "Maintenance without Adaptation (2023)",
        "Maintenance without Adaptation (2043 50% LOC)",
        "Maintenance without Adaptation (2043 95% LOC)",
    ]

    scenarios_2085 = [
        "Maintenance without Adaptation (2023)",
        "Maintenance without Adaptation (2085 50% LOC)",
        "Maintenance without Adaptation (2085 75% LOC)",
    ]

    data_2043 = {
        "emmaton": {
            s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path_emmaton)
            for s in scenarios_2043
        },
    }
    data_2085 = {
        "emmaton": {
            s: sb.DB.get_timeseries_for_scenario(scenario=s, path=path_emmaton)
            for s in scenarios_2085
        },
    }
    impacts = sb.features.Parallax(
        [
            dbc.Container(
                sb.text.from_file("text/climate_change/impacts_salinity_1"),
                className="bg-body p-4",
            ),
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            dash.dcc.Graph(
                                "graph-climate-salinity-2043",
                                figure=sb.plots.exceedance(
                                    data_2043["emmaton"],
                                    y_label="EC at Emmaton (UMHOS/CM)",
                                ),
                            ),
                            sm=12,
                            lg=6,
                        ),
                        dbc.Col(
                            dash.dcc.Graph(
                                "graph-climate-salinity-2085",
                                figure=sb.plots.exceedance(
                                    data_2085["emmaton"],
                                    y_label="EC at Emmaton (UMHOS/CM)",
                                ),
                            ),
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
            introduction(),
            dbc.Col(
                children=[
                    reservoir_storage(),
                    river_flows(),
                    deliveries(),
                    salinity(),
                ],
            ),
        ],
    )


@app.callback(
    dash.Output("scroll-to-hash", "data"),
    dash.Input("url", "href"),
)
def update_hash(href: str):
    if href and "#" in href:
        return href.split("#")[-1]
    return None
