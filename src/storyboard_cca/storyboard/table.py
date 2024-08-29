from pathlib import Path

from dash.dash_table import DataTable
from pandas import read_csv

assets = Path(__file__).parent.parent / "assets"


def from_file(src: str | Path, **kwargs) -> DataTable:
    if not isinstance(src, Path):
        src = Path(src)
    if src.suffix == "":
        src = src.with_suffix(".csv")
    if not src.exists():
        src = assets / src
    if not src.exists():
        raise FileNotFoundError(src)
    df = read_csv(src)
    cca_kwargs = dict(
        id=str(src),
        style_data=dict(
            whiteSpace="normal",
            height="auto",
            lineHeight="15px",
        ),
        style_table=dict(overflowX="auto"),
        data=df.to_dict("records"),
        columns=[{"name": i, "id": i} for i in df.columns],
    )
    cca_kwargs.update(kwargs)
    return DataTable(**cca_kwargs)
