from pathlib import Path

import dash_bootstrap_components as dbc

from . import body, cards, features, layout, markdown, nav, placeholders, plots

ASSETS_DIR = Path(__file__).parent.parent / "assets"
STYLE_SHEETS = [
    "https://cdn.jsdelivr.net/npm/bootswatch@5.3.3/dist/cerulean/bootstrap.min.css",
    dbc.icons.BOOTSTRAP,
]
