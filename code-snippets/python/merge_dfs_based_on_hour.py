pd.set_option('display.float_format','{:04f}'.format)

df1 = dict_to_df(count_source_1_hourly,'count_'+source_1_name)
df2 = dict_to_df(count_source_2_hourly,'count_'+source_2_name)

df1['hour'] = df1['date'].apply(lambda x: x[3])
df2['hour'] = df2['date'].apply(lambda x: x[3])

df = df1.merge(df2,on='hour')[['hour','count_'+source_1_name, 'count_'+source_2_name]]

df['diff'] = df[f'count_{source_1_name}'] -  df[f'count_{source_2_name}']
df['diff%'] = df['diff'] / df[f'count_{source_2_name}'] * 100

df