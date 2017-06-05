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