import dash_bootstrap_components as dbc

from .brand import BrandCCA

GITHUB_HREF = "https://github.com/CentralValleyModeling/storyboard-cca"


class NavCCA(dbc.Nav):
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


class NavBarCCA(dbc.Navbar):
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
                    BrandCCA(),
                    dbc.NavbarToggler(id="cca-navbar-toggler"),
                    dbc.Collapse(
                        NavCCA(links=links),
                        id="cca-navbar-nav-dropdown",
                        navbar=True,
                    ),
                ],
            ),
            **cca_kwargs,
        )
