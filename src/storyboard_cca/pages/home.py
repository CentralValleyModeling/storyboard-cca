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
    # 1. Header
    # 2. Introduction
    # 3. Climate Change
    # 4. Interlude
    # 5. Adaptations
    # 6. Final Note

    # 1. HEADER
    header = sb.features.BannerImage(
        title="Climate Change Adaptation Studies",
        image=sb.placeholders.get_image(
            style={
                "height": "300px",
                "object-fit": "cover",
            }
        ),
    )

    # 2. INTRODUCTION
    introduction = sb.PaddedSection(
        dbc.Row(
            [
                dbc.Col(
                    sb.text.from_file("text/home/introduction_1"),
                    xs=dict(offset=False, order=0, size=12),
                    md=dict(offset=False, order=0, size=6),
                ),
                dbc.Col(
                    sb.features.LinksBin.from_csv(
                        "text/home/links",
                        title="Learn More",
                    ),
                    xs=dict(offset=False, order=1, size=12),
                    md=dict(offset=False, order=1, size=6),
                    class_name="mb-1",
                ),
            ]
        ),
        dbc.Row(
            sb.text.from_file("text/home/introduction_2"),
        ),
        id="home-introduction",
    )

    # 3. CLIMATE CHANGE
    card_storage = sb.SimpleCard(
        header="Reservoir Storage",
        body=[
            sb.text.from_file("text/home/climate_change_storage"),
            sb.Jump("Explore", "/climate-change#section-storage"),
        ],
    )
    card_river_flows = sb.SimpleCard(
        header="River Flows",
        body=[
            sb.text.from_file("text/home/climate_change_river_flows"),
            sb.Jump("Explore", "/climate-change#section-river-flows"),
        ],
    )
    card_deliveries = sb.SimpleCard(
        header="SWP Deliveries",
        body=[
            sb.text.from_file("text/home/climate_change_deliveries"),
            sb.Jump("Explore", "/climate-change#section-deliveries"),
        ],
    )
    card_saliniaty = sb.SimpleCard(
        header="Saliniaty",
        body=[
            sb.text.from_file("text/home/climate_change_salinity"),
            sb.Jump("Explore", "/climate-change#section-salinity"),
        ],
    )
    impacts_cards = (
        dbc.Row(
            [
                dbc.Col(card_storage, xl=6, lg=12),
                dbc.Col(card_river_flows, xl=6, lg=12),
                dbc.Col(card_deliveries, xl=6, lg=12),
                dbc.Col(card_saliniaty, xl=6, lg=12),
            ],
            class_name="g-2 my-2 row-cols-1 row-cols-md-2",
        ),
    )
    climate_change = sb.features.ScrollBy(
        left=sb.SelfJump(sb.placeholders.get_image()),
        right=dbc.Col(
            children=[
                sb.text.from_file("text/home/climate_change_1"),
                sb.text.from_file("text/home/climate_change_2"),
                sb.text.from_file("text/home/climate_change_3"),
                *impacts_cards,
            ],
            class_name="me-3 py-3",
        ),
        priority="right",
        margin_y=3,
        height_limit="75vh",
        id="home-climate-change",
    )

    # 4. INTERLUDE
    interlude = sb.PaddedSection(
        dbc.Row(
            sb.text.from_file("text/home/interlude"),
        ),
    )

    # 5. ADAPTATIONS
    card_structural = sb.SimpleCard(
        header="Structural Measures",
        body=[
            sb.text.from_file("text/home/adaptations_structural"),
            sb.Jump("Explore", "/adaptation#section-structural"),
        ],
    )
    card_operational = sb.SimpleCard(
        header="Operations & Management Measures",
        body=[
            sb.text.from_file("text/home/adaptations_operational"),
            sb.Jump("Explore", "/adaptation#section-operations"),
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
                dbc.Col(card_structural, xl=4, lg=12),
                dbc.Col(card_operational, xl=4, lg=12),
                dbc.Col(card_nature_based, xl=4, lg=12),
            ],
            class_name="g-2 my-2",
        ),
    )
    adaptations = sb.features.ScrollBy(
        right=sb.SelfJump(sb.placeholders.get_image()),
        left=dbc.Col(
            children=[
                sb.text.from_file("text/home/adaptations_1"),
                *adaptation_cards,
            ],
            class_name="ms-3 py-3",
        ),
        priority="left",
        margin_y=3,
        height_limit="75vh",
        id="home-adaptations",
    )

    # 6. FINAL NOTE
    final_note = sb.PaddedSection(
        dbc.Row(
            sb.text.from_file("text/home/projects_1"),
        ),
        dbc.Row(
            sb.table.from_file(
                "text/home/projects",
                kind="bootstrap",
                class_name="table-sm",
            ),
        ),
        dbc.Row(
            sb.text.from_file("text/home/projects_2"),
        ),
        dbc.Row(
            sb.table.from_file(
                "text/home/projects_quantitative",
                kind="bootstrap",
                class_name="table-sm",
            ),
        ),
    )

    return sb.Page(
        header=header,
        children=[
            introduction,
            climate_change,
            interlude,
            adaptations,
            final_note,
        ],
    )
