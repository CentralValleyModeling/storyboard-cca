import pandas as pd
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment

from ..data import RUNS, SCEANRIOS, client
from ..templates import templates
from ..widgets import plots
from ..widgets.cards import CardWithButton
from ..widgets.placeholders import PlaceholderImage, PlaceholderPage

router = APIRouter(prefix="", include_in_schema=False)


def temp_get_data(
    path: str = "/.*/SWP_TA_TOTAL/SWP_DELIVERY/.*/.*/.*/",
) -> dict[str, pd.DataFrame]:
    frames = dict()
    for s in SCEANRIOS:
        r = RUNS[s.name][0]
        rts_1 = client.get_timeseries(
            scenario=r.scenario,
            version=r.version,
            path=path,
        )
        try:
            frames[s.name] = rts_1.to_frame()
        except Exception:
            pass
    return frames


@router.get("/home", response_class=HTMLResponse)
async def get_home(request: Request):
    env: Environment = templates.env
    introduction = env.get_template("pages/home/introduction.jinja").render()
    hydrology = env.get_template("pages/home/hydrology.jinja").render()
    oro = temp_get_data()
    oro_storage = {
        k: v
        for k, v in oro.items()
        if k in ("Baseline", "2043 50% LOC - SODS + Maintain")
    }
    plot_1 = plots.line(oro_storage, y_label="Table A Deliveries (CFS)")

    cards = [
        CardWithButton(
            "Infrastructure",
            "Additional Storage",
            f"{plot_1}<p>Additional storage South of the Delta allows Oroville to "
            + "retain more water during droughts.</p>",
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
    return PlaceholderPage(request).encode()


@router.get("/tucp", response_class=HTMLResponse)
async def get_tucp(request: Request):
    return PlaceholderPage(request).encode()


@router.get("/explore", response_class=HTMLResponse)
async def get_explore(request: Request):
    return PlaceholderPage(request).encode()
