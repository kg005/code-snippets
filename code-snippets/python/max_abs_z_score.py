def max_abs_z_score(x):
    denom = np.std(x)
    return 0 if denom == 0 else max(abs((x-np.mean(x))/np.std(x)))