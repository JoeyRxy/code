#include <iostream>
using namespace std;

int main()
{
    int a[2][3] = {
        {1, 2, 3},
        {4, 5, 6}};
    cout << a[1][2] << endl;

    int **pa = new int *[2];
    for (int i = 0; i < 2; i++)
    {
        pa[i] = new int[3];
    }
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            pa[i][j] = i + j;
        }
    }
    cout << pa[0][0] << endl;

    return 0;
}