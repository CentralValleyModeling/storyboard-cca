from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from ..templates import templates
from ..widgets.cards import CardWithButton
from ..widgets.placeholders import PlaceholderImage, PlaceholderPage, lorem

router = APIRouter(prefix="", include_in_schema=False)


@router.get("/home", response_class=HTMLResponse)
async def get_home(request: Request):
    narrative = f"<p>{lorem.SHORT}</p>"  # TODO: 2024-07-11 Make this load content

    cards = [
        CardWithButton(
            "Storage",
            "South of Delta Storage",
            PlaceholderImage(),
            router.url_path_for(get_sods.__name__),
        ),
        CardWithButton(
            "Operations",
            "Temporary Use Change Permits",
            PlaceholderImage(),
            router.url_path_for(get_tucp.__name__),
        ),
        CardWithButton(
            "Operations",
            "Temporary Use Change Permits",
            PlaceholderImage(),
        ),
        CardWithButton(
            "Operations",
            "Voluntary Agreements",
            PlaceholderImage(),
        ),
        CardWithButton(
            "Storage",
            "South of Delta Storage",
            PlaceholderImage(),
        ),
        CardWithButton(
            "Storage",
            "South of Delta Storage",
            PlaceholderImage(),
        ),
    ]

    return templates.TemplateResponse(
        name="pages/home/page.jinja",
        context={
            "request": request,
            "narrative": narrative,
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
