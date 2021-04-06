from copy import deepcopy

histogram_dict_normalized = deepcopy(histogram_dict)

cnt_source_1 = 11534219
cnt_source_2 = 3401513

for k,df in histogram_dict_normalized.items():
    df[f'count_{source_1_name}'] = df[f'count_{source_1_name}'] / cnt_source_1
    df[f'count_{source_2_name}'] = df[f'count_{source_2_name}'] / cnt_source_2
    df = df.rename(columns={f'count_{source_1_name}':f'count_{source_1_name}_%',
                            f'count_{source_2_name}':f'count_{source_2_name}_%'
                           })
#     display(df.head())
    histogram_dict_normalized[k] = df
    

hdne = dart.enhance_hist_dict(histogram_dict_normalized,suffixes=[f'_{source_2_name}_%',f'_{source_1_name}_%'])