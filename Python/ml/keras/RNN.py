# %%
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, MaxPool2D, Flatten, SimpleRNN
from keras.utils import np_utils
from keras.optimizers import Adam, SGD, RMSprop
from keras.datasets import mnist

TIME_STEPS = 28
INPUT_SIZE = 28
BATCH_SIZE = 50
BATCH_INDEX = 0
OUTPUT_SIZE = 10
CELL_SIZE = 50
LR = 0.001

# %%
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# first to modify the data format
X_train = np.reshape(X_train, (-1, 28, 28))/255# ATTENTION 为什么要/255呢？不除的话学习效果非常差……
# -1 用来变成4维，前面加了一个batch_size以符合模型的训练要求
X_test = np.reshape(X_test, (-1, 28, 28))/255
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

# %%
# Construct RNN
model = Sequential()

# RNN CELLS
model.add(SimpleRNN(
    CELL_SIZE,
    batch_input_shape=(None, TIME_STEPS, INPUT_SIZE)
))
# for batch_input_shape, if using tensorflow as the backend, we have to put None for the batch_size.
# Otherwise, model.evaluate() will get error.
# Or: input_dim=INPUT_SIZE, input_length=TIME_STEPS,

# output
model.add(Dense(OUTPUT_SIZE))
model.add(Activation('softmax'))

# optimizer
adam = Adam(lr=LR)
model.compile(optimizer=adam, loss='categorical_crossentropy',
              metrics=['accuracy'])

# %%
# training

for step in range(4000):
    X_batch = X_train[BATCH_INDEX: BATCH_INDEX+BATCH_SIZE, :, :]
    Y_batch = y_train[BATCH_INDEX: BATCH_INDEX+BATCH_SIZE, :]
    loss = model.train_on_batch(X_batch, Y_batch)

    BATCH_INDEX += BATCH_SIZE
    if BATCH_INDEX >= X_train.shape[0]:
        BATCH_INDEX = 0

    if step % 500 == 0:
        loss, accuracy = model.evaluate(
            X_test, y_test, batch_size=X_test.shape[0], verbose=False)
        print("loss: {},accuracy: {}".format(loss, accuracy))
