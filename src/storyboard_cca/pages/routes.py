import pandas as pd
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment

from ..data import DATA_CACHE
from ..templates import templates
from ..widgets import plots
from ..widgets.cards import CardWithButton
from ..widgets.placeholders import PlaceholderImage, PlaceholderPage

router = APIRouter(prefix="", include_in_schema=False)


@router.get("/home", response_class=HTMLResponse)
async def get_home(request: Request):
    env: Environment = templates.env
    introduction = env.get_template("pages/home/introduction.jinja").render()
    hydrology = env.get_template("pages/home/hydrology.jinja").render()
    storage_data = DATA_CACHE.get_timeseries("/.*/S_SLUIS/STORAGE/.*/.*/.*/")
    exports_data = DATA_CACHE.get_timeseries("/.*/D_OMR027_CAA000/DIVERSION/.*/.*/.*/")
    # Identify storage scenarios
    storage_scenarios = [
        k for k in storage_data if (("Baseline" in k) or ("SODS" in k))
    ]
    dcp_scenarios = [k for k in storage_data if (("Baseline" in k) or ("DCP" in k))]

    plot_storage = plots.monthly(
        {k: v for k, v in storage_data.items() if k in storage_scenarios},
        y_label="Storage in San Luis (TAF)",
    )
    plot_dcp = plots.exceedance(
        {k: v for k, v in exports_data.items() if k in dcp_scenarios},
        y_label="Exports at Banks (TAF)",
    )

    cards = [
        CardWithButton(
            header="Infrastructure",
            subheading="Additional Storage",
            content=plot_storage,
            href=router.url_path_for(get_sods.__name__),
            footer="Additonal text",
        ),
        CardWithButton(
            "Infrastructure",
            "Delta Conveyance Project",
            plot_dcp,
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
    return PlaceholderPage(request).encode()


@router.get("/tucp", response_class=HTMLResponse)
async def get_tucp(request: Request):
    return PlaceholderPage(request).encode()


@router.get("/explore", response_class=HTMLResponse)
async def get_explore(request: Request):
    return PlaceholderPage(request).encode()
