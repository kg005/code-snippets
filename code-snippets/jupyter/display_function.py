def disp(
    df: pd.DataFrame, /, *, perc=False, decimals=2, n=1000,
):
    """
    Temporary allows displaying up to n rows in given flaot format
    """
    format_str = "{:." + str(decimals) + ("%" if perc else "f") + "}"
    pd.options.display.float_format = format_str.format
    pd.options.display.max_rows = n
    display(df)
    pd.options.display.max_rows = 15
    pd.options.display.float_format = "{:.4f}".format
