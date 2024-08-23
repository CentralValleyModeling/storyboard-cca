import logging
import random
from pathlib import Path

from dash import html
from fastapi import APIRouter
from fastapi.responses import FileResponse

root = Path(__file__).parent.parent.parent
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/placeholder", include_in_schema=False)

image_options = [
    "assets/images/placeholders/19671110_Oroville_Const.jpg",
    "assets/images/placeholders/19570915_Ozalid_Machine.jpg",
    "assets/images/placeholders/19591117_Frenchman_Dam_Const.jpg",
]
random.shuffle(image_options)


@router.get("/image", response_class=FileResponse)
def get_image():
    logger.info("getting a placeholder image")
    i = image_options.pop(0)
    image_options.append(i)
    f = root / i
    return f


class PlaceholderImage(html.Img):
    def __init__(
        self,
        src: str = "/placeholder/image",
        alt: str = "Placeholder image.",
        class_name: str = "card-img rounded-0",
        style: dict | None = None,
    ):
        if style is None:
            style = {"height": "300px", "object-fit": "cover"}
        super().__init__(
            src=src,
            className=class_name,
            alt=alt,
            style=style,
        )
