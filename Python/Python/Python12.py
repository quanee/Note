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
        return 'str'

    def __add__(self, other):
        '''self = o1 other = o2'''
        return '__add__'

    def __del__(self):
        print('析构方法')

    def __getitem__(self, item):
        '''索引访问'''
        if type(item) == slice:
            print("切片")
            print(item.start)
            print(item.stop)
            print(item.step)
        else:
            print("索引")