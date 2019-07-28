# %%
import numpy as np
from numpy import random
from keras.models import Sequential
from keras.layers import Dense, Activation
import matplotlib.pyplot as plt

from keras.datasets import mnist
from keras.utils import np_utils
from keras.optimizers import RMSprop

import keras


class MineHistory(keras.callbacks.Callback):
    # For Visualization
    def on_train_begin(self, logs={}):
        self.losses = []
        self.accuracy = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))
        self.accuracy.append(logs.get('acc'))
    # Plot Acc & Loss curve

    def plot(self):
        t = range(len(self.losses))
        fig = plt.figure()
        plt.plot(t, self.accuracy, 'r', label='train accuracy')
        plt.plot(t, self.losses, 'g', label='train loss')
        plt.xlabel('batch')
        plt.legend(loc='upper right')
        plt.grid(True)
        fig.savefig("Loss & Acc.png")

# assistant func for show img


def show(_img, _title=None):
    plt.figure()
    plt.suptitle(_title)
    plt.imshow(_img)
    plt.show()


def awgn(X, n):
    # Adding Noise
    for i in range(len(X)):
        noise = np.abs(random.randn(X[i].shape[0], X[i].shape[1]))
        X[i] = X[i] + noise * n


# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# data preprocessing
X_train = X_train.reshape(X_train.shape[0], -1) / 255
y_train = np_utils.to_categorical(y_train, num_classes=10)

# construct model : 3 layers NN
model = Sequential([
    Dense(1024, input_dim=X_train.shape[1]),
    Activation('relu'),
    Dense(64),
    Activation('relu'),
    Dense(10),
    Activation('softmax')
])

# define optimizer
rmsprop = RMSprop()
# compile
model.compile(
    loss='categorical_crossentropy',  # loss func : categorical crossentropy
    optimizer=rmsprop,
    metrics=['accuracy']
)

# training using fit
history = MineHistory()
model.fit(X_train, y_train, batch_size=1000, epochs=8, callbacks=[history])
# visualize loss func
history.plot()

(X_train, y_train), (X_test, y_test) = mnist.load_data()
show(X_test[7])
awgn(X_test, 7)  # Add noise
show(X_test[7])

X_test = X_test.reshape(X_test.shape[0], -1) / 255
y_test = np_utils.to_categorical(y_test, num_classes=10)

loss, accuracy = model.evaluate(X_test, y_test)
print("loss : {} \t accuracy : {}".format(loss, accuracy))

# precdict
# %%
y_pred = model.predict(X_test[:20])

for i in range(20):  # print first 10 test
    print("predict:{}\tans:{}".format(
        np.argmax(y_pred[i]), np.argmax(y_test[i])))  # print predict comparing with answer


# %%
