import plotly.express as px

COLOR_SCHEME_QUALITATIVE = px.colors.qualitative.Set1

ASSIGNED_COLORS = dict()


def assign_colors_for_runs(keys: list[str]):
    for k in keys:
        get_color_for(k)


def get_color_for(key: str) -> str:
    if key in ASSIGNED_COLORS:
        return ASSIGNED_COLORS[key]
    else:
        i = len(ASSIGNED_COLORS) % len(COLOR_SCHEME_QUALITATIVE)
        ASSIGNED_COLORS[key] = COLOR_SCHEME_QUALITATIVE[i]
