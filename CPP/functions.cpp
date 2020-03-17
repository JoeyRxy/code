#include <iostream>
#include <functional>

using namespace std;

unsigned int callback(string original)
{
    string res(original);
    res.append(" fuck");
    cout << res << endl;
    hash<string> str_hash;
    unsigned int h = str_hash(res);
    return h;
}

void f(string str, unsigned int (*g)(string))
{
    cout << str << endl;
    cout << "test callback :" << endl;
    cout << g(str) << endl;
}

int main(int argc, char const *argv[])
{
    string str("hhhhhhhhhhhh");
    f(str, callback);
    return 0;
}
