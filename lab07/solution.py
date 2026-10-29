import numpy as np

def reshape_rows(values, width):
    newarr = np.asarray(values)
    
    if len(values) % width != 0:
        return np.empty((0, width))

    return newarr.reshape(-1, width)

def block(matrix, rows, columns):
    pass

def column_means(matrix):
    pass

def column_range(matrix, column):
    pass