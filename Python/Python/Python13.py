'''metaclass元类'''


class MyType(type):
    def __init__(self, *args, **kwargs):
        print(123)

    def __call__(self, *args, **kwargs):  # 2
        print(456)
        self.__init__(self.__new__(self, *args, **kwargs))  # 3 6 7
        print(self.__new__(self, *args, **kwargs))


class Foo(object, metaclass=MyType):