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


def introduction():
    # 2. INTRODUCTION
    introduction = dbc.Container(
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
                ],
            ),
        ],
    )
