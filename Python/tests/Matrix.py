import numpy as np
A = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [5, 3, 1]
])
B = np.array([
    [3, 5, 6],
    [7, 8, 1],
    [1, 7, 8]
])
print(A * B)
print(A @ B)
print(A / B)
C = np.matrix([
    [1, 2, 3],
    [2, 3, 4],
    [5, 3, 1]
])
D = np.matrix([
    [3, 5, 6],
    [7, 8, 1],
    [1, 7, 8]
])
print(C * D)
print(C / D)

# ATTENTION 不要使用np.matrix，使用np.array!
