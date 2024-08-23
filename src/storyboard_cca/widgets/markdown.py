import re
from pathlib import Path

from dash.dcc import Markdown

assets = Path(__file__).parent.parent / "assets/text"


def from_file(src: str | Path) -> Markdown:
    if not isinstance(src, Path):
        src = Path(src)
    if not src.suffix == ".md":
        src = src.with_suffix(".md")
    if not src.exists():
        src = assets / src
    if not src.exists():
        raise FileNotFoundError(src)
    with open(src, "r") as SRC:
        txt = SRC.read()
    txt = re.sub(r"<!--.*-->", "", txt)  # Remove HTML style comments
    return Markdown(txt)
