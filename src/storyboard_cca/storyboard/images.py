from pathlib import Path

from dash.html import Img

assets = Path(__file__).parent.parent / "assets"


def from_file(
    src: str | Path,
    style: dict | None = None,
    class_name: str | None = None,
    **kwargs,
) -> Img:
    if not isinstance(src, Path):
        src = Path(src)
    if src.suffix == "":
        src = src.with_suffix(".png")
    if not src.exists():
        src = assets / src
    if not src.exists():
        raise FileNotFoundError(src)
    url = str(src.relative_to(assets.parent))
    if style is None:
        style = {"height": "100%", "object-fit": "cover"}
    if class_name is None:
        class_name = "card-img rounded-0"
    return Img(src=url, style=style, className=class_name, **kwargs)
