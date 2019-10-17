$LTI$系统$\operatorname{T}$是一个从函数集合到函数集合的**线性**映射；

根据特征向量和特征值的方法来看待映射：

取特征向量$\operatorname{e}^{\operatorname{j}\Omega_0 t}$，经过$LTI$得到的函数为$y(t)=\operatorname{T}[x(t)]$.   
满足：
$$
y(t)=H(\operatorname{j}\Omega_0)\operatorname{e}^{\operatorname{j}\Omega_0 t}
$$

那么，特征值为$H(\operatorname{j}\Omega_0)$

> 离散的情况类似:$y[n]=H(\operatorname{e}^{\operatorname{j}\omega_0})\operatorname{e}^{\operatorname{j}\omega_0 n}$

> 在这里，*特征向量*被称为*特征函数*，或就是**频率响应**

## 系统函数$h[n]$
如果根据一个输入$x_0[n]$和一个输出$y_0[n]$，猜出了一个$h[n]$，那么这个系统函数满足什么条件的时候，就是真的系统函数呢？

你找的规律应该是：
$y[n]=\displaystyle\sum_{k=-\infty}^\infty a_k x[n-k]$
其中**加法和数乘**对应**线性**；**时延**对应**时不变**.