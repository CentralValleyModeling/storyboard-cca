import logging
import random
from pathlib import Path

from dash import get_asset_url, html

logger = logging.getLogger(__name__)

here = Path(__file__)
asset_dir = here.parent.parent.parent / "assets"
placeholder_img_dir = asset_dir / "images/placeholders"
image_options = [
    str(p.relative_to(asset_dir))
    for p in placeholder_img_dir.iterdir()
    if p.suffix in (".jpg", ".jpeg", ".png")
]
random.shuffle(image_options)


def get_image_src():
    logger.info("getting a placeholder image")
    p = image_options.pop(0)
    image_options.append(p)

    return get_asset_url(p)


def get_image(**kwargs):
    return PlaceholderImage(src=get_image_src(), **kwargs)


class PlaceholderImage(html.Img):
    def __init__(
        self,
        src: str,
        alt: str = "Placeholder image.",
        class_name: str = "card-img rounded-0",
        style: dict | None = None,
    ):
        if style is None:
            style = {"height": "100%", "object-fit": "cover"}
        super().__init__(
            id=str(src),
            src=src,
            className=class_name,
            alt=alt,
            style=style,
        )
