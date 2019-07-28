import numpy as np

def H(x):
    entropy = 0
    for i in x:
        entropy -= i*np.log2(i)
    return entropy

P = 0.05, 0.01, 0.03, 0.05, 0.05, 0.07, 0.19, 0.1

entropy = H(P)

print(entropy)