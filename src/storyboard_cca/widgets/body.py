import dash_bootstrap_components as dbc
from dash import html

from .nav import GITHUB_HREF


def get_icon(s: str) -> html.I:
    return html.I(className=f"bi bi-{s}")


class IconLink(html.A):
    def __init__(self, icon: str, href: str, **kwargs):
        cca_kwargs = dict(
            children=get_icon(icon),
            href=href,
            className="nav-link px-2 text-body-secondary",
        )
        cca_kwargs.update(kwargs)
        super().__init__(**cca_kwargs)


class MainCCA(html.Main):
    def __init__(self, **kwargs):
        cca_kwargs = dict()
        cca_kwargs.update(kwargs)
        super().__init__(children=dbc.Container(**cca_kwargs))


class FooterCCA(dbc.Container):
    def __init__(self, **kwargs):
        container_class = " ".join(
            [
                "d-flex",
                "flex-wrap",
                "justify-content-between",
                "align-items-center",
                "py-1",
                "px-4",
                "border-top",
            ]
        )
        ul_list = " ".join(
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
            className=container_class,
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
                    className=ul_list,
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
            class_name="m-0",
            fluid=True,
        )
