import matplotlib.pyplot as plt

# First calculation of the statistics

# columns you need the stats for
cols = ['t1','t2'] 

# .describe() helps you with max, min, mean
stats_desc = spark_df.select(*cols).describe().toPandas().astype(float).set_index('summary') 

# for med, q1,q3 use .approxQuantile(cols_you_need, [list of quartiles to be calculated], error_you_allow)
stats_aq = spark_df.approxQuantile(cols,[0.25,0.5,0.75],0.05) 

# Then create a list of dicts with stats
stats_to_plot = []
for i,c in enumerate(cols):

    stats_to_plot.append({
        "label": c,                             # not required - name on x axis
        "mean":  stats_desc.loc['mean',c],      # not required - unless you set showmeans=True
        "q1": stats_aq[i][0],                   # required
        "med": stats_aq[i][1],                  # required
        "q3": stats_aq[i][2],                   # required
        # "cilo": --                            # not required - Lower and upper confidence intervals about the median. Needed if shownotches=True
        # "cihi": --                            # not required
        "whislo": stats_desc.loc['min',c],      # required - lower whiskers - use min if you do not want fliers
        "whishi": stats_desc.loc['max',c],      # required - upper whiskers - use max if you do not want fliers
        "fliers": []                            # (not) required - used for fliers (outliers which you want to plot separately)
        })

# And plotting the boxplot from custom calculated stats
fig, axes = plt.subplots(nrows=1, ncols=1, sharey=True)
axes.bxp(stats)
axes.set_title('Boxplot for precalculated statistics')
plt.show()