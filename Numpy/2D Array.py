import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])

doubled = matrix * 2
print(doubled)

print(matrix.shape)
print(matrix.ndim)

row_sum = np.sum(matrix, axis=1)
print(row_sum)