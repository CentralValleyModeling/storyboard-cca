from dataclasses import dataclass
from typing import Literal

import requests


@dataclass
class LoremIpsum:
    paragraphs: int = 1
    length: Literal["short", "medium", "long"] = "medium"
    _content: str | None = None

    def _set_content_from_api(self) -> str:
        url = f"https://loripsum.net/api/{self.paragraphs}/{self.length}"
        self._content = requests.get(url, params={}).content.decode()

    def __str__(self) -> str:
        if self._content is None:
            self._set_content_from_api()
        return self._content


SHORT = LoremIpsum(paragraphs=1)
