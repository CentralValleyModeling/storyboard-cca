from pathlib import Path
from typing import Any, Iterable, Literal

import dash_bootstrap_components as dbc
from dash import html
from dash.dash_table import DataTable
from pandas import read_csv

assets = Path(__file__).parent.parent / "assets"


class Table(dbc.Table):
    def __init__(self, header: Iterable[Any], body: Iterable[Iterable[Any]], **kwargs):
        header = html.Thead(
            html.Tr(
                [html.Th(str(h)) for h in header],
            )
        )
        b = list()
        for row in body:
            r = html.Tr([html.Td(str(i)) for i in row])
            b.append(r)
        body = html.Tbody(b)
        super().__init__(children=[header, body], **kwargs)


def from_file(
    src: str | Path,
    kind: Literal["data", "bootstrap"] = "data",
    **kwargs,
) -> DataTable | Table:
    if not isinstance(src, Path):
        src = Path(src)
    if src.suffix == "":
        src = src.with_suffix(".csv")
    if not src.exists():
        src = assets / src
    if not src.exists():
        raise FileNotFoundError(src)
    df = read_csv(src)
    if kind == "data":
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
    elif kind == "bootstrap":
        return Table(
            header=df.columns,
            body=df.to_records(index=False),
            **kwargs,
        )
    else:
        raise NotImplementedError(f"{kind=} is not supported")
