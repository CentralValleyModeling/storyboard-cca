import logging
import random
from pathlib import Path
from typing import Literal

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


def get_image(
    alt: str = "Placeholder image.",
    class_name: str = "",
    style: dict | None = None,
    limit: Literal["height", "width"] = "height",
    rounded: int = 0,
    **kwargs,
):
    return PlaceholderImage(
        src=get_image_src(),
        alt=alt,
        class_name=class_name,
        style=style,
        limit=limit,
        rounded=rounded,
        **kwargs,
    )


class PlaceholderImage(html.Img):
    def __init__(
        self,
        src: str,
        alt: str = "Placeholder image.",
        class_name: str = "",
        style: dict | None = None,
        rounded: int = 0,
        limit: Literal["height", "width"] = "height",
    ):
        if style is None:
            style = {limit: "100%", "object-fit": "cover"}
        class_name = class_name + f" card-img rounded-{rounded}"
        super().__init__(
            id=str(src),
            src=src,
            className=class_name,
            alt=alt,
            style=style,
        )
