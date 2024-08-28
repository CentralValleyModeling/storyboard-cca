import dash
import storyboard
from flask import send_from_directory

app = dash.Dash(
    __name__,
    external_stylesheets=storyboard.STYLE_SHEETS,
    assets_folder="assets",
    pages_folder="pages",
    use_pages=True,
)

app.layout = storyboard.body.Layout()
server = app.server


@server.route("/robots.txt")
def send_robots():
    """Don't list the website"""
    return send_from_directory("assets", "robots.txt")
