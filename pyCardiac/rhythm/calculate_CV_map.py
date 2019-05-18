import numpy as np
from . import calculate_activation_map


def calculate_CV_map(data, t_start, t_end, percentage = 90., dx = 1., dy = 1.):
    act_map = calculate_activation_map(data, t_start, t_end, percentage)
    CV_map = np.gradient(act_map, dx, dy)
    return CV_map