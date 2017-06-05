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

