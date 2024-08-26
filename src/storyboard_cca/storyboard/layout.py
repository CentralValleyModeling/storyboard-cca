import dash_bootstrap_components as dbc
from dash import html, page_container

from . import body, nav


class Layout(html.Div):
    def __init__(
        self,
        links: list[dbc.NavLink] | None = None,
    ):
        super().__init__(
            children=[
                nav.NavBar(links=links),
                page_container,
                body.Footer(),
            ],
        )
