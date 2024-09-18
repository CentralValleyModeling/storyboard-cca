from pathlib import Path
from typing import Literal

import dash_bootstrap_components as dbc
from dash import html
from pandas import read_csv

assets = Path(__file__).parent.parent / "assets"


def from_file(
    src: str | Path,
    kind: Literal["title_only", "paragraph"] = "title_only",
) -> list[dbc.Card]:
    if not isinstance(src, Path):
        src = Path(src)
    if src.suffix == "":
        src = src.with_suffix(".csv")
    if not src.exists():
        src = assets / src
    if not src.exists():
        raise FileNotFoundError(src)
    df = read_csv(src)

    cards = list()
    for _, row in df.iterrows():
        row = row.copy()
        # Style the card
        if "color" in row:
            color = row.pop("color")
        else:
            color = "light"
        # Construct the card body
        if kind == "title_only":
            body = row.iloc[0]
        elif kind == "paragraph":
            body = [html.P(r) for r in row.iloc[2:]]
        else:
            raise NotImplementedError(f"{kind=} is not supported")
        cards.append(
            dbc.Card(
                [
                    dbc.CardBody(
                        body,
                        class_name="p-1",
                    ),
                ],
                class_name="m-1",
                color=color,
            )
        )
    return cards
