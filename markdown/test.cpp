#include <iostream>
using namespace std;

int main()
{
    int a = 10;
    char b = 100;
    int *p = new int[10];
    *(p + 1) = a;
    *(p + 2) = b;
    return 0;
}