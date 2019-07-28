# from scipy import fftpack
import numpy as np

# ATTENTION DCT定义繁多，最正确的应该是在参数的norm选项里声明为


""" def dct(x):
    return fftpack.dct(x, norm='ortho')


def idct(x):
    return fftpack.idct(x, norm='ortho')


x = np.array([i for i in range(16)])
print(x)
x_r = idct(dct(x))
print(x_r)
 """

a = [2, 9, 7, 1, 4]
b = np.array(a)
c = b.tolist()
c2 = list(b)
d = list(c2)

print(a)
print(b)
print(c)
print(c2)
print(d)
