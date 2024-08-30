from collections import defaultdict

import plotly.express as px

COLOR_SCHEME_QUALITATIVE = px.colors.qualitative.Set1


def next_color() -> str:
    c = COLOR_SCHEME_QUALITATIVE.pop(0)
    COLOR_SCHEME_QUALITATIVE.append(c)
    return c


ASSIGNED_COLORS = defaultdict(next_color)


def assign_colors_for_runs(keys: list[str]):
    for k in keys:
        _ = ASSIGNED_COLORS[k]
