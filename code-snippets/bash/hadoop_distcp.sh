

hadoop distcp -Dmapred.job.queue.name=root.interactive "hdfs://hadoop-namenode-prod-prg-001.s.jumpshot.com:8020/prod/urlinfo/clickstream/raw/v2/year=2018/month=8/day=30/hour=16" /user/gavenciak/data_from_prc/month=8/day=30/hour=16

# new
hadoop distcp -Dmapred.job.queue.name=root.dev.backend -skipcrccheck -update hdfs://hadoop-namenode-prod-prg-002.s.jumpshot.com{SOURCE_PATH} {TARGET_PATH}