def coefficient_of_variance(x):
    denom = np.mean(x)
    return np.inf if denom == 0 else np.std(x)/np.mean(x)