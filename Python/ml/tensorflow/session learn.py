# %%
import tensorflow as tf

matrix1 = tf.constant([[3, 3]])  # like np.matrix
matrix2 = tf.constant([
    [2],
    [2]
])

# run tf sessions
# method 1
ans = matrix1 * matrix2
ans  # 现在不会计算
sess = tf.Session()
res = sess.run(ans)  # 只有run()才会执行结构，否则不会计算

print(res)
sess.close()

# method 2
with tf.Session() as sess:
    res2 = sess.run(ans)
    print(res2)
