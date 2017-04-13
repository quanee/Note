'''特殊成员'''



class Foo:

    def __init__(self, name, age):
        print('init')
        self.__name = name
        self.__age = age

    def __call__(self, *args, **kwargs):
        print('call')

    def __int__(self):
        return 123

    def __str__(self):