from typing import Any

import dash
import dash_bootstrap_components as dbc


class PaddedSection(dbc.Container):
    def __init__(self, /, *children, **kwargs):
        children = list(children)
        for i, child in enumerate(children):
            if isinstance(child, (list, tuple, set)):
                children[i] = dash.html.Div(child)
        if not any(isinstance(child, dbc.Row) for child in children):
            children = dbc.Row(children)
        kw = dict(fluid=True)
        if ("class_name" not in kwargs) and ("className" not in kwargs):
            kw["class_name"] = "px-4 mx-0"

        kwargs = kw | kwargs
        super().__init__(children, **kwargs)


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
