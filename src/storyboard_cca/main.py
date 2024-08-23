import csrs
import csrs.config
from fastapi import FastAPI, Request
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import RedirectResponse

from . import logger, pages, templates, widgets

csrs.config.configure_logging(logger)

app_cfg = csrs.config.AppConfig()
app = FastAPI(**app_cfg.model_dump())
app.mount("/home", WSGIMiddleware(pages.home.server))
app.include_router(widgets.placeholders.router)


@app.get("/", response_class=RedirectResponse, status_code=302, include_in_schema=False)
async def redirect_home():
    return RedirectResponse("/home")


@app.exception_handler(404)
async def custom_404_handler(request: Request, __):
    logger.warning(f"404 returned for request={request.url}")
    return templates.csrs_templates.TemplateResponse(
        "errors/404.jinja",
        {"request": request},
        status_code=404,
    )
