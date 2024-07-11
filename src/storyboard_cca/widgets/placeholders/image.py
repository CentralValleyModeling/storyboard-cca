from dataclasses import dataclass


@dataclass
class PlaceholderImage:
    src: str = "https://placehold.co/240x120"
    alt: str = "Placeholder image."

    def __str__(self) -> str:
        bootstrap = "img-fluid rounded mx-auto d-block"
        return f'<img src={self.src} class="{bootstrap}" alt={self.alt}>'
