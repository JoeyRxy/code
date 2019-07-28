import numpy as np


def sigmoid(z):
    return 1/(1+np.exp(z))


def ReLU(z):
    if z >= 0:
        return z
    else:
        return 0


def dReLU(z):
    if z >= 0:
        return 1
    else:
        return 0


def ml(X, Y, alpha, N, n1):
    n0 = X.shape[0]
    m = X.shape[1]
    W1 = np.random.rand(n1, n0)  # first layer with n1 neurons
    W2 = np.random.rand(1, n1)  # second(output) lyaer with 1 layer
    B1 = np.zeros((n1, 1))
    B2 = np.zeros((1, 1))

    # Gradient Descent
    for _ in range(N):
        # forward
        A0 = X
        Z1 = W1@A0+B1
        A1 = ReLU(Z1)
        Z2 = W2@A1+B2
        A2 = sigmoid(Z2)
        # backward
        dZ2 = A2 - Y  # dZ2 denotes dL/dZ2
        dW2 = dZ2 * A1 / m
        dB2 = 1/m * np.sum(dZ2, axis=1, keepdims=True)
        dA1 = W2 * dZ2
        dZ1 = dA1 * dReLU(Z1)
        dW1 = dZ1 * A0 / m
        dB1 = 1/m * np.sum(dZ1, axis=1, keepdims=True)
        # update parameter
        W1 -= alpha * dW1
        W2 -= alpha * dW2
        B1 -= alpha * dB1
        B2 -= alpha * dB2

    A0 = X
    Z1 = W1@A0+B1
    A1 = ReLU(Z1)
    Z2 = W2@A1+B2
    A2 = sigmoid(Z2)
    return A2
