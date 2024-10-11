import re
from pathlib import Path

from dash.dcc import Markdown

assets = Path(__file__).parent.parent / "assets"


def from_file(src: str | Path, float_to: str | None = None, **kwargs) -> Markdown:
    if not isinstance(src, Path):
        src = Path(src)
    if src.suffix == "":
        src = src.with_suffix(".md")
    if not src.exists():
        src = assets / src
    if not src.exists():
        raise FileNotFoundError(src)
    with open(src, "r") as SRC:
        txt = SRC.read()
    txt = re.sub(r"<!--.*-->", "", txt)  # Remove HTML style comments
    if float_to:
        float_to = {"className": f"float-{float_to}"}
    else:
        float_to = {}
    kwargs = dict(style={"max-width": "80ch", "min-width": "20em"}, **float_to) | kwargs
    return Markdown(txt, **kwargs)
