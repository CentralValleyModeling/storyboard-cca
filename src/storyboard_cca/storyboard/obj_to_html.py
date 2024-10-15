from typing import Any, Iterable

from dash import html


def obj_to_div(obj: dict[str, Any] | Iterable[tuple[str, Any]]) -> html.Div:
    children = list()
    if isinstance(obj, dict):
        object_iterator = obj.items()
    else:
        object_iterator = obj
    for k, v in object_iterator:
        if isinstance(v, dict):
            v = obj_to_div(v)
        children.append(html.Div(id=str(k), children=v))

    return html.Div(
        id=f"{type(obj).__name__}-{id(obj)}",
        children=children,
        style={"display": "none"},
    )
