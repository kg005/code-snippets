# data
#                                                                    tags_str  count_reference  count_boosted    diff  diff_abs  ratio
# 0                                      REFERER_TO_SEARCH & PRERENDER & SERP                0              1       1         1   0.00
# 1                                                          PRERENDER & SERP               23         102010  101987    101987   0.00
# 2                            LOCATION_FROM_LAST_REDIRECT & PRERENDER & SERP             1827           2665     838       838   0.69
# 3                      PING_TO_FROM_LAST_REDIRECT & EXTRACTED_FROM_REDIRECT            22401          26320    3919      3919   0.85
# 4                                                  REFERER_TO_SEARCH & SERP              205            233      28        28   0.88
# 5             REFERER_TO_LAST_REDIRECT & LOCATION_FROM_LAST_REDIRECT & SERP               58             52      -6         6   1.12
# 6     PARAM_FROM_LAST_REDIRECT & EXTRACTED_FROM_REDIRECT & PRERENDER & SERP             6527           2623   -3904      3904   2.49
# 7   PING_TO_FROM_LAST_REDIRECT & EXTRACTED_FROM_REDIRECT & PRERENDER & SERP            66585          20075  -46510     46510   3.32
# 8  LOCATION_FROM_LAST_REDIRECT & EXTRACTED_FROM_REDIRECT & PRERENDER & SERP              502             80    -422       422   6.28



fig, axes = plt.subplots(ncols=2, sharey=True)

ax = (
    df_enhanced_2.set_index("tags_str")[["count_reference", "count_boosted"]]
    .plot.barh(color=["b", "g"],ax=axes[0])
)
ax.set_ylabel("Tags Combination")
ax.set_xlabel("Count")

ax2 = (
    df_enhanced_2
    .rename(columns={"ratio": "ratio - cnt_ref/cnt_boost"})
    .plot.barh(
        x="tags_str", y="ratio - cnt_ref/cnt_boost", color="r",ax=axes[1],width=0.3
    )
)

ax2.set_xlabel("ratio - cnt_ref/cnt_boost")

for i in df_enhanced_2[abs(df_enhanced_2.ratio - 1)>ratio_highlight_limit].index:
    ax.get_yticklabels()[i].set_backgroundcolor("lightcoral")

axes[0].invert_xaxis()


ax.set_title('Count of tag combinations within datasamples')
ax2.set_title(f'Ratio between counts (Highlighted if < {1-ratio_highlight_limit} or > {1+ratio_highlight_limit})');


# plt.savefig('Comarison of distinct tag combinations cnts and ratios - Only Highlighted.png')