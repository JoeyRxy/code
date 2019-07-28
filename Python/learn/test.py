import numpy as np
A = np.matrix([
    [2, 4, 6, 8],
    [1, 3, 5, 7]
])
B = A.tolist()
s = 0
for t in B:
    for x in t:
        s += x

print(s)
