w = Window.partitionBy("guid").orderBy("cts")
beta_data = beta_data.withColumn(
    "av_version_changed",
    (beta_data.browser.av_version != f.lag("browser.av_version", 1, 0).over(w)).cast(
        "int"
    ),
)