import dash
import dash_bootstrap_components as dbc


class GridContainer(dbc.Container):
    def __init__(self, /, *children, **kwargs):
        children = list(children)
        for i, child in enumerate(children):
            if isinstance(child, (list, tuple, set)):
                children[i] = dash.html.Div(child)
        if not any(isinstance(child, dbc.Row) for child in children):
            children = dbc.Row(children)
        super().__init__(children, **kwargs)
