import dash
import dash_bootstrap_components as dbc
import storyboard

dash.register_page(
    __name__,
    path="/climate-change",
    title="Climate Change - Climate Change Adaptation Studies",
)

app = dash.get_app()


def layout():
    """Create the layout of the climate-change page.

    Returns
    -------
    storyboard.typing.Child
        The html component that will be rendered, may have nested children.
    """
    # 1. Header
    # 2. Introduction
    # 3. Impacts to Reservoir Storage
    # 3. Impacts to Deliveries
    # 4. Impacts to River Flows
    # 5. ...
    # 6. Final Note

    # 1. HEADER
    header = storyboard.features.BannerImage(
        title="Climate Change",
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
            storyboard.markdown.from_file("text/climate_change/introduction"),
        ),
    )

    # 3. IMPACTS TO RESERVOIR STORAGE
    storage = storyboard.DB.get_timeseries("/.*/S_OROVL/STORAGE/.*/.*/.*/")
    storage = {
        k: v for k, v in storage.items() if k in ("Baseline", "2043 50% LOC - Maintain")
    }
    impacts_to_storage = storyboard.features.ScrollBy(
        left=storyboard.placeholders.get_image(),
        right=dbc.Col(
            children=[
                storyboard.markdown.from_file("text/climate_change/impacts_storage_1"),
                dash.dcc.Graph(
                    id="graph-climate-change-storage",
                    figure=storyboard.plots.monthly(
                        storage,
                        y_label="Oroville Storage",
                    ),
                ),
            ],
            class_name="me-3 mt-2",
        ),
        height_limit="75vh",
        left_width=3,
        id="section-storage",
    )

    # 4. IMPACTS TO RIVER FLOWS
    exports = storyboard.DB.get_timeseries("/.*/D_OMR027_CAA000/DIVERSION/.*/.*/.*/")
    impacts_to_deliveries = storyboard.features.ScrollBy(
        right=storyboard.placeholders.get_image(),
        left=dbc.Col(
            children=[
                storyboard.markdown.from_file(
                    "text/climate_change/impacts_deliveries_1"
                ),
                dash.dcc.Graph(
                    "graph-climate-change-river-flows",
                    figure=storyboard.plots.exceedance(
                        exports, y_label="Delta Exports"
                    ),
                ),
            ],
            class_name="me-3 mt-2",
        ),
        height_limit="75vh",
        left_width=9,
        id="section-river-flows",
    )

    # 6. FINAL NOTE
    final_note = storyboard.PaddedSection(
        dbc.Col(
            storyboard.markdown.from_file("text/climate_change/final_note"),
        )
    )

    return storyboard.Page(
        header=header,
        children=[
            introduction,
            impacts_to_storage,
            impacts_to_deliveries,
            final_note,
        ],
    )


@app.callback(
    dash.Output("scroll-to-hash", "data"),
    dash.Input("url", "href"),
)
def update_hash(href: str):
    if href and "#" in href:
        print(href.split("#"))
        return href.split("#")[-1]
    return None
