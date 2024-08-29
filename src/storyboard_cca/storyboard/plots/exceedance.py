import numpy as np
import pandas as pd
from csrs import schemas
from plotly import graph_objects as go

from .line import line


def exceedance(
    timeseries: dict[str, schemas.Timeseries],
    y_label: str = "y",
    **layout_kwargs,
) -> go.Figure:
    all_series = dict()
    for k, ts in timeseries.items():
        df = ts.to_frame()
        sorted = df.iloc[:, 0].sort_values().values
        exceedance = (np.arange(1.0, len(sorted) + 1.0) / len(sorted)) * 100.0
        series = pd.Series(sorted, index=exceedance)
        all_series[k] = series
    return line(
        series=all_series,
        y_label=y_label,
        x_label="Non-Exceedance Probability (%)",
        **layout_kwargs,
    )
