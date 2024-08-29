import dash
import dash_bootstrap_components as dbc
import storyboard

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
    # 4. Adaptations

    # 1. HEADER
    header = storyboard.features.BannerImage(
        title="Climate Change Adaptation Studies",
        image=storyboard.placeholders.get_image(
            style={
                "height": "300px",
                "object-fit": "cover",
            }
        ),
    )

    # 2. INTRODUCTION
    introduction = storyboard.PaddedSection(
        dbc.Col(
            storyboard.markdown.from_file("text/home/introduction"),
            width=8,
        ),
        dbc.Col(
            storyboard.features.LinksBin.from_csv(
                "text/home/links",
                title="Learn More",
            ),
            width=4,
        ),
    )

    # 3. CLIMATE CHANGE
    climate_change = storyboard.features.ScrollBy(
        left=storyboard.features.BannerImage(
            title="Climate Change",
            image=storyboard.placeholders.get_image(),
        ),
        right=dbc.Col(
            children=[
                storyboard.markdown.from_file("text/home/baseline_conditions"),
                dash.html.Div(
                    storyboard.table.from_file("text/home/dcr_results"),
                    className="mb-1",
                ),
                storyboard.placeholders.LoremIpsum(10),
            ],
            class_name="me-3 mt-2",
        ),
    )

    # 4. ADAPTATIONS
    adaptations = storyboard.features.ScrollBy(
        right=storyboard.placeholders.get_image(),
        left=storyboard.placeholders.LoremIpsum(20),
        height_limit="50vh",
    )

    return storyboard.Page(
        header=header,
        children=[
            introduction,
            climate_change,
            adaptations,
        ],
    )
