import numpy as np
from ..signal.analysis import calculate_APD

def calculate_APD_map(data, t_start, t_end, percentage = 80.):
    time = np.arange(t_start, t_end)
    apd_map = np.apply_along_axis(lambda x: calculate_APD(time, x[t_start: t_end], percentage = 80.), -1, data)
    return apd_map