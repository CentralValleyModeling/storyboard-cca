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
        super().__init__(children, **kwargs)


class Accordion(dbc.Accordion):
    def __init__(self, /, *sections: list[tuple[Any, dict]], **kwargs):
        sections = [dbc.AccordionItem(a, **k) for a, k in sections]
        super().__init__(sections, **kwargs)
