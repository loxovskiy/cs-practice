import numpy as np

def reshape_rows(values, width):
    newarr = np.asarray(values)
    
    if len(values) % width != 0 or width <= 0:
        return []

    return newarr.reshape(-1, width).tolist()

def block(matrix, rows, columns):
     matrixx = np.asarray(matrix)
     return matrixx[np.ix_(rows, columns)].tolist()

def column_means(matrix):
     if not matrix:
         return []
     array = np.asarray(matrix)

     return np.round(np.mean(array, axis = 0), 6).tolist()

def column_range(matrix, column):
    if not matrix:
        return []
    array = np.asarray(matrix)
    values = array[:, column]
    return float(np.round(values.max() - values.min(), 6))

