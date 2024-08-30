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

storyboard.plots.colors.assign_colors_for_runs(
    [s.name for s in storyboard.DB.get_all_scenarios()]
)


@server.route("/robots.txt")
def send_robots():
    """Don't list the website"""
    return send_from_directory("assets", "robots.txt")
