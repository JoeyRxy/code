class OOPTest():
    def __init__(self, x):
        self._x = x
        self.func()
        self.staticFunc(self._x)

    def func(self):
        if (self._x > 10):
            print(self._x)
        else:
            print("wrong")

    @staticmethod
    def staticFunc(x):
        if (x <= 10):
            print(x)
        else:
            print("wrong")


if __name__ == "__main__":
    t = OOPTest(100)
    t2 = OOPTest(1)
    OOPTest.staticFunc(100)
