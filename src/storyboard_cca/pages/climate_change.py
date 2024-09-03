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
    introduction = sb.PaddedSection(
        dbc.Row(
            sb.text.from_file("text/climate_change/introduction"),
        ),
    )
    return introduction


def reservoir_storage():
    # 3. IMPACTS TO RESERVOIR STORAGE
    data = sb.DB.get_timeseries("/.*/S_OROVL/STORAGE/.*/.*/.*/")
    data = {
        k: v for k, v in data.items() if k in ("Baseline", "2043 50% LOC - Maintain")
    }
    impacts = dbc.Row(
        [
            dbc.Col(
                sb.SelfJump(sb.placeholders.get_image()),
                width=1,
            ),
            dbc.Col(
                class_name="mt-2 mb-5 me-5",
                children=[
                    sb.text.from_file("text/climate_change/impacts_storage_1"),
                    dbc.Row(
                        [
                            dbc.Col(
                                dash.dcc.Graph(
                                    "graph-climate-change-storage-2043",
                                    figure=sb.plots.monthly(
                                        data,
                                        y_label="Oroville Storage (TAF)",
                                    ),
                                ),
                            ),
                            dbc.Col(
                                dash.dcc.Graph(
                                    "graph-climate-change-storage-2085",
                                    figure=sb.plots.monthly(
                                        data,
                                        y_label="Oroville Storage (TAF)",
                                    ),
                                ),
                            ),
                        ]
                    ),
                ],
            ),
        ],
        id="section-storage",
        class_name="border-top border-primary",
    )
    return impacts


def river_flows():
    # 4. IMPACTS TO RIVER FLOWS
    data = sb.DB.get_timeseries("/.*/NDOI/FLOW/.*/.*/.*/")
    data = {
        k: v for k, v in data.items() if k in ("Baseline", "2043 50% LOC - Maintain")
    }
    impacts = dbc.Row(
        [
            dbc.Col(
                class_name="mt-2 mb-5 ms-5",
                children=[
                    sb.text.from_file("text/climate_change/impacts_river_flows_1"),
                    dbc.Row(
                        [
                            dbc.Col(
                                dash.dcc.Graph(
                                    "graph-climate-change-river-flows-2043",
                                    figure=sb.plots.monthly(
                                        data,
                                        y_label="Delta Outflow (cfs)",
                                    ),
                                ),
                            ),
                            dbc.Col(
                                dash.dcc.Graph(
                                    "graph-climate-change-river-flows-2085",
                                    figure=sb.plots.monthly(
                                        data,
                                        y_label="Delta Outflow (cfs)",
                                    ),
                                ),
                            ),
                        ]
                    ),
                ],
            ),
            dbc.Col(sb.SelfJump(sb.placeholders.get_image()), width=1),
        ],
        id="section-river-flows",
        class_name="border-top border-primary",
    )
    return impacts


def deliveries():
    # 4. IMPACTS TO DELIVERIES
    data = sb.DB.get_timeseries("/.*/SWP_PERDELDV/SWP-DELIVERY/.*/.*/.*/")
    data = {
        k: v for k, v in data.items() if k in ("Baseline", "2043 50% LOC - Maintain")
    }
    impacts = dbc.Row(
        [
            dbc.Col(sb.SelfJump(sb.placeholders.get_image()), width=1),
            dbc.Col(
                class_name="mt-2 mb-5  me-5",
                children=[
                    sb.text.from_file("text/climate_change/impacts_deliveries_1"),
                    dbc.Row(
                        [
                            dbc.Col(
                                dash.dcc.Graph(
                                    "graph-climate-change-delivery-2043",
                                    figure=sb.plots.exceedance(
                                        data,
                                        y_label="SWP Delivery (%)",
                                    ),
                                ),
                            ),
                            dbc.Col(
                                dash.dcc.Graph(
                                    "graph-climate-change-delivery-2085",
                                    figure=sb.plots.exceedance(
                                        data,
                                        y_label="SWP Delivery (%)",
                                    ),
                                ),
                            ),
                        ]
                    ),
                ],
            ),
        ],
        id="section-deliveries",
        class_name="border-top border-primary",
    )
    return impacts


def salinity():
    # 4. IMPACTS TO SALINITY
    data = sb.DB.get_timeseries("/.*/EM_EC_MONTH/SALINITY/.*/.*/.*/")
    data = {
        k: v for k, v in data.items() if k in ("Baseline", "2043 50% LOC - Maintain")
    }
    impacts = dbc.Row(
        [
            dbc.Col(
                class_name="pt-2 mb-5 ms-5",
                children=[
                    sb.text.from_file("text/climate_change/impacts_salinity_1"),
                    dbc.Row(
                        [
                            dbc.Col(
                                dash.dcc.Graph(
                                    "graph-climate-salinity-2043",
                                    figure=sb.plots.exceedance(
                                        data,
                                        y_label="EC at Emmaton (UMHOS/CM)",
                                    ),
                                ),
                            ),
                            dbc.Col(
                                dash.dcc.Graph(
                                    "graph-climate-salinity-2085",
                                    figure=sb.plots.exceedance(
                                        data,
                                        y_label="EC at Emmaton (UMHOS/CM)",
                                    ),
                                ),
                            ),
                        ]
                    ),
                ],
            ),
            dbc.Col(sb.SelfJump(sb.placeholders.get_image()), width=1),
        ],
        id="section-salinity",
        class_name="border-top border-primary",
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
