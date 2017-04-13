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
            return item + 10

    def __setitem__(self, key, value):
        '''索引赋值'''
        print(key, value)

    def __delitem__(self, key):
        print(key)

    def __iter__(self):
        return iter([1, 2, 3, 4])


obj = Foo("abc", 23)
obj()  # 执行__call__
print(int(obj))  # __int__
print(str(obj))  # __str__
print(obj)  # __str__

o1 = Foo("bbc", 34)
o2 = Foo("cbc", 45)
ret = o1 + o2  # 执行第一个对象的__add__方法， 并将第二个对象当作参数传入
print(ret)

o3 = Foo("dbc", 55)
d = o3.__dict__
print(d)

ret = o3[4]  # 索引
print(ret)

o3[1:3:4]  # 切片

o3[23] = 46  # 赋值

del o3[56]