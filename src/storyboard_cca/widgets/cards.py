from dataclasses import dataclass


@dataclass
class CardWithButton:
    header: str
    subheading: str
    content: str
    href: str = "#"
    link: str = "Explore"
    footer: str = ""

    def __str__(self) -> str:
        return f"""<div class="card text-center m-2">
            <div class="card-header">
                {self.header}
            </div>
            <div class="card-body">
                <h5 class="card-title">{self.subheading}</h5>
                <div class="row mx-1 my-2 mh-100">
                    {self.content}
                </div>
                <a href="{self.href}" class="btn btn-primary">{self.link}</a>
            </div>
            <div class="card-footer text-muted">
                {self.footer}
            </div>
        </div>"""
