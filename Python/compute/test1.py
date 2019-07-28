import scipy.linalg as al
import numpy as np
import scipy.integrate
from scipy.special import comb


def f(x):
    return 1 / scipy.sqrt(2 * scipy.pi) * scipy.exp(-x ** 2 / 2)


def Q(a):
    return scipy.integrate.quad(f, a, scipy.inf)


def P_b_after_channels_coding(P_original, n, t):
    '''
    t : 可纠正的错码的个数
    '''
    return 1 / n * np.sum([i * comb(n, i) * P_original ** i * (1 - P)**(n - i) for i in range(t + 1, n + 1)])


if __name__ == "__main__":
    P = Q(np.sqrt(13))[0]
    print(P_b_after_channels_coding(P, 7, 1))
