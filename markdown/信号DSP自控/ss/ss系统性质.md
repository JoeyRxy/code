# 判断系统性质
## 1. 线性系统
$T[k_1e_1(t)+k_2e_2(t)]=k_1r_1(t)+k_2r_2(t)$
## 2. 时不变系统
$T[e(t-t_0)]=r(t-t_0)$
## 3. 因果系统
### 1) 一般系统
当输入在$t_0$时刻变化时，输出在$t\ge t_0$时刻发生变化.
### 2) LTI系统
冲激响应$h(t)$满足：在$t<0$时$h(t)=0$.
## 4. 稳定系统
### 1) 一般系统
BIBO原则
### 2) LTI系统
冲激响应$h(t)$满足：
$\displaystyle\int_{-\infty}^{\infty}|h(t)|\mathrm{d}t<\infty$

# 题目
1. 求$4\varepsilon(t)\delta(t)$
    答案：$2\delta(t)$  
    - [ ] why？难道是在跳变处取值为$\dfrac{f(t-0)+f(t+0)}{2}$？搞不好真是这样
2. 

