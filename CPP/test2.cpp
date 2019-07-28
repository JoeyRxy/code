#include "lib/hello"
#include <vector>
using namespace std;

int main()
{
    vector<vector<int>> obj = {
        {2, 4, 6, 2},
        {3, 6, 2, 1}};
    for (int i = 0; i < obj.size(); i++)
    {
        for (int j = 0; j < obj[i].size(); j++)
        {
            cout << obj[i][j] << '\t';
        }
        cout << endl;
    }

    system("pause");
    return 0;
}