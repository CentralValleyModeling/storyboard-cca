from typing import Any

import dash_bootstrap_components as dbc


class Accordion(dbc.Accordion):
    def __init__(self, /, *sections: list[tuple[Any, dict]], **kwargs):
        sections = [dbc.AccordionItem(a, **k) for a, k in sections]
        super().__init__(sections, **kwargs)


class SimpleCard(dbc.Card):
    def __init__(
        self,
        header: Any = None,
        body: Any = None,
        footer: Any = None,
        **kwargs,
    ):
        children = list()
        if header:
            kw = kwargs.pop("header", dict())
            children.append(dbc.CardHeader(header), **kw)
        if body:
            kw = kwargs.pop("body", dict())
            children.append(dbc.CardBody(body), **kw)
        if footer:
            kw = kwargs.pop("footer", dict())
            children.append(dbc.CardFooter(footer), **kw)
        super().__init__(children=children, **kwargs)
