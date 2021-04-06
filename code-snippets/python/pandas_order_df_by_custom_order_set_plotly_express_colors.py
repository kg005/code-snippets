# https://stackoverflow.com/a/59718809

# imports
import pandas as pd
import plotly.express as px

# data
df = px.data.iris()

# function to subset and order a pandas
# dataframe fo a long format
def order_df(df_input, order_by, order):
    df_output=pd.DataFrame()
    for var in order:    
        df_append=df_input[df_input[order_by]==var].copy()
        df_output = pd.concat([df_output, df_append])
    return(df_output)

# data subsets
df_express = order_df(df_input = df, order_by='species', order=['virginica'])
df_express = order_df(df_input = df, order_by='species', order=['virginica', 'setosa'])
df_express = order_df(df_input = df, order_by='species', order=['virginica', 'setosa', 'versicolor'])

# plotly
fig = px.scatter(df_express, x="sepal_width", y="sepal_length", color="species")
fig.show()

# or set distinct colorscale i.e.:
px.line(data.reset_index(), y=y_col_names, x=x_colname, title=title, color_discrete_sequence=color_seq)
