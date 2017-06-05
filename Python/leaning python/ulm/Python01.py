'''特性'''

class Person(object):
    """docstring for Person"""

    def __init__(self, name):
        self._name = name

    def getName(self):
        print('fetch...')
        return self._name

    def setName(self, value):
        print('change...')
        self._name = value

    def delName(self):
        print('remove...')
        del self._name

    name = property(getName, setName, delName, "name property docs")


bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)
print(Person.name.__doc__)
print(help(Person.name))


'''计算的属性'''
class PropSquare(object):
    """docstring for PropSquare"""

    def __init__(self, start):
        self.value = start

    def getX(self):
        return self.value ** 2

    def setX(self, value):
        self.value = value

    X = property(getX, setX)


P = PropSquare(3)
Q = PropSquare(32)

print(P.X)
P.X = 4
print(P.X)
print(Q.X)


'''使用装饰器编写特性'''
class Person(object):
    """docstring for Person"""

    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # name = property(name)
        '''name property docs'''
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):  # name = name.setter(name)
        print('change...')
        self._name = value

    @name.deleter
    def name(self):  # name = name.deleter(name)
        print('remove...')
        del self._name


bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)
print(Person.name.__doc__)
print(help(Person.name))


'''描述符'''
# 特性是描述符的一种

'''
class Descriptor:
    """docstring goes here"""
    def __get__(self, instance, owner):...
    def __set__(self, instance, value):...
    def __delete__(self, instance):...

带有这些方法的类都可以看做描述符
'''

class Descriptor(object):
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')


class Subject:
    attr = Descriptor()


X = Subject()
X.attr
Subject.attr


# 只读描述符
class D:
    def __get__(*args):
        print('get')

    def __set__(*args):
        raise AttributeError('cannot set')


class C:
    a = D()


X = C()
X.a
# X.a = 99  # AttributeError: cannot set
"""
*** __deleter__:试图删除所有者类的一个实例上的管理器属性名称
*** __del__:实例析构方法
"""

class Name:
    '''name descriptor docs'''

    def __get__(self, instance, owner):  # self是Name类实例 instance是Person类实例 owner是Person类实例
        print('fetch...')
        return instance._name

    def __set__(self, instance, value):
        print('change...')
        instance._name = value

    def __delete__(self, instance):
        print('remove...')
        del instance._name


class Person:

    def __init__(self, name):
        self._name = name

    name = Name()


bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)
print(Name.__doc__)


class DescState(object):
    """docstring for DescState"""

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print('DescState get')
        return self.value * 10

    def __set__(self, instance, value):
        print('Descriptor set')
        self.value = value


class CalcAttrs(object):
    """docstring for CalcAttrs"""

    X = DescState(2)
    Y = 3  # 客户类

    def __init__(self):
        self.Z = 4  # 实例


obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)
obj.X = 5
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)


class InstState(object):
    """docstring for InstState"""

    def __get__(self, instance, owner):
        print('InstState get')
        return instance._Y * 100

    def __set__(self, instance, value):
        print('InstState set')
        instance._Y = value


class CalcAttrs:
    X = DescState(2)
    Y = InstState()

    def __init__(self):
        self._Y = 3
        self.Z = 4


obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)
obj.X = 5
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)


'''模拟property函数'''
class Property(object):
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)


class Person(object):
    def getName(self):
        ...

    def setName(self, value):
        ...

    name = Property(getName, setName)


'''属性拦截'''
class Catcher:
    def __getattr__(self, name):
        print('Get:', name)

    def __setattr__(self, name, value):
        print('Set:', name, value)


X = Catcher()
X.job
X.pay
X.pay = 99

# 避免循环
# # 把获取指向一个更高的超类 (x = object.__getattribute__(self, 'other'))
# # 把属性作为实例的__dict__命名空间字典中的一个键赋值 (self.__dict__['other'] = value)
# # 把属性赋值传递给一个更高的超类 (object.__setattr__(self, 'other', value))
# # 不能使用__dict__在__getattribute__中, __dict__会再次触发__getattribute__导致递归循环


class Person(object):
    def __init__(self, name):
        self._name = name  # 触发__setattr__

    def __getattribute__(self, attr):
        if attr == 'name':  # 拦截未定义属性
            print('fetch...')
            attr = '_name'
        #     return self._name  # 返回属性
        # else:
        #     raise AttributeError(attr)
        return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value):  # obj.any = value
        if attr == 'name':
            print('change...')
            attr = '_name'  # 设置内部变量命
        self.__dict__[attr] = value  # 避免循环

    def __delattr__(self, attr):
        if attr == 'name':
            print('remove...')
            attr = '_name'  # 避免循环

        del self.__dict__[attr]


bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name
print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)


# __getattr__和__getattribute__
class GetAttr(object):
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, attr):   # 未定义变量
        print('get: ' + attr)
        return 3


X = GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)
print('-' * 40)

class GetAttribut(object):
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattribute__(self, attr):
        print('get: ' + attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)


X = GetAttribut()
print(X.attr1)
print(X.attr2)
print(X.attr3)


'''管理属性'''
class Powers(object):
    """使用特性拦截并计算属性(square, cube)"""

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def getSquare(self):
        return self._square ** 2

    def setSquare(self, value):
        self._square = value

    square = property(getSquare, setSquare)

    def getCube(self):
        return self._cube ** 3

    cube = property(getCube)


X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)


class DescSquare(object):
    """描述符拦截计算属性"""

    def __get__(self, instance, owner):
        return instance._square ** 2

    def __set__(self, instance, value):
        instance._square = value
class DescCube(object):
    def __get__(self, instance, owner):
        return instance._cube ** 3


class Powers:
    square = DescSquare()
    cube = DescCube()

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube


X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)


class Powers(object):
    """使用__getattr__访问拦截并计算属性"""

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cube ** 3
        else:
            raise TypeError('unknown attr: ' + name)

    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        else:
            self.__dict__[name] = value


X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)


class Powers(object):
    """使用__getattribute__拦截并计算属性"""

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattribute__(self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        else:
            self.__dict__[name] = value


X = Powers(3, 4)
print(X.square)
print(X.cube)