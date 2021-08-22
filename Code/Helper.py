def get_median_from_mean_iqr(data):
    return get_median(get_mean_with_iqr(data))


def get_mean_with_iqr(data):
    if len(data) > 0:
        import numpy as np
        Q1 = np.quantile(data,0.25)
        Q3 = np.quantile(data,0.75)
        IQR = Q3 - Q1
        # Any value below Q1-1.5*IQR or above Q3+1.5*IQR is an Outlier
        lower_bound = Q1 - (1.5 * IQR)
        upper_bound = Q3 + (1.5 * IQR)
        filtered_data = []
        for x in data:
            if ((x >= lower_bound) and (x <= upper_bound)):
                filtered_data.append(x)
        if len(filtered_data) == 0:
            return [-999]
        else:
            return filtered_data
    else:
        return [-999]


def get_median(data):
    import statistics
    return float(statistics.median(data))


def get_working_directory():
    from pathlib import Path
    return Path.cwd() 