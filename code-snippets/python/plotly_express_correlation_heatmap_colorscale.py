import plotly.express as px

fig = px.imshow(
    corr,
    color_continuous_scale=px.colors.diverging.RdBu,
    zmax=1,
    zmin=-1,
    width=1200,
    height=1200,
)
fig.show()