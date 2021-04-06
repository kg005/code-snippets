df = df.withColumn('localTimestamp',
                   expr("from_utc_timestamp(utcTimestamp, timezone)"))