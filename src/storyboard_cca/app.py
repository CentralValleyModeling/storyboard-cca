import dash
import storyboard

app = dash.Dash(
    __name__,
    external_stylesheets=storyboard.STYLE_SHEETS,
    assets_folder="assets",
    pages_folder="pages",
    use_pages=True,
)

app.layout = storyboard.Layout()
server = app.server
