
# pandas pyspark udf to select first

from pyspark.sql.functions import pandas_udf, PandasUDFType

w = Window.partitionBy('session.browse.id','session.domain.id','url.domain').orderBy('timestamp')

cs_gb_g_dsess_urld = (
    df_cs_sample.groupby(
        "guid",
        col("session.browse.id").alias("browse_id"),
        col("session.domain.id").alias("domain_id"),
        col("url.domain").alias("url_domain"),
    )
    .agg(
        su_udf("domainsessionreferrer.domain").alias('domain'),
    )
    .groupby('domain')
    .count()
    .toPandas()
)