from typing import Literal

import numpy as np
import pandas as pd
from csrs import schemas
from plotly import graph_objects as go

from ._line import line
from .conversions import cfs_to_taf


def exceedance(
    timeseries: dict[str, schemas.Timeseries],
    y_label: str = "y",
    conversion: Literal["cfs_to_taf"] | None = None,
    **layout_kwargs,
) -> go.Figure:
    all_series = dict()
    for k, ts in timeseries.items():
        df = ts.to_frame()
        if conversion == "cfs_to_taf":
            df = cfs_to_taf(df)
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


def annual_exceedance(
    timeseries: dict[str, schemas.Timeseries],
    y_label: str = "y",
    conversion: Literal["cfs_to_taf"] | None = None,
    **layout_kwargs,
) -> go.Figure:
    all_series = dict()
    for k, ts in timeseries.items():
        df = ts.to_frame()
        if conversion == "cfs_to_taf":
            df = cfs_to_taf(df)
        df = df.groupby(df.index.year).sum()
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
