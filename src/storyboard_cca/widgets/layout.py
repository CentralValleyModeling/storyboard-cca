from typing import Any

import dash_bootstrap_components as dbc
from dash import html

from . import body, nav


class LayoutCCA(html.Div):
    def __init__(
        self,
        header: Any | None = None,
        children: Any | None = None,
        links: list[dbc.NavLink] | None = None,
    ):
        super().__init__(
            children=[
                nav.NavBarCCA(links=links),
                body.MainCCA(header=header, children=children),
                body.FooterCCA(),
            ]
        )
