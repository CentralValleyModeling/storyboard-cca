import logging
import random

from dash import get_asset_url, html

logger = logging.getLogger(__name__)


image_options = [
    "images/placeholders/19671110_Oroville_Const.jpg",
    "images/placeholders/19570915_Ozalid_Machine.jpg",
    "images/placeholders/19591117_Frenchman_Dam_Const.jpg",
]
random.shuffle(image_options)


def get_image():
    logger.info("getting a placeholder image")
    p = image_options.pop(0)
    image_options.append(p)

    return PlaceholderImage(src=get_asset_url(p))


class PlaceholderImage(html.Img):
    def __init__(
        self,
        src: str,
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
