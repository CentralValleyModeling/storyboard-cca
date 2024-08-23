import csrs
import csrs.config
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from . import __version__, logger, pages, widgets
from .templates import templates

csrs.config.configure_logging(logger)

TITLE = "STORYBOARD_CCA"
SUMMARY = "Story Charts for the SWP CCA Studies"
DESCRIPTION = """Story Charts for the SWP CCA Studies."""
CONTACT = {
    "name": "California DWR, Central Valley Modeling",
    "url": "https://water.ca.gov/Library/"
    + "Modeling-and-Analysis/Central-Valley-models-and-tools",
}
LISCENSE = {
    "name": "MIT",
    "identifier": "MIT",
}


# log the environment args
app = FastAPI(
    title=TITLE,
    summary=SUMMARY,
    version=__version__ or "dev",
    docs_url="/docs",
    description=DESCRIPTION,
    contact=CONTACT,
    license_info=LISCENSE,
)

app.include_router(pages.router)
app.include_router(widgets.placeholders.image.router)


@app.get(
    "/",
    response_class=RedirectResponse,
    status_code=302,
    include_in_schema=False,
)
async def redirect_home():
    return RedirectResponse("/home")


@app.exception_handler(404)
async def custom_404_handler(request: Request, __):
    logger.warning(f"404 returned for request={request.url}")
    return templates.TemplateResponse(
        "errors/404.jinja",
        {"request": request},
        status_code=404,
    )
