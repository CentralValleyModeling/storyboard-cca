import dash


class JumpLink(dash.dcc.Link):
    def __init__(self, text: str, href: str, same_page: bool = False, **kwargs):
        super().__init__(
            [
                text,
                dash.dcc.Store(id="scroll-to-hash"),
            ],
            href=href,
            className="btn btn-primary",
            refresh=not same_page,
            **kwargs,
        )
