import numpy as np


def make_hours() -> list[int]:
    return np.arange(0, 22, 3).tolist()


def vector_report(values: list[float]) -> dict:
    third = values[2]
    last = values[-1]
    cut = values[2:6]
    second = values[::2]
    reverse = values[::-1]
    return {'third': third,'last': last, 'cut': cut, 'second': second, 'reverse': reverse}

