import plotly.graph_objects as go

fig = go.Figure()
data = ech_gb_rc_floored["count"]
fig.add_trace(go.Pie(labels=data.index, values=data.values, name=data.index.name))

fig.update_traces(
    textinfo="percent+label",
#     hole=0.4,
    hoverinfo="label+percent+value",
    textposition="inside",
)

fig.update_layout(
    title_text="Response codes distribution among all echidna clicks"
)
fig.show()