from pathlib import Path
from typing import Any, Self

import dash_bootstrap_components as dbc
from dash import html
from pandas import read_csv

assets = Path(__file__).parent.parent / "assets"


class BannerImage(html.Div):
    def __init__(
        self,
        title: str,
        image: html.Img,
        paragraph: str | None = None,
    ):
        paragraph_objects = []
        if paragraph:
            for txt in paragraph.split("\n"):
                paragraph_objects.append(
                    html.P(
                        className="card-text text-light ms-2",
                        children=txt,
                    )
                )
        card_overlay_class = " ".join(
            [
                "card-img-overlay",
                "p-0",
                "rounded-0",
                "d-flex",
                "justify-content-end",
                "flex-column",
            ]
        )
        super().__init__(
            className="card bg-inverse rounded-0",
            children=[
                image,
                html.Div(
                    className=card_overlay_class,
                    children=html.Div(
                        className="bg-primary p-2",
                        style={"--bs-bg-opacity": 0.50},
                        children=[
                            html.H1(
                                className="card-title text-light",
                                children=title,
                            ),
                            *paragraph_objects,
                        ],
                    ),
                ),
            ],
        )


class ScrollBy(dbc.Row):
    def __init__(
        self,
        left: Any,
        right: Any,
        height_limit: str = "50vh",
        left_width: int = 6,
    ):
        uuid = id(object())

        super().__init__(
            children=[
                dbc.Col(
                    id=f"left-{uuid}",
                    children=left,
                    style={"height": height_limit},
                    class_name="overflow-auto scroll-by ps-0",
                    width=left_width,
                ),
                dbc.Col(
                    id=f"right-{uuid}",
                    children=right,
                    style={"height": height_limit},
                    class_name="overflow-auto scroll-by pe-0",
                ),
            ],
            class_name="mx-0 my-5 shadow border-top border-bottom border-primary",
        )


class LinksBin(html.Div):
    def __init__(
        self,
        links: list[tuple[str, str]],
        title: str = "More",
        **kwargs,
    ):
        link_list = [
            html.A(
                link[0],
                className="list-group-item list-group-item-action",
                href=link[1],
                target="_blank",
            )
            for link in links
        ]

        kwargs = (
            dict(
                className="border border-secondary p-2 rounded-1",
            )
            | kwargs
        )
        super().__init__(
            children=[
                html.H5(title),
                html.Ul(
                    link_list,
                    className="list-group",
                ),
            ],
            **kwargs,
        )

    @classmethod
    def from_csv(cls, src: str | Path, **kwargs) -> Self:
        if not isinstance(src, Path):
            src = Path(src)
        if src.suffix == "":
            src = src.with_suffix(".csv")
        if not src.exists():
            src = assets / src
        if not src.exists():
            raise FileNotFoundError(src)
        df = read_csv(src)
        df.columns = [c.upper() for c in df.columns]
        links = list()
        for _, row in df.iterrows():
            links.append((row["P"], row["HREF"]))
        return cls(links=links, **kwargs)
