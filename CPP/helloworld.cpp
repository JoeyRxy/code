#include <iostream>
using namespace std;

int f(int n)
{
    if (n == 0 || n == 1)
        return 1;
    else
        return n * f(n - 1);
}

int main()
{
    int res = f(10);
    cout << "helloworld\t" << res << endl;
    system("pause");
    return 0;
}