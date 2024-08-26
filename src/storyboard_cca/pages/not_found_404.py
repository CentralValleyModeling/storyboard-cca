import dash
import widgets

dash.register_page(__name__)


def layout():
    return widgets.layout.LayoutCCA(children=widgets.markdown.from_file("errors/404"))
