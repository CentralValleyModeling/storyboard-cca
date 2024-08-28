from typing import Any

import dash_bootstrap_components as dbc
from dash import html, page_container

from . import body
from .brand import Brand

GITHUB_HREF = "https://github.com/CentralValleyModeling/storyboard-cca"


def get_icon(s: str) -> html.I:
    return html.I(className=f"bi bi-{s}")


class Nav(dbc.Nav):
    def __init__(
        self,
        links: list[dbc.NavLink] | None = None,
        **kwargs,
    ):
        if links is None:
            links = [
                dbc.NavLink("Home", href="/home"),
                dbc.NavLink("Climate Change", href="/climate-change"),
                dbc.NavLink("Adaptation", href="/adaptation"),
            ]
        cca_kwargs = dict(
            className="navbar-nav",
            navbar=True,
        )
        cca_kwargs.update(kwargs)
        super().__init__(children=[dbc.NavItem(link) for link in links], **cca_kwargs)


class NavBar(dbc.Navbar):
    def __init__(
        self,
        links: list[dbc.NavLink] | None = None,
        **kwargs,
    ):
        cca_kwargs = dict(
            className="navbar navbar-expand-md bg-body-secondary border-bottom",
        )
        cca_kwargs.update(kwargs)
        super().__init__(
            children=dbc.Container(
                fluid=True,
                children=[
                    Brand(),
                    dbc.NavbarToggler(id="cca-navbar-toggler"),
                    dbc.Collapse(
                        Nav(links=links),
                        id="cca-navbar-nav-dropdown",
                        navbar=True,
                    ),
                ],
            ),
            **cca_kwargs,
        )


class IconLink(html.A):
    def __init__(self, icon: str, href: str, **kwargs):
        cca_kwargs = dict(
            children=get_icon(icon),
            href=href,
            className="nav-link px-2 text-body-secondary",
        )
        cca_kwargs.update(kwargs)
        super().__init__(**cca_kwargs)


class Page(html.Main):
    def __init__(
        self,
        header: Any | None = None,
        children: Any | None = None,
    ):
        content = list()
        if header:
            content.append(header)
        if children:
            if isinstance(children, list):
                children = html.Div(children, className="my-3")
            content.append(children)
        super().__init__(children=content)


class Footer(dbc.Container):
    def __init__(self, **kwargs):
        footer_class = " ".join(
            [
                "d-flex",
                "flex-wrap",
                "justify-content-between",
                "align-items-center",
                "py-1",
                "px-3",
                "border-top",
            ]
        )
        ul_list_class = " ".join(
            [
                "nav",
                "col-md-4",
                "justify-content-end",
                "align-items-center",
                "list-unstyled",
                "d-flex",
            ]
        )
        cca_kwargs = dict(
            className=footer_class,
            children=[
                dbc.Col(
                    md=4,
                    class_name="flex-wrap d-flex align-items-center",
                    children=html.Span(
                        "CA Department of Water Resources",
                        className="mb-3 mb-md-0 text-body-secondary",
                    ),
                ),
                html.Ul(
                    className=ul_list_class,
                    children=[
                        html.Li(IconLink("house-fill", "/home"), className="nav-item"),
                        html.Li(IconLink("github", GITHUB_HREF), className="nav-item"),
                    ],
                ),
            ],
        )
        cca_kwargs.update(kwargs)
        super().__init__(
            children=html.Footer(**cca_kwargs),
            class_name="m-0 p-0",
            fluid=True,
        )


class AppLayout(html.Div):
    def __init__(
        self,
        links: list[dbc.NavLink] | None = None,
    ):
        super().__init__(
            id="app-layout",
            children=[
                NavBar(links=links),
                page_container,
                body.Footer(),
            ],
        )
