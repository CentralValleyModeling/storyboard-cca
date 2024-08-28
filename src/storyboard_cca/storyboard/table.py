from pathlib import Path

from dash.dash_table import DataTable
from pandas import read_csv

assets = Path(__file__).parent.parent / "assets"


def from_file(src: str | Path) -> DataTable:
    if not isinstance(src, Path):
        src = Path(src)
    if src.suffix == "":
        src = src.with_suffix(".csv")
    if not src.exists():
        src = assets / src
    if not src.exists():
        raise FileNotFoundError(src)
    df = read_csv(src)
    return DataTable(df.to_dict("records"), [{"name": i, "id": i} for i in df.columns])
