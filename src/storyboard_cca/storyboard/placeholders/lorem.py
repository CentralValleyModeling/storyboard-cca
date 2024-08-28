from functools import lru_cache
from typing import Literal

import dash
import requests


@lru_cache()
def get_lorem(
    paragraphs: int = 1,
    length: Literal["short", "medium", "long"] = "medium",
) -> list[str]:
    url = f"https://loripsum.net/api/{paragraphs}/{length}"
    html_p = requests.get(url, params={}, verify=False).content.decode()
    return [t.strip().strip("</p>") for t in html_p.strip("<p>").split("<p>")]


class LoremIpsum(dash.html.Div):
    def __init__(
        self,
        paragraphs: int = 1,
        length: Literal["short", "medium", "long"] = "medium",
        **kwargs,
    ):
        txt = get_lorem(paragraphs, length)
        p = [dash.html.P(t) for t in txt]
        super().__init__(p, **kwargs)
