# %%
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# 3d 图形
# 参数形式的曲线
t = np.linspace(-10, 10, 100)
x = np.sin(t)
y = np.cos(t)
z = t
fig = plt.figure()
sub = fig.add_subplot(1, 1, 1, projection='3d')
sub.plot(x, y, z)
plt.show(sub)
# %%
X, Y = np.meshgrid(t, t)


# %%
Z = X ** 2 + Y ** 2
# %%
fig = plt.figure()
sub = fig.add_subplot(1, 1, 1, projection='3d')
sub.scatter(X, Y, Z)
plt.show(sub)
