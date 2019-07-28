# %%
import numpy as np
from numpy import random
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

X = np.linspace(-1, 1, 200)
random.seed(1234)
random.shuffle(X)
Y = 0.5 * X + 2 + random.normal(0, 0.05, (200,))
plt.scatter(X, Y)
# %%
X_train, Y_train = X[:160], Y[:160]
X_test, Y_test = X[160:], Y[160:]
# %%
model = Sequential(
    [Dense(1, input_dim=1)],
    [Dense(1)]
)  # 创建一个顺序模型：一次添加层之类的

model.compile(loss='mse', optimizer='sgd')
# %%
# train
for step in range(300):
    cost = model.train_on_batch(X_train, Y_train)
    if step % 100 == 0:
        print("train cost: {}".format(cost))
# %%
# test
cost = model.evaluate(X_test, Y_test)
print("test: {}".format(cost))
W, b = model.layers[0].get_weights()

print("Weights: {}\tbiases: {}".format(W, b))
# %%
Y_predict = model.predict(X_test)
plt.scatter(X_test, Y_test)
plt.plot(X_test, Y_test)
