from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from ..templates import templates
from ..widgets.cards import CardWithButton
from ..widgets.placeholders import Image

router = APIRouter(prefix="", include_in_schema=False)


@router.get("/home", response_class=HTMLResponse)
async def get_home(request: Request):
    narrative = """<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus 
    lectus justo, molestie finibus leo nec, gravida ullamcorper nunc. In hac habitasse 
    platea dictumst. Ut fermentum orci non quam suscipit dignissim. Phasellus quis 
    neque in diam laoreet hendrerit. Aenean convallis interdum massa eu ornare. Nunc 
    at sapien et ligula tempus mollis. Nullam vulputate fringilla sapien sit amet 
    dapibus. Nam augue erat, dictum eu efficitur sed, suscipit eget elit. Phasellus 
    pretium pulvinar vestibulum.</p>"""

    cards = [
        CardWithButton(
            "Storage",
            "South of Delta Storage",
            Image(),
            router.url_path_for(get_sods.__name__),
        ),
        CardWithButton(
            "Operations",
            "Temporary Use Change Permits",
            Image(),
        ),
        CardWithButton(
            "Operations",
            "Temporary Use Change Permits",
            Image(),
        ),
        CardWithButton(
            "Operations",
            "Voluntary Agreements",
            Image(),
        ),
        CardWithButton(
            "Storage",
            "South of Delta Storage",
            Image(),
        ),
        CardWithButton(
            "Storage",
            "South of Delta Storage",
            Image(),
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
