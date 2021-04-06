# +---+-----+------+----+------------+------------+
# | ID|  ID2|Number|Name|Opening_Hour|Closing_Hour|
# +---+-----+------+----+------------+------------+
# |ALT|  QWA|     6|null|    08:59:00|    23:30:00|
# |ALT|AUTRE|     2|null|    08:58:00|    23:29:00|
# |TDR|  QWA|     3|null|    08:57:00|    23:28:00|
# |ALT| TEST|     4|null|    08:56:00|    23:27:00|
# |ALT|  QWA|     6|null|    08:55:00|    23:26:00|
# |ALT|  QWA|     2|null|    08:54:00|    23:25:00|
# |ALT|  QWA|     2|null|    08:53:00|    23:24:00|
# +---+-----+------+----+------------+------------+
w = Window.partitionBy('ID', 'ID2', 'Number')
w2 = Window.partitionBy('ID', 'ID2', 'Number').orderBy('ID', 'ID2', 'Number')
df.select(
        '*',
        f.count('ID').over(w).alias('dupeCount'),
        f.row_number().over(w2).alias('rowNum')
    )\
    .where('(dupeCount > 1) AND (rowNum = 1)')\
    .drop('dupeCount', 'rowNum')\
    .show()

#+---+---+------+----+------------+------------+
#| ID|ID2|Number|Name|Opening_Hour|Closing_Hour|
#+---+---+------+----+------------+------------+
#|ALT|QWA|     2|null|    08:54:00|    23:25:00|
#|ALT|QWA|     6|null|    08:59:00|    23:30:00|
#+---+---+------+----+------------+------------+