#include <iostream>
using namespace std;

class A
{
private:
    int x;

public:
    A() {}
    A(int);
    int getX();
    void setX(int);
    ~A() { cout << "析构函数被调用了" << endl; }
};

A::A(int x)
{
    this->x = x;
}

int A::getX()
{
    return x;
}

void A::setX(int x)
{
    this->x = x;
}

int main()
{
    A *a = new A[10];
    a[0].setX(3);
    a[1].setX(4);
    cout << a[1].getX() << endl;
    delete[] a;
}
