import logging

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment

from .. import widgets
from ..database import DATA_CACHE
from ..templates import templates
from ..widgets.cards import CardWithButton
from ..widgets.placeholders import PlaceholderImage, PlaceholderPage

router = APIRouter(prefix="", include_in_schema=False)
logger = logging.getLogger(__name__)


@router.get("/home", response_class=HTMLResponse)
async def get_home(request: Request):
    env: Environment = templates.env

    introduction = env.get_template("pages/home/introduction.jinja").render()
    adaptations = env.get_template("pages/home/adaptations.jinja").render()
    hydrology = env.get_template("pages/home/hydrology.jinja").render()

    return templates.TemplateResponse(
        name="pages/home/page.jinja",
        context={
            "request": request,
            "introduction": introduction,
            "hydrology": hydrology,
            "adaptations": adaptations,
        },
    )


@router.get("/south_of_delta_storage", response_class=HTMLResponse)
async def get_sods(request: Request):
    return PlaceholderPage(request).encode()


@router.get("/tucp", response_class=HTMLResponse)
async def get_tucp(request: Request):
    return PlaceholderPage(request).encode()


@router.get("/explore", response_class=HTMLResponse)
async def get_explore(request: Request):
    return PlaceholderPage(request).encode()


@router.get("/widget", response_class=HTMLResponse)
async def get_widget(request: Request):
    env: Environment = templates.env
    w = widgets.features.TitleImageOverlay(
        title="Example",
        image=widgets.placeholders.PlaceholderFeatureImage(),
        paragraph="This is how text on an image can look.",
    )
    return templates.TemplateResponse(
        name="pages/testing.jinja",
        context={
            "request": request,
            "content": w,
        },
    )
