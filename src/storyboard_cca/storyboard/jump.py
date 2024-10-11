import dash


class Jump(dash.dcc.Link):
    def __init__(self, text: str, href: str, same_page: bool = False, **kwargs):
        super().__init__(
            [
                text,
                dash.dcc.Store(id="scroll-to-hash"),
            ],
            href=href,
            className="btn btn-primary m-1",
            refresh=not same_page,
            **kwargs,
        )


class SelfJump(dash.html.A):
    def __init__(self, *args, **kwargs):
        uuid = kwargs.pop("id", id(object()))  # Make a unique id if not given
        kwargs = dict(href=f"#{uuid}", id=str(uuid)) | kwargs
        super().__init__(*args, **kwargs)
