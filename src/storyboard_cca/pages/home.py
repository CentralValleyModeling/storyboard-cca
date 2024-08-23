from pathlib import Path

import dash

from .. import widgets

here = Path(__file__).parent


def layout():
    return widgets.layout.LayoutCCA(
        children=[
            widgets.features.TitleImageOverlay(
                title="Climate Change Adaptation Studies",
                image=widgets.placeholders.PlaceholderImage(),
            )
        ]
    )


app = dash.Dash(
    __name__,
    title="Home - Climate Change Adaptation Studies",
    external_stylesheets=widgets.style_sheets,
    requests_pathname_prefix="/home/",
    assets_folder=here.parent / "assets",
)

app.layout = layout
