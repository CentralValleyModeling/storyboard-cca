import dash
import storyboard

dash.register_page(__name__)


def layout():
    return storyboard.Page(children=storyboard.markdown.from_file("errors/404"))
