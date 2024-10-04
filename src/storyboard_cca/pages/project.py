import dash
import dash_bootstrap_components as dbc
import storyboard as sb

dash.register_page(
    __name__,
    path="/project",
    title="Projects - Climate Change Adaptation Studies",
)

app = dash.get_app()

PROJECTS = {
    "Delta Conveyance Project": tuple(
        a.name
        for a in sb.DB.get_scenarios_for_assumption(
            kind="dcp",
            assumption="Delta Conveyance Project",
        )
    ),
    "Additional South Of Delta Storage": tuple(
        a.name
        for a in sb.DB.get_scenarios_for_assumption(
            kind="sods",
            assumption="Additional South of Delta Storage",
        )
    ),
    "Forecast Informed Reservoir Operations": tuple(
        a.name
        for a in sb.DB.get_scenarios_for_assumption(
            kind="firo",
            assumption="Forecast-informed Reservoir Operations",
        )
    ),
}
print(PROJECTS)


def url_to_pretty(s: str) -> str:
    return s.replace("-", " ").title()


def pretty_to_url(s: str) -> str:
    return s.replace(" ", "-").lower()


def introduction():
    # 2. INTRODUCTION
    introduction = dbc.Container(
        dbc.Row(
            sb.text.from_file("text/project/introduction"),
        ),
    )
    return introduction


def sankey():
    # 3. IMPACTS TO RESERVOIR STORAGE
    data = {
        "oroville": sb.DB.get_timeseries("/.*/S_OROVL/STORAGE/.*/.*/.*/"),
        "san_luis": sb.DB.get_timeseries("/.*/S_SLUIS_SWP/STORAGE/.*/.*/.*/"),
    }
    for key, value in data.items():
        value = {
            k: v
            for k, v in value.items()
            if k in ("Baseline", "2043 50% LOC - Maintain")
        }
        data[key] = value


def all_plots(project: str):
    if project:
        project = url_to_pretty(project)
    return dbc.Container(
        id="section-explore",
        children=[
            dash.dcc.Dropdown(
                list(PROJECTS.keys()),
                project,
                placeholder="Select an Adaptation",
                id="adaptation-selection",
            ),
            dbc.Row(
                id="adaptation-explorer",
                class_name="mt-3",
            ),
        ],
        class_name="mt-3",
    )


def layout(name: str = "", **kwargs):
    """Create the layout of the climate-change page.

    Returns
    -------
    sb.typing.Child
        The html component that will be rendered, may have nested children.
    """
    # 1. Introduction

    return sb.Page(
        children=[
            introduction(),
            all_plots(name),
        ]
    )


@app.callback(
    dash.Output("url", "search"),
    dash.Input("adaptation-selection", "value"),
    dash.State("url", "search"),
)
def update_url(project: str, search: str) -> str:
    key = pretty_to_url(project)
    s = f"?name={key}"
    if key and (s != search):
        return s
    return dash.no_update


@app.callback(
    dash.Output("adaptation-explorer", "children"),
    dash.Input("adaptation-selection", "value"),
)
def update_explore(project: str) -> list:
    content = list()
    paths = [
        {
            "title": "Oroville Storage",
            "path": "/.*/S_OROVL/STORAGE/.*/.*/.*/",
            "y": "Oroville Storage (TAF)",
        },
        {
            "title": "San Luis Storage (SWP)",
            "path": "/.*/S_SLUIS_SWP/STORAGE/.*/.*/.*/",
            "y": "SWP San Luis Storage (TAF)",
        },
        {
            "title": "Delta Outflow",
            "path": "/.*/NDOI/FLOW/.*/.*/.*/",
            "y": "Delta Outflow (cfs)",
        },
        {
            "title": "SWP Delivery %",
            "path": "/.*/SWP_PERDELDV/SWP-DELIVERY/.*/.*/.*/",
            "y": "SWP Delivery (%)",
        },
        {
            "title": "Emmaton Salinity",
            "path": "/.*/EM_EC_MONTH/SALINITY/.*/.*/.*/",
            "y": "EC at Emmaton (UMHOS/CM)",
        },
    ]
    for kwargs in paths:
        data = sb.DB.get_timeseries(kwargs["path"])
        data = {k: v for k, v in data.items() if k in PROJECTS[project]}
        figs = [
            sb.plots.annual_exceedance(data, y_label=kwargs["y"]),
            sb.plots.monthly(data, y_label=kwargs["y"]),
        ]
        figs = [dash.dcc.Graph(figure=f) for f in figs]

        r = list()
        for fig in figs:
            r.append(
                dbc.Col(
                    [fig],
                    width=12,
                    lg=6,
                )
            )
        content.append(dash.html.H3(kwargs["title"]))
        content.append(dbc.Row(r))
    return content
