queue = 'root.dev.backend'
driver_mem = '4g'
mem_overhead = '8g'
max_executors = '500'
app_name = f"KG_{ticket_id}_v{str(version).zfill(2)}"

spark = dart.get_spark(app_name,queue,driver_mem,mem_overhead,max_executors)

spark