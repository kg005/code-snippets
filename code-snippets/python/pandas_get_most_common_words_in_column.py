# Get  N most common words in a column with strings

pd.Series(' '.join(df["string_col_name"]).lower().split()).value_counts()[:N]

