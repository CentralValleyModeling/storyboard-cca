from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment

from ..templates import templates
from ..widgets.cards import CardWithButton
from ..widgets.placeholders import PlaceholderImage, PlaceholderPage

router = APIRouter(prefix="", include_in_schema=False)


@router.get("/home", response_class=HTMLResponse)
async def get_home(request: Request):
    env: Environment = templates.env
    introduction = env.get_template("pages/home/introduction.jinja").render()
    hydrology = env.get_template("pages/home/hydrology.jinja").render()
    cards = [
        CardWithButton(
            "Infrastructure",
            "Additional Storage",
            PlaceholderImage(),
            router.url_path_for(get_sods.__name__),
        ),
        CardWithButton(
            "Infrastructure",
            "Delta Conveyance Project",
            PlaceholderImage(),
            router.url_path_for(get_tucp.__name__),
        ),
        CardWithButton(
            "Infrastructure",
            "FIRO",
            PlaceholderImage(),
        ),
        CardWithButton(
            "Operations",
            "Voluntary Agreements",
            PlaceholderImage(),
        ),
    ]

    return templates.TemplateResponse(
        name="pages/home/page.jinja",
        context={
            "request": request,
            "introduction": introduction,
            "hydrology": hydrology,
            "cards": cards,
        },
    )


@router.get("/south_of_delta_storage", response_class=HTMLResponse)
async def get_sods(request: Request):
    return templates.TemplateResponse(
        name="pages/south_of_delta_storage/page.jinja",
        context={
            "request": request,
        },
    )


@router.get("/tucp", response_class=HTMLResponse)
async def get_tucp(request: Request):
    return PlaceholderPage(request).encode()
