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
    # 4. Interlude
    # 5. Adaptations
    # 6. Final Note

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
    exports = storyboard.DB.get_timeseries("/.*/D_OMR027_CAA000/DIVERSION/.*/.*/.*/")

    climate_change = storyboard.features.ScrollBy(
        left=storyboard.features.BannerImage(
            title="Climate Change",
            image=storyboard.placeholders.get_image(),
            title_level=2,
            bar_color="bg-danger",
        ),
        right=dbc.Col(
            children=[
                storyboard.markdown.from_file("text/home/climate_change_1"),
                dash.dcc.Graph(
                    "graph-climate-change-1",
                    figure=storyboard.plots.monthly(exports, y_label="Delta Exports"),
                ),
                storyboard.markdown.from_file("text/home/climate_change_2"),
                storyboard.table.from_file("text/home/dcr_results"),
            ],
            class_name="me-3 mt-2",
        ),
        left_width=4,
    )

    # 4. INTERLUDE
    interlude = storyboard.PaddedSection(
        dbc.Col(
            storyboard.markdown.from_file("text/home/interlude"),
        )
    )

    # 5. ADAPTATIONS
    adaptations = storyboard.features.ScrollBy(
        right=storyboard.features.BannerImage(
            title="Adaptations",
            image=storyboard.placeholders.get_image(),
            title_level=2,
            bar_color="bg-success",
        ),
        left=storyboard.markdown.from_file("text/home/adaptations_1"),
        height_limit="50vh",
        left_width=7,
    )

    # 6. FINAL NOTE
    final_note = storyboard.PaddedSection(
        dbc.Col(
            storyboard.markdown.from_file("text/home/final_note"),
        )
    )

    return storyboard.Page(
        header=header,
        children=[
            introduction,
            climate_change,
            interlude,
            adaptations,
            final_note,
        ],
    )
