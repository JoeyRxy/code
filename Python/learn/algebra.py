'''
python(numpy)里的矩阵运算
---
不用python原生的matrix(2-D array)\n
先使用 A=np.matrix(A) 转换成numpy矩阵
在导入algebra库之后可以使用inv等函数
\n
操作：\n
* -> 矩阵乘法
multiply -> 点乘
'''
import numpy as np
import numpy.linalg as al
from numpy import matrix


A = [0.1, 0.3, 0.6]


B = [
    [0.6, 0.2, 0.2],
    [0.7, 0.1, 0.2],
    [0.4, 0.5, 0.1]
]

print(A)
print(B)

# begin test
A = matrix(A)
B = matrix(B)
# should transform the python matrix(2-D array) to np.matrix

C = A * B
print('C:\n')
print(C)
D = A @ B
print('D:\n')
print(D)
# for np.matrix,@ is enqual to *

E = np.multiply(A.transpose(), B)
print('E\n')
print(E)
# np.multiply() is element-wise and can broadcast

# for more linear algebra,using np.linalg

# invese of B
B_inv = al.inv(B)
print('inverse of B:\n')
print(B_inv)