import json
import requests
import pyspark.sql.functions as f
from pyspark.sql.types import StringType
urlEventTypes = 'https://vertical-manager.int.jumpshot.com/api/eventtypes'
eventTypeMap = {x['id']: x['title'] for x in json.loads(requests.get(urlEventTypes).text)}
def eventTypeName(eventId):
    return eventTypeMap.get(eventId).lower().replace(' ','_')
eventTypeNameUdf = f.udf(eventTypeName, StringType())
df_old_all = df_old_all.withColumn('match_event_type', eventTypeNameUdf(f.col("match.event.type")))