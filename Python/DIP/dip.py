# %%
from scipy import fftpack
import scipy.linalg as al
import scipy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image


def dct(x):
    return fftpack.dct(x, norm='ortho')


def idct(x):
    return fftpack.idct(x, norm='ortho')


def plot(_X, _title=None):
    fig = plt.figure(figsize=[20, 15])
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
    plt.figure(figsize=[20, 15])
    plt.suptitle(_title)
    plt.imshow(_img, cmap='gray')
    plt.show()


def gatefilter(_IMG):
    num = _IMG.shape[0] * _IMG.shape[1]
    img_reshape = np.reshape(np.abs(_IMG), (num, 1))
    t = np.sort(img_reshape)[int(num * 0.95)][0]
    for i in range(_IMG.shape[0]):
        for j in range(_IMG.shape[1]):
            if abs(_IMG[i][j]) < t:
                _IMG[i][j] = 0


def PSNR(_img1, _img2):
    N, M = _img1.shape[0], _img1.shape[1]
    diff = np.abs(_img1 - _img2)
    a = np.sum(diff ** 2) / (N * M * 255 ** 2)
    return - 10 * np.log10(a)


img = np.array(Image.open(
    'DIP\\Lenna.png'))[:, :, 0]
show(img, 'original')
# %%
# fft
fft_img = fftpack.fft2(img)
print("====================== FFT ========================")
print(fft_img)
amp_fft = np.abs(fft_img)
pha_fft = np.angle(fft_img)
# %%
# amp_fft
plot(amp_fft, 'AMP of FFT')
show(np.abs(amp_fft), 'AMP of FFT')
# %%
# phase
plot(pha_fft, 'PHASE of FFT')
show(pha_fft, 'phase of fft')
# %%
# ifft
gatefilter(fft_img)
img_r = fftpack.ifft2(fft_img)
show(np.abs(img_r), 'FFT recovery')
print("PSNR of fft")
print(PSNR(img, np.abs(img_r)))

# %%
# DCT
dct_img = dct(img)
print("====================== DCT =====================")
print(dct_img)
gatefilter(dct_img)
img_dct_r = idct(dct_img)

amp_dct = np.abs(dct_img)
pha_dct = np.angle(dct_img)
# %%
# amp_dct
plot(amp_dct, 'AMP of DCT')
show(amp_dct, 'AMP of DCT')
# %%
# phase dct
plot(pha_dct, 'PHASE of DCT')
# %%
show(np.abs(img_dct_r), "IDCT RECOVERY")
print("PSNR of dct")
print(PSNR(img, np.abs(img_dct_r)))
# %%
# Walsh-Hadamard
N = img.shape[0]
G = al.hadamard(N)
hadamard_img = G @ img @ G
hadamard_img = hadamard_img/N**2
print("============= Walsh-Hadamard ===================")
print(hadamard_img)
# %%
# hadamard
plot(hadamard_img, 'HADAMARD')
show(hadamard_img, 'HADAMARD')
# %%
gatefilter(hadamard_img)
img_hadamard_r = G @ hadamard_img @ G
show(img_hadamard_r, 'WALSH-HADAMARD RECOVERY')
print("PSNR of hadamard")
print(PSNR(img, img_hadamard_r))
