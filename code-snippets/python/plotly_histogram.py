    fig = px.histogram(
        df,
        x="weight",
        color="data_type",
        title=f"Comparison of weighings for {ct}",
        labels={
            "data_type": "Fan Status",
            "weight": "Measured Weight",
            "count": "Count of Weighings",
        },
        barmode="overlay",
        marginal="box",
        hover_data=df.columns,
    )
