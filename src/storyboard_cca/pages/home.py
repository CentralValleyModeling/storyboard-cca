import dash

from .. import widgets


def layout():
    return widgets.layout.LayoutCCA(
        children=[
            widgets.features.TitleImageOverlay(
                title="Climate Change Adaptation Studies",
                image=widgets.placeholders.PlaceholderImage(),
            ),
            widgets.markdown.from_file("home/introduction"),
        ]
    )


app = dash.Dash(
    __name__,
    title="Home - Climate Change Adaptation Studies",
    external_stylesheets=widgets.STYLE_SHEETS,
    requests_pathname_prefix="/home/",
    assets_folder=widgets.ASSETS_DIR,
)

app.layout = layout
