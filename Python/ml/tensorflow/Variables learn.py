# %%
import tensorflow as tf

state = tf.Variable(0, name="counter")  # 与python的原生变量是不同的，必须要通过该语句来标明是 变量
print(state.name)

one = tf.constant(1)

new_val = state + 1

update = tf.assign(state, new_val)

init = tf.global_variables_initializer()  # ATTENTION Important

with tf.Session() as sess:
    sess.run(init)  # 不仅要init，还要执行(run)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
