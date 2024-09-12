from pathlib import Path
from typing import Any, Literal, Self

import dash_bootstrap_components as dbc
from dash import html
from pandas import read_csv

assets = Path(__file__).parent.parent / "assets"
LEVELS = {
    1: html.H1,
    2: html.H2,
    3: html.H3,
    4: html.H4,
    5: html.H5,
    6: html.H6,
}


class BannerImage(html.Div):
    def __init__(
        self,
        title: str,
        image: html.Img,
        paragraph: str | None = None,
        title_level: int = 1,
        bar_color: str = "bg-primary",
    ):
        header_level = LEVELS.get(title_level, html.H6)
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
        main_div_class = " ".join(
            [
                "card",
                "bg-inverse",
                "rounded-0",
                "h-100",
            ]
        )
        super().__init__(
            className=main_div_class,
            children=[
                image,
                html.Div(
                    className=card_overlay_class,
                    children=html.Div(
                        className=f"{bar_color} p-2",
                        style={"--bs-bg-opacity": 0.50},
                        children=[
                            header_level(
                                className="card-title text-light m-0",
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
        priority: Literal["left", "right"] = "left",
        minor_col_steps: dict[str, int] | None = None,
        border: bool | str = True,
        shadow: bool = True,
        margin_y: int = 0,
        **kwargs,
    ):
        uuid = id(object())
        class_name = "mx-0"
        if border:
            if isinstance(border, str):
                class_name = class_name + " " + border
            else:
                class_name = class_name + " border-top border-bottom border-primary"
        if shadow:
            class_name = class_name + " shadow"
        if margin_y:
            class_name = class_name + f" my-{margin_y}"
        cca_kwargs = dict(
            class_name=class_name,
        )
        cca_kwargs.update(kwargs)
        # Set up the class names for each side
        col_L = "overflow-auto scroll-by ps-0"
        col_R = "overflow-auto scroll-by ps-0"
        # Set up the breakpoints of the minor column
        minor_col_steps_used = dict(xs=1, sm=1, md=2, lg=3, xl=3, xxl=3)
        if minor_col_steps:
            minor_col_steps_used.update(minor_col_steps)
        minor_col = " "
        for breakpoint, size in minor_col_steps_used.items():
            if breakpoint == "xs":
                minor_col = minor_col + f" col-{size}"
            else:
                minor_col = minor_col + f" col-{breakpoint}-{size}"
        if priority == "left":
            col_R = col_R + minor_col
        elif priority == "right":
            col_L = col_L + minor_col
        super().__init__(
            children=[
                dbc.Col(
                    id=f"left-{uuid}",
                    children=left,
                    style={"height": height_limit},
                    class_name=col_L,
                ),
                dbc.Col(
                    id=f"right-{uuid}",
                    children=right,
                    style={"height": height_limit},
                    class_name=col_R,
                ),
            ],
            **cca_kwargs,
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
