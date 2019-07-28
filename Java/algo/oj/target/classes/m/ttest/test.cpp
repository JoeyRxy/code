#include <iostream>
using namespace std;

int PI(int n)
{
    int ans = 1;
    for (int i = 1; i <= n; i++)
    {
        ans *= i;
    }
    return ans;
}

int SUM(int n)
{
    int s = 0;
    for (int i = 1; i <= n; i++)
    {
        s += i;
    }
    return s;
}

int f(int n, int (*func)(int))
{
    return func(n);
}

int main()
{
    int a[] = {1, 2, 3};
    for (auto &i : a)
    {
        cout << f(i, PI) << endl;
    }
    for (auto &i : a)
    {
        cout << f(i, SUM) << endl;
    }
    system("pause");
}