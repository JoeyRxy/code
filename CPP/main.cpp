#include <iostream>
#include "lib/DC3"
int main()
{
    char s[] = "mississippi";
    int N = sizeof(s);
    int *T = new int[N + 3];
    for (int i = 0; i < N; i++)
        T[i] = s[i];
    T[N] = T[N + 1] = T[N + 2] = 0;
    int *SA = new int[N];
    suffixArray(T, SA, 12, 128);
    for (int i = 0; i < N; i++)
    {
        printf("%d ", SA[i]);
    }
    system("pause");
}