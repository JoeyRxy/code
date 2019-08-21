# c/cpp中数组的查看技巧：
```c
int a[10]={1,2,3,4,5,6,7,8,9,0};
int * p =a;
```
使用`*p`可以查看第一个的值；使用`p[2]`查看`a[2]`的值；如何一并查看呢？

`*p@10`即可

# 容器的查看
```cpp
vector<int> v;
```
gdb:
```gdb
p *(v._M_impl._M_start)@(v.size())
```
vscode中只要将其卸载洼watch窗口中即可。

其实和数组是一样的。

## 二维数组
```cpp
int **dp = new int*[N];
for (int i = 0; i < N; i++)
{
   dp[i] = new int[M];
}
```

一个$N\times{}M$的数组；

```gdb
p **dp@M@N
```

注意先后顺序