import dash_bootstrap_components as dbc
from dash import get_asset_url, html

BRAND_IMG_SRC = "images/calsim3_icon.svg"


class CalSim3Img(html.Img):
    def __init__(self, **kwargs):
        cca_kwargs = dict(
            id="calsim3-icon",
            src=get_asset_url(BRAND_IMG_SRC),
            alt="CalSim3 Icon.",
            width=30,
            height=24,
            className="d-inline-block align-text-top",
        )
        cca_kwargs.update(kwargs)
        super().__init__(**cca_kwargs)


class Brand(dbc.NavbarBrand):
    def __init__(self, **kwargs):
        cca_kwargs = dict(
            id="calsim3-navbar-brand",
            children=CalSim3Img(),
            href="/",
            className="navbar-brand",
        )
        cca_kwargs.update(kwargs)
        super().__init__(**cca_kwargs)
