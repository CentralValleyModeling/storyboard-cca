import dash
import storyboard

app = dash.Dash(
    __name__,
    external_stylesheets=storyboard.STYLE_SHEETS,
    use_pages=True,
)

app.layout = storyboard.Layout()
server = app.server
