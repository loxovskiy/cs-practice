import numpy as np


def make_hours() -> list[int]:
    return np.arange(0, 22, 3).tolist()

values = make_hours()

def vector_report(values: list[float]) -> dict:
    arr = np.array(values, dtype = float)
    third = arr[2]
    last = arr[-1]
    middle = arr[2:6].tolist()
    every_second = arr[::2].tolist()
    reversed = arr[::-1].tolist()
    return {'third': third,'last': last, 'middle': middle, 'every_second': every_second, 'reversed': reversed}

def change_vector(values: list[float]) -> list[float]:
    copy_values = values.copy()
    for i in range(2, 4):
        copy_values[i] = 99
    for i in range(0, len(values), 2):
        copy_values[i] = -1
    return copy_values

def cap_above(values: list[float], limit: float) -> list[float]:
    copy_values = np.array(values, copy = True)
    mask = copy_values > limit
    copy_values[mask] = limit
    return copy_values.tolist()

def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    copy_values = np.array(values, copy=True)
    for i in range(len(copy_values)):
        copy_values[i] = copy_values[i] * 9 / 5 + 32
    return copy_values.tolist()



