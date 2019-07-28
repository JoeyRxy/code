from scipy import signal
from scipy import ndimage
import numpy as np
from scipy.special import comb
# x = 1 / 6 * np.array([
#     [-1, -1, -1],
#     [0, 0, 0],
#     [-1, -1, -1]
# ])
# y = x.transpose()
# I = 1 / 9

# img = np.array([
#     [3, 6, 9],
#     [2, 5, 7],
#     [2, 4, 7]
# ])
# alpha = ndimage.convolve(img, x)
# print(alpha)
# beta = ndimage.convolve(img, y)
# print(beta)

a = [i ** 2 * comb(9, i) for i in range(10)]
print(a)
