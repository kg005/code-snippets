from pyspark.sql.types import StringType,ArrayType

def get_all_keys(customKeyValues):
    return list(set([kv_pair[0] for kv_pair in customKeyValues]))

gak_udf = F.udf(get_all_keys,ArrayType(StringType()))

df_all_ckv_keys = all_ckv_keys.toPandas()

#                    ckv_key
# 0                ajaxLogic
# 1                 api_port
# 2            api_timestamp
# 3                className
# 4               duplicated
# 5                    event
# 6        gss_global_female
# 7          gss_global_male
# 8         gss_local_female
# 9           gss_local_male
# 10                    host
# 11  initiating_user_action
# 12    iuaPossibleOverwrite
# 13                  method
# 14                 request
# 15       served_from_cache
# 16               throttled
# 17                   title
# 18         webshieldStatus