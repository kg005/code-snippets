cm = plt.cm.get_cmap('rainbow')

n, bins, patches = plt.hist(missing_in_boost_window_w_dt.ttl_diff_sec,bins=120);

bin_centers = 0.5 * (bins[:-1] + bins[1:])
# scale values to interval [0,1]
col = bin_centers - min(bin_centers)
col /= max(col)
for c, p in zip(col, patches):
    plt.setp(p, 'facecolor', cm(c))