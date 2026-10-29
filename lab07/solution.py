import numpy as np
matrix = (np.array
        ([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]))

rows = [0, 2]
columns = [1, 2]
def reshape_rows(values, width):
    newarr = np.asarray(values)
    
    if len(values) % width != 0:
        return np.empty((0, width))

    return newarr.reshape(-1, width)

 def block(matrix, rows, columns):
     matrixx = np.asarray(matrix)
     return matrixx[np.ix_(rows, columns)]

# def column_means(matrix):
#     pass
#
# def column_range(matrix, column):
#     pass

print(matrix[np.ix_(rows, columns)])