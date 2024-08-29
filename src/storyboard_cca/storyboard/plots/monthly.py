import pandas as pd
from csrs import schemas
from plotly import graph_objects as go

from .line import line


def monthly(
    timeseries: dict[str, schemas.Timeseries],
    y_label: str = "Value",
    **layout_kwargs,
) -> go.Figure:
    all_series = dict()
    month_key = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec",
    }
    for k, ts in timeseries.items():
        df = ts.to_frame()
        months: pd.Series = df.index.month
        df = df.groupby(months).agg("mean")
        df.index = [month_key[i] for i in df.index]
        all_series[k] = df.iloc[:, 0]
    return line(
        series=all_series,
        y_label=y_label,
        **layout_kwargs,
    )
