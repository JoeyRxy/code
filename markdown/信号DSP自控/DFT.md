[matlab参考文件][reffile]
# DFT分析连续信号
DFT的第k个 如何 对应到连续时间的$X_c(j\Omega)$:

$$
\displaystyle{X[k]=X(e^{j\omega})\bigg|_{\omega=\dfrac{2\pi k}{N}}=\dfrac{1}{T}X_c(j\Omega)\bigg|_{\Omega=\dfrac{\omega}{T}=\dfrac{2\pi k}{NT}}}
$$

# 循环卷积和线性卷积
两个原序列：$x_1[n],x_2[n]$，循环卷积得到的序列$x_{3r}[n]$，线性卷积得到的$x_3[n]$.
$$
x_{3r}[n]=\displaystyle\sum_{r=0}^{N-1}x_1[r]x_2[(N-r)\%N]
$$
1. 循环卷积的计算方法：将序列$x_2[n]$进行周期为$N$的延拓，再进行线性卷积
2. 另外一种计算方法**更合适**：也就是**线性卷积**和**循环卷积**的关系：
    先算出线性卷积，再以$N$为周期进行延拓。

    在频域上，就是先变成$X_1(e^{j\omega})X_2(e^{j\omega})$，再以$N$频域采样。

    “先卷积再延拓 和 先延拓再卷积是一样的”

# 线性相位的拓展
什么性质的$x[n]$才具有$A[k]e^{j\alpha k}$形式的DFT？

动动脑子：

当然是 $\widetilde{x}[n]$具有对称性的（只是充分条件）

# 增减采样在DFT上的体现（再认识）
## 减采样
$$
x_d[n]=x[Mn]
$$
总长度$N'=N/M$（假设能够整除）
#### 1) 连续频域
$$
X_d(e^{j\omega})=\frac{1}{M}\sum_{r=1}^{M-1}X(e^{j\frac{\omega-2\pi r}{M}})
$$
#### 2) 离散频域
在$N\%M==0$的情况下

直接利用$\omega=\dfrac{2\pi k}{N/M}$的关系式，带入到上式中：
$$
X_d[k]=\frac{1}{M}\sum_{r=1}^{M-1}X\left[k-r\dfrac{N}{M}\right]\qquad  k=0,1,...,\left(\frac{N}{M}-1\right)
$$

> 从记忆的角度来说，“频域采样，时域周期延拓”=>原来以N为周期周期延拓，现在以N/M为周期延拓
## 增采样
### Ⅰ.未经内插的“增采样”
$$
x_e[n]=\begin{cases}
    x[n/L]&,n=L,2L,...\\
    0&,others
\end{cases}
$$
总长度$N' = NL$
#### 1) 连续频域
$$
X_e(e^{j\omega})=X(e^{jL\omega}))
$$
#### 2) 离散频域
$$
X_e[k]=X[k]
$$
看似一样，但是记住 ***DFT要在DFS*** 上来看：
这里的离散频域的长度为$NL$，就是DFS截取了得更长了。

图：

### Ⅱ.真正的增采样
经过低通滤波器滤去主值以外的图形，在时域上的表现就是经过了一边 重构 ==> 内插，其表达式为

$$
x_i[n]=x_c(nT/L)
$$

#### 1) 连续频域
$$

X_i(e^{j\omega})=LX(e^{jL\omega})\quad{\color{red}{\omega<|\pi/L|}}
\overset{DTFT}{\xLeftarrow{}}x_c(nT/L)
$$


#### 2) 离散频域
在频域以$\dfrac{2\pi k}{NL}$采样
$$
X_i[k]=\begin{cases}
    LX[k]&,0<\omega<\frac{N}{2}\cup NL-\frac{N}{L}<\omega<NL\\
    0&,others
\end{cases}
$$

fig:
![](2019-09-16-19-19-15.png)

***上图中为什么在60附近出现了偏差呢？***

原因：

实际上，如果图象是带限的，那么理应在32到95之间（见上）为0。但是问题是函数**不带限**!

如果一个$X(e^{j\omega})$在$\omega_c<\pi$点之后都截止了，那么其IDTFT一定是一个无限长度的脉冲响应。如果是FIR，那么一定是经过了 加窗 操作。所以实际上用计算机处理的时候都是不带限的。

那么为什么不带限就出现了不为0呢？

这时候就要说一说这个图是怎么来的（可参见[matlab文件][reffile]），我们已经假设 已经知道了被采样的信号，而由于被采样的信号**不是带限**，那么我们增采样之后，由$X_c(j\frac{\omega-2\pi r}{T/2})$可以看出确实是图中结果，而且增采样之后的高频部分（中间部分）**更低**了。

[reffile]:dft.mlx