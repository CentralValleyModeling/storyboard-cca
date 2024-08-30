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
        dbc.Row(
            [
                dbc.Col(
                    storyboard.markdown.from_file("text/home/introduction_1"),
                    sm=dict(offset=False, order=0, size=12),
                    md=dict(offset=False, order=0, size=6),
                ),
                dbc.Col(
                    storyboard.features.LinksBin.from_csv(
                        "text/home/links",
                        title="Learn More",
                    ),
                    sm=dict(offset=False, order=1, size=12),
                    md=dict(offset=False, order=1, size=6),
                    class_name="mb-1",
                ),
            ]
        ),
        dbc.Row(storyboard.markdown.from_file("text/home/introduction_2")),
        id="home-introduction",
    )

    # 3. CLIMATE CHANGE
    exports = storyboard.DB.get_timeseries("/.*/SWP_TA_TOTAL/SWP_DELIVERY/.*/.*/.*/")
    exports = {
        k: v for k, v in exports.items() if k in ("Baseline", "2043 50% LOC - Maintain")
    }
    climate_change = storyboard.features.ScrollBy(
        left=storyboard.placeholders.get_image(),
        right=dbc.Col(
            children=[
                storyboard.markdown.from_file("text/home/climate_change_1"),
                dbc.Row(),
                storyboard.markdown.from_file("text/home/climate_change_2"),
                dash.dcc.Graph(
                    "graph-climate-change-1",
                    figure=storyboard.plots.annual_exceedance(
                        exports,
                        y_label="SWP Table A Deliveries (TAF)",
                        conversion="cfs_to_taf",
                    ),
                ),
                storyboard.markdown.from_file("text/home/climate_change_3"),
                storyboard.table.from_file("text/home/dcr_results"),
            ],
            class_name="me-3 mt-2",
        ),
        left_width=4,
        height_limit="75vh",
        id="home-climate-change",
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
        id="home-adaptations",
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
