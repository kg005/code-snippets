# Within python, you can call the following to set the configuration:
sqlContext.setConf("spark.sql.parquet.binaryAsString", "true") 

# If using SQL notebooks, you can use the set key=value notation:
set spark.sql.parquet.binaryAsString=true