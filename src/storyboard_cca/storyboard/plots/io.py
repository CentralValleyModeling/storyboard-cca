from pathlib import Path

import plotly
import plotly.graph_objects

assets = Path(__file__).parent.parent.parent / "assets"


def from_file(src: str | Path, **kwargs) -> plotly.graph_objects.Figure:
    if not isinstance(src, Path):
        src = Path(src)
    if src.suffix == "":
        src = src.with_suffix(".json")
    if not src.exists():
        src = assets / src
    if not src.exists():
        raise FileNotFoundError(src)
    return plotly.io.read_json(src, **kwargs)


def to_file(
    dst: str | Path,
    fig: plotly.graph_objects.Figure,
    overwrite: bool = False,
    **kwargs,
):
    if not isinstance(dst, Path):
        dst = Path(dst)
    if dst.suffix == "":
        dst = dst.with_suffix(".json")
    if (overwrite is False) and dst.exists():
        raise FileExistsError(dst)
    kwargs = dict(pretty=True) | kwargs
    plotly.io.write_json(fig, dst, **kwargs)
