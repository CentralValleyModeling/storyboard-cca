import dash
import dash_bootstrap_components as dbc
import storyboard as sb

dash.register_page(
    __name__,
    path="/",
    title="Home - Climate Change Adaptation Studies",
)


def layout():
    """Create the layout of the home page.

    Returns
    -------
    storyboard.typing.Child
        The html component that will be rendered, may have nested children.
    """
    # 2. Introduction
    # 3. Climate Change
    # 4. Interlude
    # 5. Adaptations

    # 2. INTRODUCTION
    introduction = dbc.Container(
        dbc.Row(
            [
                dbc.Col(
                    [
                        sb.text.from_file(
                            "text/home/introduction",
                            float_to="xl-end",
                        ),
                    ],
                    xs=dict(offset=False, order=0, size=12),
                    xl=dict(offset=False, order=0, size=6),
                ),
                dbc.Col(
                    sb.features.LinksBin.from_csv(
                        "text/home/links",
                        title="Learn More",
                        float_to="xl-start",
                    ),
                    xs=dict(offset=False, order=1, size=12),
                    xl=dict(offset=False, order=1, size=6),
                ),
            ],
            class_name="my-3",
        ),
        id="home-introduction",
    )

    # 3. CLIMATE CHANGE
    card_storage = sb.SimpleCard(
        header="Reservoir Storage",
        body=[
            sb.text.from_file("text/home/climate_change_storage"),
            sb.Jump("See the Impacts", "/climate-change#section-storage"),
        ],
    )
    card_river_flows = sb.SimpleCard(
        header="River Flows",
        body=[
            sb.text.from_file("text/home/climate_change_river_flows"),
            sb.Jump("See the Impacts", "/climate-change#section-river-flows"),
        ],
    )
    card_deliveries = sb.SimpleCard(
        header="SWP Deliveries",
        body=[
            sb.text.from_file("text/home/climate_change_deliveries"),
            sb.Jump("See the Impacts", "/climate-change#section-deliveries"),
        ],
    )
    card_salinity = sb.SimpleCard(
        header="Saliniaty",
        body=[
            sb.text.from_file("text/home/climate_change_salinity"),
            sb.Jump("See the Impacts", "/climate-change#section-salinity"),
        ],
    )
    climate_change = sb.features.Parallax(
        [
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(sb.text.from_file("text/home/climate_change_1")),
                            dbc.Col(sb.placeholders.get_image()),
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(sb.text.from_file("text/home/climate_change_2")),
                            dbc.Col(sb.text.from_file("text/home/climate_change_3")),
                        ],
                        class_name="grid gap-0 pt-3",
                    ),
                ],
                className="bg-body p-4",
            ),
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(card_storage),
                            dbc.Col(card_river_flows),
                            dbc.Col(card_salinity),
                            dbc.Col(card_deliveries),
                        ],
                        className="g-3 row-cols-1 row-cols-xl-2",
                    ),
                ],
                className="bg-body py-3",
                style={"--bs-bg-opacity": 0.5},
            ),
        ],
        id="home-climate-change",
        background="images/home/2024_09_05_SN_0121_Oroville_Lake_Levels_DRONE.jpg",
    )

    # 4. INTERLUDE
    interlude = dbc.Container(
        dbc.Row(
            [
                dbc.Col(sb.text.from_file("text/home/interlude")),
                dbc.Col(sb.placeholders.get_image()),
            ],
            class_name="py-5",
        ),
    )

    # 5. ADAPTATIONS
    card_structural = sb.SimpleCard(
        header="Structural Measures",
        body=[
            sb.text.from_file("text/home/adaptations_structural"),
            sb.Jump("See the Projects", "/adaptation#section-structural"),
        ],
    )
    card_operational = sb.SimpleCard(
        header="Operations & Management Measures",
        body=[
            sb.text.from_file("text/home/adaptations_operational"),
            sb.Jump("See the Projects", "/adaptation#section-operations"),
        ],
    )
    card_nature_based = sb.SimpleCard(
        header="Nature Based Measures",
        body=[
            sb.text.from_file("text/home/adaptations_nature"),
        ],
    )

    adaptation_cards = (
        dbc.Row(
            [
                dbc.Col(card_structural),
                dbc.Col(card_operational),
                dbc.Col(card_nature_based),
            ],
            class_name="grid gap-3 my-2",
        ),
    )
    adaptations = sb.features.Parallax(
        [
            dbc.Container(
                sb.text.from_file("text/home/adaptations_1"),
                className="bg-body p-3",
            ),
            dbc.Container(
                dbc.Row(*adaptation_cards),
                className="bg-body p-3",
                style={"--bs-bg-opacity": 0.5},
            ),
            dbc.Container(
                dbc.Row(
                    sb.text.from_file("text/home/projects_1"),
                    className="bg-body p-3",
                )
            ),
            dbc.Container(
                dash.html.Div(
                    sb.cards.from_file(
                        "text/home/projects",
                        kind="title_only",
                    ),
                    className="d-flex align-content-stretch flex-wrap",
                ),
                className="bg-body p-3",
                style={"--bs-bg-opacity": 0.5},
            ),
            dbc.Container(
                dbc.Row(
                    sb.text.from_file("text/home/projects_2"),
                    className="bg-body p-3",
                )
            ),
            dbc.Container(
                dash.html.Div(
                    sb.cards.from_file(
                        "text/home/projects_quantitative",
                        kind="title_only",
                    ),
                    className="d-flex align-content-stretch flex-wrap ",
                ),
                class_name="bg-body p-3",
                style={"--bs-bg-opacity": 0.5},
            ),
            dbc.Container(
                dash.html.Div(
                    sb.Jump(
                        "See how Climate Change Impacts the State Water Project",
                        "/climate-change",
                    ),
                    className="d-flex justify-content-center",
                ),
                class_name="bg-body p-3",
            ),
        ],
        background="images/home/PJH_Delta_Farming-3.jpg",
        id="home-adaptations",
    )

    return sb.Page(
        children=[
            introduction,
            climate_change,
            interlude,
            adaptations,
        ],
    )
