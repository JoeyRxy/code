# %%
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# import cv2
from scipy import ndimage


def show(_img, _title=None):
    plt.figure()
    plt.suptitle(_title)
    plt.imshow(_img, cmap='gray')
    plt.show()


def g(_img, _thresh, Z_E, Z_B):
    N = _img.shape[0]
    M = _img.shape[1]
    res = np.zeros((N, M))
    for i in range(N):
        for j in range(M):
            if _img[i][j] >= _thresh:
                res[i][j] = Z_E
            else:
                res[i][j] = Z_B
    return res

# 类间方差


def mu(p):
    s = 0
    for i in range(len(p)):
        s += i * p[i]
    return s


def sigma(p, mu):
    s = 0
    for i in range(len(p)):
        s += (i - mu) ** 2 * p[i]
    return s


def eta(t, p):
    w0 = np.sum(p[:t])
    w1 = 1 - w0
    mu0 = mu(p[:t]) / w0
    muT = mu(p)
    mu1 = (muT - mu0) / w1
    var_w = sigma(p[:t], mu0) + sigma(p[t:], mu1)
    var_B = w0 * w1 * (mu1 - mu0) ** 2
    return var_B / (var_B + var_w)


def ostu(_img):
    N = _img.shape[0]
    M = _img.shape[1]
    freq = np.zeros((256, 1))
    for i in range(N):
        for j in range(M):
            freq[_img[i][j]] += 1
    freq /= (N * M)
    _eta = np.zeros(freq.shape)
    for t in range(1, 256):
        _eta[t] = eta(t, freq)
    return np.argmax(_eta)


img = np.array(Image.open('C:\\Users\\29388\\Pictures\\dip.png'))[:, :, 0]
show(img, 'original')
# %%
# median filter
# img_blur = cv2.medianBlur(img, 3)
img_blur = ndimage.median_filter(img, 3)
show(img_blur, 'blur')
# %%
# test with t=128
res = g(img_blur, 128, 256, 0)
show(res, 'test')
# %%
t_ostu = ostu(img_blur)
res_ostu = g(img_blur, t_ostu, 256, 0)
show(res_ostu, 'ostu')
# %%
# erosion
img_eroded = ndimage.grey_erosion(img, 1)
show(img_eroded, 'erosion r = 1')
show(g(img_eroded, 128, 256, 0), 'test_erosion r = 1')
show(g(img_eroded, ostu(img_eroded), 256, 0), 'ostu_erosion r = 1')
img_eroded = ndimage.grey_erosion(img, 3)
show(img_eroded, 'erosion r = 3')
show(g(img_eroded, 128, 256, 0), 'test_erosion r = 3')
show(g(img_eroded, ostu(img_eroded), 256, 0), 'ostu_erosion r = 3')
img_eroded = ndimage.grey_erosion(img, 5)
show(img_eroded, 'erosion r = 5')
show(g(img_eroded, 128, 256, 0), 'test_erosion r = 5')
show(g(img_eroded, ostu(img_eroded), 256, 0), 'ostu_erosion r = 5')
# %%
img_dilated = ndimage.grey_dilation(img, 1)
show(img_dilated, 'dilatation r = 1')
show(g(img_dilated, 128, 256, 0), 'test_dilatation r = 1')
show(g(img_dilated, ostu(img_dilated), 256, 0), 'ostu_dilatation r = 1')
img_dilated = ndimage.grey_dilation(img, 3)
show(img_dilated, 'dilatation r = 3')
show(g(img_dilated, 128, 256, 0), 'test_dilatation r = 3')
show(g(img_dilated, ostu(img_dilated), 256, 0), 'ostu_dilatation r = 3')
img_dilated = ndimage.grey_dilation(img, 5)
show(img_dilated, 'dilatation r = 5')
show(g(img_dilated, 128, 256, 0), 'test_dilatation r = 5')
show(g(img_dilated, ostu(img_dilated), 256, 0), 'ostu_dilatation r = 5')
