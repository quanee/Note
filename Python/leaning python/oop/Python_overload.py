
'''
常见重载函数(拦截Python内置操作)
__init__    构造函数    对象建立: X = Class(args)
__del__     析构函数    X 对象回收
__add__     运算符 +   如果没有__iadd__ X+Y X+=Y
__or__      运算符|(位or)   如果没有__ior__ X|Y X|=Y
__repr__,__str__    打印转换    print(X) repr(X) str(X)
__call__    函数调用    X(*args, **kargs)
__getattr__ 点号运算符   X.undefined
__setattr__ 属性赋值语句  X.any = value
__delattr__ 属性删除    del X.any
__getattribute__    属性获取    X.any
__getitem__ 索引 分片 迭代    X[key] X[i:j] 没__iter__时的分片 for循环和其他迭代器
__setitem__ 索引和分片赋值 X[key] = value X[i:j] = sequence
__delitem__ 索引和分片删除 del X[key] del X[i:j]
__len__     长度  len(X)如果没有__bool__ 真值测试
__bool__    布尔测试    bool(X) 真值测试(在Python2.6中叫__nonzero__)
__lt__ __gt__   特定的比较   X < Y X > Y X <= Y X >= Y X == Y X != Y (在Python2.6中只有__cmp__)
__le__ __ge__
__eq__ __ne__
__radd__    右侧加法    Other + X
__iadd__    实地(增强的)加法   X+=Y(or else __add__)
__iter__ __next__   迭代环境    l=iter(X),next(l);for loops, in if no __contains__, all comparehensions, map(F, X), others(__next__在Py2.6中称为next)
__contains__    成员关系测试  item in X(任何可迭代)
__index__   整数值 hex(X),bin(X),oct(X),O[X],O[X:](Python2为__oct__,__hex__)
__enter__ __exit__  环境管理器   with obj as var:
__get__ __set__ __delete__  描述符属性   X.attr, X.attr=value,del X.attr
__new__ 创建  在__init__之前创建对象
'''

# 索引和分片
class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value


class C:
    # 针对一个实例返回一个整数值

    def __index__(self):
        return 255


# 索引迭代
class stepper:
    def __getitem__(self, i):
        return self.data[i]


if __name__ == '__main__':
    X = Indexer()
    print(X[2])
    for i in range(5):
        print(X[i], end=' ')
    print()
    # 拦截分片
    L = [5, 6, 7, 8, 9]
    print(L[slice(2, 4)])

    print(X[2:4])
    print(X[1:])
    print(X[:-1])
    print(X[::2])

    X[3] = 'e'
    print(X.data)

    X = C()
    print(hex(X))
    print(bin(X))
    print(oct(X))

    X = stepper()
    X.data = 'love'
    print(X[1])
    for item in X:
        print(item, end=' ')
    print('p' in X)
    print([c for c in X])
    print(list(map(str.upper, X)))
    (a, b, c, d) = X
    print(a, c, d)
    print(list(X), tuple(X), ''.join(X))

'''__slot__'''
class limiter(object):
    __slots__ = ['age', 'name', 'job']


if __name__ == '__main__':
    # Slot违背Python动态特性
    x = limiter()
    x.age = 40
    print(x.age)

    # x.ape = 1000
    # AttributeError: 'limiter' object has no attribute 'ape'

# 用类方法统计实例
class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    def printNumInstances(cls):
        print("Number of instances:", cls.numInstances)

    printNumInstances = classmethod(printNumInstances)


class Sub(Spam):
    def printNumInstances(cls):
        print("Extra stuff...", cls)
        Spam.printNumInstances()

    printNumInstances = classmethod(printNumInstances)


class Other(Spam):
    ...


x, y = Sub(), Spam()
x.printNumInstances()
Sub.printNumInstances()
y.printNumInstances()
z = Other()
z.printNumInstances()


# 用类方法统计每个类的实例
# 静态方法和显示类名称用来处理类本地数据
# 类方法处理层级中的每个类不同的数据
class Spam:
    numInstances = 0

    def count(cls):
        cls.numInstances += 1

    def __init__(self):
        self.count()

    count = classmethod(count)


class Sub(Spam):
    numInstances = 0

    def __init__(self):
        Spam.__init__(self)

class Other(Spam):
    numInstances = 0


x = Spam()
y1, y2 = Sub(), Sub()
z1, z2, z3 = Other(), Other(), Other()
print(x.numInstances, y1.numInstances, z1.numInstances)
print(Spam.numInstances, Sub.numInstances, Other.numInstances)


# 装饰器
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)


@tracer
def spam(a, b, c):
    print(a, b, c)


spam(1, 2, 3)
spam('a', 'b', 'c')
spam(4, 5, 6)


'''
类装饰器和元类
def decorator(aClass):...

@decorator
class C:...
等同于
def decorator(aClass):...

class C:...
C = decorator(C)
'''
# 装饰器
def count(aClass):
    aClass.numInstances = 0
    return aClass


@count
class Spam:
    numInstances = 0

    def count(cls):
        cls.numInstances += 1

    def __init__(self):
        self.count()

    count = classmethod(count)


@count
class Sub(Spam):
    def printNumInstances(cls):
        print("Extra stuff...", cls)
        Spam.printNumInstances()

    printNumInstances = classmethod(printNumInstances)


@count
class Other(Spam):
    ...


# 元类
class Meta(type):
    def __new__(meta, classname, supers, classdict):
        ...


class C(metaclass=Meta):
    ...


# 修改类属性的副作用
class X:
    a = 1


Z = X()
print(Z.a)
# 1
print(X.a)
# 1
X.a = 2
print(Z.a)
# 2
J = X()
print(J.a)
# 2


class X:
    ...


class Y: