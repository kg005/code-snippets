from pyspark.sql import HiveContext
from pyspark.context import SparkContext
from pyspark.conf import SparkConf

conf = SparkConf()
conf.set('spark.app.name', 'APP_NAME_PLACEHOLDER')

sc = SparkContext(conf = conf)
sqlc = HiveContext(sc)

df = (sqlc.read
    .option("inferSchema", "true")
    .option("delimiter", "\t")
    .option("quote", "\u0000")  # magic is happening here to prevent misinterpretation of quoutes
                                # see https://github.com/databricks/spark-csv/issues/89
    .csv("/data/searches-dev/moz-kw2/out/2017/12/*/") # change this 
    .toDF("guid_hash", "age_group", "keyword", 
          "landingpage", "platform", "gender", "timestamp", "landingdomain", 
          "clicktype", "countrycode", "state")  # change those as well
 )
 
 df.registerTempTable('tmp_moz')
 
 sqlc.sql('select * from tmp_moz limit 10').toPandas()  # query the data however you like in SQL
