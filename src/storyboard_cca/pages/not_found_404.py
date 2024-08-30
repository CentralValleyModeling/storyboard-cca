import dash
import storyboard

dash.register_page(__name__)


def layout():
    return storyboard.Page(children=storyboard.text.from_file("text/errors/404"))
