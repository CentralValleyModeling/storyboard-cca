from dataclasses import dataclass


@dataclass
class PlaceholderImage:
    src: str = "https://placehold.co/320x160"
    alt: str = "Placeholder image."

    def __str__(self) -> str:
        return f'<img src={self.src} class="rounded mx-auto d-block" alt={self.alt}>'
