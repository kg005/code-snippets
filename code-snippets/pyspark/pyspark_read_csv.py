customSchema = StructType([
  StructField("guid", StringType(), True),
])
csv = spark.read.csv('/user/martin.mesrsmid/guids_90days13_09_19_ordered2.csv/part-00000-0bab9825-8f14-4e7c-8670-0cb2cdd895a8-c000.csv',header=False, sep='\t',schema=customSchema)