# Save df to png file
import dataframe_image as dfi
import pandas as pd

def to_png(df: pd.DataFrame, file_name,n=100, perc=True,decimals=2,use_gradient=False):
    format_str = "{:." + str(decimals) + ("%" if perc else "f") + "}"
    pd.options.display.float_format = format_str.format
    pd.options.display.max_rows = n
    dfi.export(df, file_name)
    display(
        df
        if not use_gradient
        else df.style.format(format_str.format).background_gradient(axis=None)
    )
    pd.options.display.max_rows = 15
    pd.options.display.float_format = "{:.4f}".format
