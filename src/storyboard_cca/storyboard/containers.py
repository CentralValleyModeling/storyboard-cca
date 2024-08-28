import dash_bootstrap_components as dbc


class Container(dbc.Container):
    def __init__(self, /, *children, **kwargs):
        if isinstance(children, (list, tuple, set)):
            if any(isinstance(child, dbc.Row) for child in children):
                holder = dbc.Col
            else:
                holder = dbc.Row
            children = holder(children)
        super().__init__(children, **kwargs)
