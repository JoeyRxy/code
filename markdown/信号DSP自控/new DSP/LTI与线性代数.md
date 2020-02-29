# 系统的特征函数
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

> $\colorbox{yellow}{ATTENTION}$:这里的特征函数$\operatorname{e}^{\operatorname{j}\omega_0 n},\operatorname{e}^{\operatorname{j}\Omega_0 t}$取值范围都是$(-\infty,+\infty)$. 
> 一旦进行截断，就会导致出现其他频率分量。    
## 更牛的特征函数（复频域）
- Laplace : $T[\operatorname{e}^{s_0t}]=H(s_0)\operatorname{e}^{s_0t}$
- Z : $T[z_0^n]=H(z_0)z_0^n$

同理也要注意，t和n的范围都是$(-\infty,\infty)$
# 系统函数$h[n]$
如果根据一个输入$x_0[n]$和一个输出$y_0[n]$，猜出了一个$h[n]$，那么这个系统函数满足什么条件的时候，就是真的系统函数呢？

你找的规律应该是：
$y[n]=\displaystyle\sum_{k=-\infty}^\infty a_k x[n-k]$
其中**加法和数乘**对应**线性**；**时延**对应**时不变**.

# 正交性
这个性质其实推导的时候很常用，所以一些探究性的题目有可能会用到
## DFT
$$
\begin{aligned}
    \sum_{{\color{red}{}k=0}}^{N-1}W_N^{(n-r){\color{red}{}k}=}\begin{cases}
        N,&r=n\\
        0,&r\ne n
    \end{cases}
\end{aligned}
$$
其实就是$\operatorname{DFT}_N[1]=N\delta[k]$