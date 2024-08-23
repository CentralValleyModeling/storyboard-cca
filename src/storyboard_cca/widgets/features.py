from dataclasses import dataclass


@dataclass
class TitleImageOverlay:
    title: str
    image: str
    paragraph: str | None = None
    text_color: str = ""

    def __str__(self):
        p = ""
        if self.paragraph:
            p = []
            for _p in self.paragraph.split("\n"):
                p.append(f'<p class="card-text">{_p}</p>')
            p = "".join(p)
        return f"""
        <div class="card bg-inverse" style="max-width: 600px;">
            {self.image}
            <div class="card-img-overlay p-0">
                <div class="bg-light p-2" style="--bs-bg-opacity:0.5;">
                    <h3 class="card-title" >{self.title}</h3>
                    {p}
                </div>
            </div>
        </div>"""
