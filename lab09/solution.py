import numpy as np


def make_hours() -> list[int]:
    return np.arange(0, 22, 3).tolist()

values = make_hours()

def vector_report(values: list[float]) -> dict:
    third = values[2]
    last = values[-1]
    cut = values[2:6]
    second = values[::2]
    reverse = values[::-1]
    return {'third': third,'last': last, 'cut': cut, 'second': second, 'reverse': reverse}

def change_vector(values: list[float]) -> list[float]:
    copy_values = values.copy()
    for i in range(2, 4):
        copy_values[i] = 99
    for i in range(1, len(values), 2):
        copy_values[i] = -1
    return copy_values



