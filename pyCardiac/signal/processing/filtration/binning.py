import numpy as np
from ....routines import kernel_gaussian, add_borders

def binning(data, kernel_size = 3, kernel_name = 'uniform', mask = None):

    if (kernel_size % 2 != 1) or (kernel_size < 1):
        raise Exception("kernel_size must be odd positive integer but '{}' was given".format(kernel_size))
    
    if kernel_name == 'uniform':
            kernel = np.ones((kernel_size, kernel_size)) / kernel_size**2
    elif kernel_name == 'gaussian':
            sigma = kernel_size / (3. * 2)
            kernel = kernel_gaussian(kernel_size, sigma)
    else:
        raise Exception("kernel_name must be 'uniform' or 'gaussian' but '{}' was given".format(kernel_name))
    
    
    if mask is None:
        mask = np.ones_like(data[:, :, 0])

    data_binned = np.zeros(data.shape)

    kernel_size_half = kernel_size / 2
    N, M, T = data.shape
    
    for y in range(N):
        for x in range(M):

            if mask[y, x]:

                range_x = [x - kernel_size_half, x + kernel_size_half]
                range_y = [y - kernel_size_half, y + kernel_size_half]
                
                left_border_size = 0
                right_border_size = 0
                top_border_size = 0
                bottom_border_size = 0

                if range_x[0] < 0:
                    left_border_size = -range_x[0]
                if range_x[1] > M - 1:
                    right_border_size = range_x[1] - (M - 1)
                if range_y[0] < 0:
                    top_border_size = -range_y[0]
                if range_y[1] > N - 1:
                    bottom_border_size = range_y[1] - (N - 1)
                    
                mask_window = mask[range_y[0] + top_border_size : (range_y[1] + 1) - bottom_border_size,
                                   range_x[0] + left_border_size : (range_x[1] + 1) - right_border_size]
                
                mask_window = add_borders(mask_window,
                                                  left_border_size,
                                                  right_border_size,
                                                  top_border_size,
                                                  bottom_border_size)           

                kernel_current = kernel * mask_window
                kernel_current = kernel_current[top_border_size : kernel_size - bottom_border_size,
                                                left_border_size : kernel_size - right_border_size]  
                
                data_windows = data[range_y[0] + top_border_size : (range_y[1] + 1) - bottom_border_size,
                                   range_x[0] + left_border_size : (range_x[1] + 1) - right_border_size,
                                   :]

                temp = np.rollaxis(data_windows, 2) * kernel_current
                data_binned[y, x, :] = np.sum(temp, axis = (1, 2))           

    return data_binned