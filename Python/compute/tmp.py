# %%
from myPack.information_theroy import entropy
import huffman
import myPack.information_theroy as info
import numpy as np

X = np.array([0.25, 0.25, 0.2, 0.15, 0.1, 0.05])
# print(info.entropy.H(X))
print("length\n{}".format(info.entropy.codeLength(X)))
print(info.entropy.code_efficiency(X))
# %%
print(huffman.codebook(
    [
        (0, 1),
        (1, 3),
        (2, 3),
        (3, 9),
        (4, 3),
        (5, 9),
        (6, 9),
        (7, 27)
    ]
)
)
# %%
info.entropy.code_efficiency(np.array([1, 3, 3, 9, 3, 9, 9, 27])/64)

# %%
info.entropy.H([0.2, 0.19, 0.18, 0.17, 0.15, 0.1, 0.01])
##
# Shannon
# %%
xxx = [0, 0, 1, 1]
s = str(xxx)
print(s)
# %%


def Shannon(X):
    '''X is P(X)'''
    L = np.ceil(info.entropy.codeLength(X))
    L = [int(i) for i in L]
    code = ['' for _ in range(len(X))]
    i = 0
    x = X[0]
    _bin = []
    for l in L:
        x = X[i]
        _bin = []
        for _ in range(l):
            x *= 2
            _bin.append(str(int(x)))
        code[i] = ''.join(_bin)
        i += 1
    return code


# %%
ans = Shannon(X)
print(ans)
# %%
X = [0.1, 0.9]
print(entropy.H(X))
print(entropy.code_efficiency(X))
# %%
print(huffman.codebook([
    (1, 0.2),
    (2, 0.19),
    (3, 0.18),
    (4, 0.17),
    (5, 0.15),
    (6, 0.1),
    (7, 0.01)
]))
