import dash_bootstrap_components as dbc
from dash import html

BRAND_IMG_SRC = (
    "https://raw.githubusercontent.com/CentralValleyModeling"
    + "/static-assets/main/images/calsim3_icon.svg"
)


class ImgCCA(html.Img):
    def __init__(self, **kwargs):
        cca_kwargs = dict(
            src=BRAND_IMG_SRC,
            alt="CalSim3 Icon.",
            width=30,
            height=24,
            className="d-inline-block align-text-top",
        )
        cca_kwargs.update(kwargs)
        super().__init__(**cca_kwargs)


class BrandCCA(dbc.NavbarBrand):
    def __init__(self, **kwargs):
        cca_kwargs = dict(
            children=html.A(ImgCCA()),
            id="cca-navbar-brand",
            href="/home",
            className="navbar-brand",
        )
        cca_kwargs.update(kwargs)
        super().__init__(**cca_kwargs)
