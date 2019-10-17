# Hilbert变换
符号约定：

$x_e[n],x_o[n]$：偶对称和奇对称序列(即使是复数序列，也不是共轭（反）对称)；   
$X_e(e^{j\omega}),X_o(e^{j\omega})$：共轭对称和共轭反对称；   
$x_r[n],X_r(e^{j\omega}),x_i[n],X_i(e^{j\omega})$：实部和虚部；   

## 因果序列的$DTFT$
### 对序列的要求
1. 因果 ： 可以从$x_e[n]$中恢复$x[n]$,从$x_o[n]$部分恢复$x[n]$.
2. 稳定

### 从$X_R(e^{j\omega})$求$X(e^{j\omega})$
$$
\begin{aligned}
    &X_R(e^{j\omega})\\
    &\Rightarrow x[n]=2x_e[n]u[n]-x_e[0]\delta[n]\\
    &\Rightarrow X(e^{j\omega}) \\
\end{aligned}
$$
---
## 单边频谱的$IDTFT$