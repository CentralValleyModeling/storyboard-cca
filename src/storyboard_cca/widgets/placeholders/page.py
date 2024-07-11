from dataclasses import dataclass

from fastapi import Request

from ...templates import templates


@dataclass
class PlaceholderPage:
    request: Request

    def encode(self):
        return templates.TemplateResponse(
            name="pages/placeholder.jinja",
            context={
                "request": self.request,
            },
        )
