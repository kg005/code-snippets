# from https://stackoverflow.com/questions/24826368/summing-over-a-multiindex-level-in-a-pandas-series

data.groupby([a,b,c]).sum(level=[0,1])


