from pathlib import Path

from dash import html


class TitleImageOverlay(html.Div):
    def __init__(
        self,
        title: str,
        image: html.Img,
        paragraph: str | None = None,
    ):
        paragraph_objects = []
        if paragraph:
            for txt in paragraph.split("\n"):
                paragraph_objects.append(html.P(className="card-text", children=txt))
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
                        className="bg-light p-2",
                        style={"--bs-bg-opacity": 0.5},
                        children=[
                            html.H3(
                                className="card-title",
                                children=title,
                            ),
                            *paragraph_objects,
                        ],
                    ),
                ),
            ],
        )
