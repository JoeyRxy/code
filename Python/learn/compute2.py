# %%
import myPack.information_theroy as info
import numpy as np

X = np.ones((1, 4))/4
P = np.zeros((4, 4))
P[1][3] = P[0][3] = 1
P[2][0] = P[2][1] = 1 / 2
P[3][2] = 1
# %%
print(X)
print(P)
# %%
t1 = info.entropy(X, P)
Y = t1.Y
print(Y)
P2 = P * P
print(P2)
t2 = info.entropy(X, P2)
print(t1.IXY)
print(t2.IXY)
# %%
np.log2(3) - info.entropy.H(1/2, 1/3, 1/6)
