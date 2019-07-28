# TODO 没建成层还
# %%
import numpy as np
from numpy import random
from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, MaxPool2D, Flatten
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.datasets import mnist
from keras.optimizers import RMSprop, Adam
# %%
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# first to modify the data format
X_train = np.reshape(X_train, (-1, 28, 28, 1))
# -1 用来变成4维，前面加了一个batch_size以符合模型的训练要求
X_test = np.reshape(X_test, (-1, 28, 28, 1))
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

# %%
model = Sequential()
# convolution
model.add(Conv2D(
    input_shape=(28, 28, 1),
    filters=32,
    kernel_size=(5, 5),
    padding="same",
    data_format="channels_last"
))
# activation
model.add(Activation('relu'))
# pooling
model.add(MaxPool2D(
    pool_size=(2, 2),
    strides=(2, 2),
    data_format="channels_last",
    padding="same"
))
# convolution number of filters=64,kernel_size=(5,5)
model.add(Conv2D(
    filters=64,
    padding='same',
    kernel_size=(5, 5),
    data_format="channels_last"
))
# activation
model.add(Activation('relu'))
# pooling
model.add(MaxPool2D(
    strides=(2, 2),
    padding='same',
    data_format="channels_last"
))

# Flatten for using Dense
model.add(Flatten())

model.add(Dense(1024))
model.add(Activation('relu'))
model.add(Dense(10))
model.add(Activation('softmax'))
# 结构建成
# %%
adam = Adam(lr=1e-4)
# compile
model.compile(
    loss='categorical_crossentropy',
    optimizer=adam,
    metrics=['accuracy']
)
# %%
# training using fit
model.fit(X_train, y_train, batch_size=64, epochs=1)

# %%
# test
loss, accuracy = model.evaluate(X_test, y_test)
print(loss)
print(accuracy)
# %%
pred = model.predict(X_test)
# %%
for i in range(10):
    print('================================')
    plt.figure()
    plt.imshow(X_test[i, :, :, 0])
    plt.title("{}".format(np.argmax(pred[i])))
