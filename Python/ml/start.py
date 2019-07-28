# 函数作为参数传递
def test(a, b, c):
    print("a is {}", a)
    print("b is {}", b)
    print("c is {}", c)

argss = ("hello", 32, 1.4)

kwargss = {"a": 2, "b": 45, "c": "helllll"}
#必须要求键值和形参的名称一样

test(*argss)

test(**kwargss)