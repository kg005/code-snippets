# pd_dataframe_highlite_gradient

import seaborn as sns

cm = sns.light_palette("green", as_cmap=True)
nan_table.style.background_gradient(cmap=cm)