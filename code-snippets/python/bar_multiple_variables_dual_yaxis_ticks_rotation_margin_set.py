ax = (
    df_enhanced_2.set_index("tags_str")
    .sort_values("ratio", ascending=False)[["count_reference", "count_boosted"]]
    .plot.bar(color=["b", "g"])
)
ax.set_ylabel("count")
ax2 = (
    df_enhanced_2.sort_values("ratio", ascending=False)
    .rename(columns={"ratio": "ratio - cnt_ref/cnt_boost"})
    .plot(
        x="tags_str", y="ratio - cnt_ref/cnt_boost", secondary_y=True, ax=ax, style="ro"
    )
)
ax2.set_xlabel("tags_combination")
ax2.set_ylabel("ratio - cnt_ref/cnt_boost")
for tick in ax.get_xticklabels():
    tick.set_rotation(90)
    
for tick in ax.get_yticklabels():
    tick.set_rotation(90)
    
for tick in ax2.get_yticklabels():
    tick.set_rotation(90)


plt.xlim(-0.5, len(df_enhanced_2) + 0.5);
