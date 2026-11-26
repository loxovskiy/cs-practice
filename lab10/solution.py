import numpy as np

def make_table(rows: int, columns: int) :
    mat = np.arange(rows * columns).reshape(rows, columns)
    return mat.tolist()