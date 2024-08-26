import dash_bootstrap_components as dbc

from .brand import Brand

GITHUB_HREF = "https://github.com/CentralValleyModeling/storyboard-cca"


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
