import logging

import csrs
import csrs.config
import dash
import widgets

logger = logging.getLogger(__name__)

csrs.config.configure_logging(logger)

app = dash.Dash(
    __name__,
    title="Home - Climate Change Adaptation Studies",
    assets_folder=widgets.ASSETS_DIR,
    external_stylesheets=widgets.STYLE_SHEETS,
    use_pages=True,
)

app.layout = dash.html.Div(
    [
        dash.page_container,
    ]
)
server = app.server
