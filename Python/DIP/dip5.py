# %%
from keras.models import load_model
from scipy import fftpack
import scipy.linalg as al
import scipy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, MaxPool2D, Flatten
from keras.datasets import mnist
from keras.optimizers import SGD, RMSprop
from keras.utils import np_utils
import tensorflow as tf
from keras.callbacks import Callback

# Assist Func


class MineHistory(Callback):
    def on_train_begin(self, logs={}):
        self.losses = []
        self.accuracy = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))
        self.accuracy.append(logs.get('acc'))

    def plot(self):
        t = range(len(self.losses))
        plt.figure()
        plt.plot(t, self.accuracy, 'r', label='train accuracy')
        plt.plot(t, self.losses, 'g', label='train loss')
        plt.xlabel('batch')
        plt.legend(loc='upper right')
        plt.show()


def show(_img, _title=None):
    plt.figure()
    plt.suptitle(_title)
    plt.imshow(_img, cmap='gray')
    plt.show()


# %%
# Load Data
(X_train_original, y_train), (X_test_original, y_test) = mnist.load_data()

# Data Pre-Processing
X_train = np.reshape(
    X_train_original, (-1, X_train_original.shape[1], X_train_original.shape[2], 1)) / 255
X_test = np.reshape(
    X_test_original, (-1, X_test_original.shape[1], X_test_original.shape[2], 1)) / 255
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

# Construct Model
# %%
model = Sequential([
    Conv2D(32, 5, input_shape=X_train.shape[1:], padding='same'),
    Activation('relu'),
    MaxPool2D(2, 2, padding='same'),
    # Conv2D(64, 5, padding='same'),
    # Activation('relu'),
    # MaxPool2D(2, 2, padding='same'),
    Flatten(),
    Dense(32),
    Activation('relu'),
    Dense(10),
    Activation('softmax')
])

rmsprop = RMSprop(lr=0.001)

model.compile(
    loss='mean_squared_error',
    optimizer=rmsprop,
    metrics=['accuracy']
)
# %%
# training
history = MineHistory()

model.fit(X_train, y_train, batch_size=1000, epochs=2, callbacks=[history])

# %%
# Visualize

history.plot()
# %%
loss, accuracy = model.evaluate(X_test, y_test)
print("loss : {} \t accuracy : {}".format(loss, accuracy))

# precdict
y_pred = model.predict(X_test[:10])

for i in range(10):
    show(X_test_original[i, :, :], np.argmax(y_pred[i]))

# %%
model.save('kearsMinst.h5')


# %%
mine_model = load_model('kearsMinst.h5')


# %%
y_pred = mine_model.predict(X_test[:10])

for i in range(10):
    show(X_test_original[i, :, :], np.argmax(y_pred[i]))


# %%
