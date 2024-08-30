import pandas as pd


def cfs_to_taf(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()  # Don't mess with the original data
    dates: pd.DatetimeIndex = df.index
    days = dates.days_in_month
    seconds = days * 24 * 60 * 60
    for c in df.columns:
        df.loc[:, c] = (df.loc[:, c] * seconds) / 43_560_000
    return df
