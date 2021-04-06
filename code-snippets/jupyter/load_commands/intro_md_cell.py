import data_reconciliation_toolkit as dart

ticket_id = "XXX-XXX"
title = "NTBTITLE"
version = 1
version_desc = ""
cluster = "PRG/BRQ"
data_paths = {
    "data_src_name": "path",
    "data_src_name2": "path2",
}
task_desc = """-"""

dart.intro_md(title, ticket_id, version, version_desc, cluster, task_desc, data_paths)
