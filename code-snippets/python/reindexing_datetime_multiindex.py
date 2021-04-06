# reindexing_datetime_multiindex.py

# https://stackoverflow.com/a/54905095

dates = pd.date_range(loaded_ouput[datetime_col].min(), loaded_ouput[datetime_col].max())
    mux = pd.MultiIndex.from_product([grouped_out.index.levels[0], dates], names=grouped_out.index.names)

    grouped_out = grouped_out.reindex(index=mux, fill_value=set())
