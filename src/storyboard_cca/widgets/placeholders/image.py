import logging
import random
from dataclasses import dataclass
from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

root = Path(__file__).parent.parent.parent
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/placeholder", include_in_schema=False)

image_options = [
    "static/images/placeholders/19671110_Oroville_Const.jpg",
    "static/images/placeholders/19570915_Ozalid_Machine.jpg",
    "static/images/placeholders/19591117_Frenchman_Dam_Const.jpg",
]
random.shuffle(image_options)


@router.get("/image", response_class=FileResponse)
def get_image():
    logger.info("getting a placeholder image")
    i = image_options.pop(0)
    image_options.append(i)
    f = root / i
    return f


@dataclass
class PlaceholderImage:
    src: str = "https://placehold.co/240x120"
    alt: str = "Placeholder image."

    def __str__(self) -> str:
        bootstrap = "img-fluid rounded mx-auto d-block"
        return f'<img src={self.src} class="{bootstrap}" alt={self.alt}>'


@dataclass
class PlaceholderFeatureImage:
    src: str = "/placeholder/image"
    alt: str = "Placeholder image."

    def __str__(self) -> str:
        bootstrap = "card-img"
        return f'<img src={self.src} class="{bootstrap}" alt="{self.alt}">'
