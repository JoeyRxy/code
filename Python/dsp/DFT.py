# %%
import numpy as np
import scipy.fftpack


def fft(x):
    return scipy.fftpack.fft(x)


def ifft(X):
    return scipy.fftpack.ifft(X)


# %%


def x(n):
    return np.sin(n)


# %%
n = np.arange(0, 8, 1)
n1 = np.arange(0, 8, 2)

# %%
xn = x(n)
print(xn)
x1n = x(n1)
print(x1n)

X = fft(x)
X1 = fft(x1n)

print("X: "+X)
print("X1: "+X1)

# %%
