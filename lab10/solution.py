import numpy as np

def make_table(rows: int, columns: int) :
    mat = np.arange(rows * columns).reshape(rows, columns)
    return mat.tolist()

def rectangle(matrix: list[list[float]], row_start: int, row_stop: int, column_start: int, column_stop: int) -> list[list[float]]:
    arr = np.asarray(matrix)
    return arr[row_start:row_stop, column_start:column_stop].tolist()

def replace_rectangle(matrix: list[list[float]], row_start: int, row_stop: int, column_start: int, column_stop: int, value: float) -> list[list[float]]:
    mat = np.asarray(matrix, dtype=float).copy()
    mat[row_start:row_stop, column_start:column_stop] = value
    return mat.tolist()

def matrix_vector_product(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return (np.asanyarray(matrix) @ np.asarray(vector)).tolist()

def matrix_multiply(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    A = np.asarray(left)
    B = np.asarray(right)
    return (A @ B).tolist()

def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    return (np.asarray(matrix).T).tolist()

def solve_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    A = np.asarray(matrix)
    b = np.asarray(vector)
    x = np.linalg.solve(A, b)
    return np.round(x, 6).tolist()

def tensor_channel_mean(tensor: list) -> list:
    arr = np.asarray(tensor)
    return arr.mean(axis=-1).tolist()

def point_distance(first: list[float],second: list[float]) -> float:
    a = np.asarray(first, dtype=float)
    b = np.asarray(second, dtype=float)
    distance = np.linalg.norm(a - b)
    return round(float(distance), 6)
