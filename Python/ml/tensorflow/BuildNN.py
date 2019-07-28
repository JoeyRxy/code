import tensorflow as tf
import numpy as np


def add_layer(inputs, prev_neurons, cur_neurons, activation_function=None):
    # 可以使用官方的函数:tf.layers.dense()
    layer_name = 'layer'
    with tf.name_scope(layer_name):
        with tf.name_scope('Weights'):
            Weights = tf.Variable(tf.random_normal(
                [cur_neurons, prev_neurons]), name='W')  # vector
            tf.summary.histogram(layer_name + '/Weights', Weights)
        with tf.name_scope('bias'):
            biases = tf.Variable(
                tf.zeros([cur_neurons, 1]) + 0.1, name='b')  # scale
            tf.summary.histogram(layer_name+'/bias', biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = Weights @ inputs + biases  # scale
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name+'/outputs', outputs)
    return outputs  # scale


x_data = np.linspace(-1, 1, 300)[:, None].transpose()
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

# placeholder
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, x_data.shape, name='x_input')
    ys = tf.placeholder(tf.float32, y_data.shape, name='y_input')

l1 = add_layer(xs, xs.shape[0].value, 10, tf.nn.relu)
prediction = add_layer(l1, 10, 1, tf.nn.sigmoid)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.square(ys - prediction))
    tf.summary.scalar('loss', loss)

with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(
        learning_rate=0.1).minimize(loss)  # don't forget sess.run(train_step)

sess = tf.Session()
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter('logs/', sess.graph)

init = tf.global_variables_initializer()
sess.run(init)

for i in range(2000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        res = sess.run(merged, feed_dict={xs: x_data, ys: y_data})
        writer.add_summary(res, i)
