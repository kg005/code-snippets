# get configuration for spark context
spark.sparkContext._conf.getAll()

# update configuration of running spark context
conf = spark.sparkContext._conf.setAll([('spark.sql.parquet.binaryAsString',True)])
