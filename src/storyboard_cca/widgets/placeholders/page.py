from dataclasses import dataclass

from fastapi import Request

from ...templates import csrs_templates


@dataclass
class PlaceholderPage:
    request: Request

    def encode(self):
        return csrs_templates.TemplateResponse(
            name="pages/placeholder.jinja",
            context={
                "request": self.request,
            },
        )
