import numpy as np

def kernel_gaussian(kernel_size, sigma):

    kernel = np.zeros((kernel_size, kernel_size))

    i_center = kernel_size / 2
    j_center = i_center

    i_center_int = kernel_size / 2
    j_center_int = kernel_size / 2

    for i in range(i_center_int, kernel_size):
        for j in range(j_center_int, kernel_size):
            
            r = np.array([i - i_center, j - j_center])
            r_norm = np.linalg.norm(r)
            
            kernel_element = np.exp(-r_norm**2 / (2. * sigma**2))
            
            kernel[i, j] = kernel_element
            kernel[(kernel_size - 1) - i, j] = kernel_element
            kernel[i, (kernel_size - 1) - j] = kernel_element
            kernel[(kernel_size - 1) - i, (kernel_size - 1) - j] = kernel_element

    kernel = kernel / kernel.sum()
    
    return kernel