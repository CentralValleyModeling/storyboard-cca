from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from . import __version__

TITLE = ""
SUMMARY = ""
DESCRIPTION = """"""
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
