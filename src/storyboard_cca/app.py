import dash
import storyboard
from flask import send_from_directory

app = dash.Dash(
    __name__,
    external_stylesheets=storyboard.EXTERNAL_STYLE_SHEETS,
    external_scripts=storyboard.EXTERNAL_SCRIPTS,
    assets_folder="assets",
    pages_folder="pages",
    use_pages=True,
)

app.layout = storyboard.body.AppLayout()
server = app.server


@server.route("/robots.txt")
def send_robots():
    """Don't list the website"""
    return send_from_directory("assets", "robots.txt")


@app.callback(
    dash.Output("navbar-collapse", "is_open"),
    dash.Input("navbar-toggler", "n_clicks"),
    dash.State("navbar-collapse", "is_open"),
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
