import pandas as pd


def display_long(df: pd.DataFrame):
    """
    Temporary allows displaying up to 1000 rows and displays given Dataframe
    """
    pd.options.display.max_rows = 1000
    display(df)
    pd.options.display.max_rows = 15