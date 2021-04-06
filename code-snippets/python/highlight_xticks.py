for i in df[df.perc_diff > 0].index:
    ax.get_xticklabels()[i].set_backgroundcolor("navajowhite")
