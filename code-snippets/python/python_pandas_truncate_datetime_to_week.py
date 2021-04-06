# we truncate the date to Year Week number and 1 (for monday) and then convert it back into datetime 
loaded_orders['shipped_at_week'] = pd.to_datetime(loaded_orders['shipped_at'].dt.strftime('%Y-%U-1'),  format="%Y-%W-%w")
