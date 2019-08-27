# %%
from scipy import signal
from scipy import fftpack
import scipy.linalg as al
import scipy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.image as mpimg
from PIL import Image

############################

# 有待解决疑问——为什么实验指导里的定义是从 -N/2 开始？


def PSNR(_img1, _img2):
    N, M = _img1.shape[0], _img1.shape[1]
    diff = np.abs(_img1 - _img2)
    a = np.sum(diff ** 2) / (N * M * 255 ** 2)
    return - 10 * np.log10(a)


def H(N, M, T=5, a=1, b=1):
    res = np.zeros((N, M))
    tmp = 0.
    for u in range(1, N + 1):
        for v in range(1, M + 1):
            tmp = np.pi * (a * u + b * v)
            res[u - 1][v - 1] = T / tmp * \
                np.sin(tmp) * np.exp(-np.complex(0, 1) * tmp)
    return res


def plot(_X, _title=None):
    fig = plt.figure()
    plt.suptitle(_title)
    x, y = np.linspace(0, _X.shape[0], _X.shape[0]), np.linspace(
        0, _X.shape[1], _X.shape[1])
    X, Y = np.meshgrid(x, y)
    Z = _X
    sub = fig.add_subplot(1, 1, 1, projection='3d')
    sub.plot_surface(X, Y, Z)
    sub.set_xlabel('X')
    sub.set_ylabel('Y')
    sub.set_zlabel('Z')
    plt.show(sub)


def show(_img, _title=None):
    plt.figure()
    plt.suptitle(_title)
    plt.imshow(_img, cmap='gray')
    plt.show()


############################
img = np.array(Image.open(
    'Lenna.png'))[:, :, 0]
show(img, 'original')

sigma = 0.05
mu = 0
img = img + sigma * np.random.randn(img.shape[0], img.shape[1]) + mu
show(img, "img with noise")


H_ = H(img.shape[0], img.shape[1])
plot(np.abs(H_), 'H(u,v) amp')
plot(np.angle(H_), 'H(u,v) phase')
F_img = fftpack.fft2(img)
G = H_ * F_img  # 2-d的dft相乘时域也是圆周卷积吗？？
G_r = fftpack.ifft2(G)
show(np.abs(G_r), 'After H(u,v)')
# %%
# 反向滤波
r0 = [1, 0.8, 0.5, 0.3]
for r in r0:
    xs = int(r * H_.shape[0])
    ys = int(r * H_.shape[1])
    H__ = np.ones(H_.shape)
    H__[:xs, :ys] = H_[:xs, :ys]
    img_rev = fftpack.ifft2(G / H__)
    psnr = PSNR(img_rev, img)
    show(np.abs(img_rev), 'Inverse Filter : r0 = {} : PSNR = {} dB'.format(r, psnr))

# %%
# 维纳滤波
K = np.array([0.1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-10]) * sigma
for k in K:
    img_wiener = signal.wiener(G_r, noise=k)
    psnr = PSNR(img_wiener, img)
    show(np.abs(img_wiener), 'Wiener Filter : K = {} : PSNR = {} dB'.format(k, psnr))
