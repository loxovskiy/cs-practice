import numpy as np

def make_table(rows: int, columns: int) :
    mat = np.arange(rows * columns).reshape(rows, columns)
    return mat.tolist()

def rectangle(matrix: list[list[float]], row_start: int, row_stop: int, column_start: int, column_stop: int) -> list[list[float]]:
    mat = np.asarray(matrix)
    return arr[row_start:row_stop, column_start:column_stop].tolist()

def replace_rectangle(matrix: list[list[float]], row_start: int, row_stop: int, column_start: int, column_stop: int, value: float) -> list[list[float]]:
    mat = np.asarray(matrix, dtype=float).copy()
    mat[row_start:row_stop, column_start:column_stop] = value
    return mat.tolist()

def matrix_vector_product(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return (np.asanyarray(matrix) @ np.asarray(vector)).tolist()