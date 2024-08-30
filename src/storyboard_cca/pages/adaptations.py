import dash
import dash_bootstrap_components as dbc
import storyboard

dash.register_page(
    __name__,
    path="/adaptation",
    title="Adaptations - Climate Change Adaptation Studies",
    redirect_from=["/adaptations"],
)


def layout():
    """Create the layout of the adaptations page.

    Returns
    -------
    storyboard.typing.Child
        The html component that will be rendered, may have nested children.
    """
    # 1. Header
    # 2. Introduction
    # 3. Impacts to Deliveries
    # 4. Impacts to River Flows
    # 5. ...
    # 6. Final Note

    # 1. HEADER
    header = storyboard.features.BannerImage(
        title="Adatpations",
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
            storyboard.text.from_file("text/adaptation/introduction"),
        ),
    )

    # 3. CLIMATE CHANGE
    exports = storyboard.DB.get_timeseries("/.*/D_OMR027_CAA000/DIVERSION/.*/.*/.*/")
    impacts_to_deliveries = storyboard.features.ScrollBy(
        left=storyboard.features.BannerImage(
            title="Delta Conveyance Project",
            image=storyboard.placeholders.get_image(),
            title_level=2,
            bar_color="bg-danger",
        ),
        right=dbc.Col(
            children=[
                storyboard.text.from_file("text/adaptation/dcp_1"),
                dash.dcc.Graph(
                    "graph-climate-change-1",
                    figure=storyboard.plots.exceedance(
                        exports, y_label="Delta Exports"
                    ),
                ),
            ],
            class_name="me-3 mt-2",
        ),
        left_width=6,
    )

    # 6. FINAL NOTE
    final_note = storyboard.PaddedSection(
        dbc.Col(
            storyboard.text.from_file("text/adaptation/final_note"),
        )
    )

    return storyboard.Page(
        header=header,
        children=[
            introduction,
            impacts_to_deliveries,
            final_note,
        ],
    )
