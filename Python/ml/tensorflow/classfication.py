# %%
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import numpy as np


# model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# model.compile(optimizer='sgd', loss='mean_squared_error')

# xs = np.array([-1, 0, 1, 2, 3, 4])
# ys = np.array([-3, -1, 1, 3, 5, 7])

# plt.scatter(xs, ys)

# model.fit(xs, ys, epochs=500)

# x_predict = np.linspace(-10, 10)

# plt.scatter(x_predict, model.predict(x_predict))
# %%

mnist = tf.keras.datasets.fashion_mnist

(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
# %%
plt.imshow(training_images[0])
print(training_images[0])
# %%
training_images = training_images / 255.0
test_images = test_images / 255.0
model = keras.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(200, tf.nn.relu),
    keras.layers.Dense(10, tf.nn.sigmoid)
])
#%%
model.compile(optimizer = tf.train.AdamOptimizer(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5)

#%%
model.evaluate(test_images, test_labels)

#%%
predic = model.predict(test_images)
print(predic[0])