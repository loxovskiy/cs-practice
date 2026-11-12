import numpy as np

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1, dtype=int)
identity = np.eye(3, 3, 0, dtype=int)
print(hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

print(hours[2])
print(hours[-1])
print(hours[1:5])
print(hours[0::2])
print(hours[::-1])

