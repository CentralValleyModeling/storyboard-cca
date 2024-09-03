import dash
import dash_bootstrap_components as dbc
import storyboard as sb

dash.register_page(
    __name__,
    path="/adaptation",
    title="Adaptations - Climate Change Adaptation Studies",
    redirect_from=["/adaptations"],
)

app = dash.get_app()

PROJECTS = {
    "Delta Conveyance Project": (
        "2043 50% LOC - Maintain",
        "2043 50% LOC - DCP + Maintain",
    ),
    "Additional South Of Delta Storage": (
        "2043 50% LOC - Maintain",
        "2043 50% LOC - SODS + Maintain",
    ),
    "Forecast Informed Reservoir Operations": (
        "2043 50% LOC - Maintain",
        "2043 50% LOC - FIRO + Maintain",
    ),
}


def url_to_pretty(s: str) -> str:
    return s.replace("-", " ").title()


def pretty_to_url(s: str) -> str:
    return s.replace(" ", "-").lower()


def introduction():
    # 2. INTRODUCTION
    introduction = sb.PaddedSection(
        dbc.Row(
            sb.text.from_file("text/adaptation/introduction"),
        ),
    )
    return introduction


def structural():
    # 2. STRUCTURAL MEASURES
    dcp = dbc.Card(
        [
            dbc.CardImg(
                src=sb.placeholders.get_image_src(),
                top=True,
                style={
                    "height": "10vh",
                    "object-fit": "cover",
                },
            ),
            dbc.CardBody(
                [
                    sb.text.from_file("text/adaptation/dcp_1"),
                    sb.Jump(
                        "Explore",
                        "/adaptation?project=delta-conveyance-project#section-explore",
                        same_page=False,
                    ),
                ]
            ),
        ],
    )
    casp = dbc.Card(
        [
            dbc.CardImg(
                src=sb.placeholders.get_image_src(),
                top=True,
                style={
                    "height": "10vh",
                    "object-fit": "cover",
                },
            ),
            dbc.CardBody(
                [
                    sb.text.from_file("text/adaptation/casp_1"),
                ]
            ),
        ],
    )
    sods = dbc.Card(
        [
            dbc.CardImg(
                src=sb.placeholders.get_image_src(),
                top=True,
                style={
                    "height": "10vh",
                    "object-fit": "cover",
                },
            ),
            dbc.CardBody(
                [
                    sb.text.from_file("text/adaptation/sods_1"),
                    sb.Jump(
                        "Explore",
                        "/adaptation?project=additional-south-of-delta-storage#section-explore",
                        same_page=False,
                    ),
                ]
            ),
        ],
    )

    adaptations = dbc.Row(
        [
            dbc.Col(
                sb.SelfJump(sb.placeholders.get_image()),
                width=1,
            ),
            dbc.Col(
                class_name="mt-2 mb-5 me-5",
                children=[
                    dbc.Row(sb.text.from_file("text/adaptation/structural_1")),
                    dbc.Row(
                        [
                            dbc.Col(casp),
                            dbc.Col(dcp),
                            dbc.Col(sods),
                        ],
                    ),
                ],
            ),
        ],
        id="section-structural",
        class_name="border-top border-bottom border-primary",
    )
    return adaptations


def operational():
    # 3. OPERATIONAL & MANAGEMENT MEASURES
    firo = dbc.Card(
        [
            dbc.CardImg(
                src=sb.placeholders.get_image_src(),
                top=True,
                style={
                    "height": "10vh",
                    "object-fit": "cover",
                },
            ),
            dbc.CardBody(
                [
                    sb.text.from_file("text/adaptation/firo_1"),
                    sb.Jump(
                        "Explore",
                        "/adaptation?project=forecast-informed-reservoir-operations#section-explore",
                        same_page=False,
                    ),
                ]
            ),
        ],
    )
    asset_management = dbc.Card(
        [
            dbc.CardImg(
                src=sb.placeholders.get_image_src(),
                top=True,
                style={
                    "height": "10vh",
                    "object-fit": "cover",
                },
            ),
            dbc.CardBody(
                [
                    sb.text.from_file("text/adaptation/asset_management_1"),
                ]
            ),
        ],
    )
    adaptations = dbc.Row(
        [
            dbc.Col(
                class_name="mt-2 mb-5 ms-5",
                children=[
                    dbc.Row(sb.text.from_file("text/adaptation/operational_1")),
                    dbc.Row(
                        [
                            dbc.Col(asset_management),
                            dbc.Col(firo),
                        ],
                    ),
                ],
            ),
            dbc.Col(
                sb.SelfJump(sb.placeholders.get_image()),
                width=1,
            ),
        ],
        id="section-operations",
        class_name="border-top border-primary",
    )
    return adaptations


def project_impacts(project: str = ""):
    if project:
        project = url_to_pretty(project)
    return dbc.Container(
        id="section-explore",
        children=[
            dash.html.H1("Explore Project Impacts"),
            dash.dcc.Dropdown(
                list(PROJECTS.keys()),
                project,
                placeholder="Select a Project",
                id="project-selection",
            ),
            dbc.Row(
                id="project-explorer",
            ),
        ],
        class_name="mt-3",
    )


def layout(project: str = "", **kwargs):
    """Create the layout of the climate-change page.

    Returns
    -------
    sb.typing.Child
        The html component that will be rendered, may have nested children.
    """
    # 1. Introduction
    # 2. Structural Measures
    # 3. Operations & Management Measures
    return sb.Page(
        children=[
            introduction(),
            dbc.Col(
                children=[
                    operational(),
                    structural(),
                    project_impacts(project),
                ],
            ),
        ],
    )


@app.callback(
    dash.Output("url", "search"),
    dash.Input("project-selection", "value"),
    dash.State("url", "pathname"),
    dash.State("url", "search"),
    prevent_initial_call=True,
)
def update_url(project: str, url: str, search: str) -> str:
    key = pretty_to_url(project)
    s = f"?project={key}"
    if key and (s != search):
        return s
    return dash.no_update


@app.callback(
    dash.Output("project-explorer", "children"),
    dash.Input("project-selection", "value"),
)
def update_explore(project: str) -> str:
    scenario_names = PROJECTS[project]
    data = {
        "storage": sb.DB.get_timeseries("/.*/S_OROVL/STORAGE/.*/.*/.*/"),
        "river_flow": sb.DB.get_timeseries("/.*/NDOI/FLOW/.*/.*/.*/"),
        "deliveries": sb.DB.get_timeseries("/.*/SWP_PERDELDV/SWP-DELIVERY/.*/.*/.*/"),
    }
    for k, v in data.items():
        data[k] = {s: ts for s, ts in v.items() if s in scenario_names}

    return [
        dbc.Col(
            [
                dash.html.H3(project, className="mt-1"),
                dash.dcc.Graph(
                    figure=sb.plots.monthly(
                        data["storage"],
                        y_label="Oroville Stroage",
                    )
                ),
                dash.dcc.Graph(
                    figure=sb.plots.monthly(
                        data["river_flow"],
                        y_label="Delta Outflow",
                        conversion="cfs_to_taf",
                    )
                ),
                dash.dcc.Graph(
                    figure=sb.plots.annual_exceedance(
                        data["deliveries"],
                        y_label="SWP Deliveries",
                    )
                ),
            ],
            width=9,
        ),
        dbc.Col(sb.text.from_file(f"text/adaptation/explore/{pretty_to_url(project)}")),
    ]
