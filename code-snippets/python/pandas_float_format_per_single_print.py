df.head().style.format("{:,.0f}") (for all columns)

df.head().style.format({"total_sales_column": "{:,.0f}", "perc_column": "{:.2%}"}) (per column)
