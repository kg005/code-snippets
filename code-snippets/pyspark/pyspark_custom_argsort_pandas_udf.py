@pandas_udf("string", PandasUDFType.SCALAR)
def get_order_pandas_udf(series):
    def argsort_custom(ls):
        return sorted(range(len(ls)), key=ls.__getitem__)

    def str_order(timestamps_list):
        return "".join([str(idx) for idx in argsort_custom(timestamps_list)])

    return series.apply(lambda x: str_order(x) if x is not None else None)