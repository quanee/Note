'''装饰器'''

# 函数装饰器在函数定义时进行名称重绑定,提供一个逻辑层来管理函数和方法或随后对它们的调用
# 类装饰器在类定义时进行名称重绑定,提供一个逻辑层来管理类,或管理随后调用它们所建的实例

# 管理调用和实例
# 函数装饰器安装包装器对象,以在需要的时候拦截随后的函数调用并处理它们
# 类装饰器安装包装器对象,以在需要的时候拦截随后的实例创建调用并处理它们


def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            print(name)
            return getattr(self.wrapped, name)
    return Wrapper

@decorator
class C:
    def __init__(self, x, y):
        self.attr = 'spam'


x = C(6, 7)
print(x.attr)


# 函数装饰器
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
    print(a + b + c)


print('#' * 50)
spam(1, 2, 3)
spam('a', 'b', 'c')
print(spam.calls)  # spam实际为tracer类的一个实例


'''类实例属性'''
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args, **kwargs)


@tracer
def spam(a, b, c):
    print(a + b + c)


@tracer
def eggs(x, y):
    print(x ** y)


spam(1, 2, 3)
spam(a=4, b=5, c=6)

eggs(2, 16)
eggs(4, y=4)


'''使用嵌套函数来装饰方法'''
def tracer(func):
    calls = 0

    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))

        return func(*args, **kwargs)
    return onCall


@tracer
def spam(a, b, c):
    print(a + b + c)


print('#' * 50)
spam(1, 2, 3)
spam(a=4, b=5, c=6)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]


print('methods...')
bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(sue.pay)
print(bob.lastName(), sue.lastName())


'''使用描述符装饰方法'''
# 装饰的函数只调用其__call__
# 装饰的方法首先调用__get__来解析方法名获取; __get__返回的对象保持主体类实例并且随后调用以完成调用表达式, 由此触发__call__

class tracer(object):
    def __init__(self, func):
        print(0)
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        print(4)
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        print(1)
        return wrapper(self, instance)


class wrapper:
    def __init__(self, desc, subj):
        print(2)
        self.desc = desc
        self.subj = subj

    def __call__(self, *args, **kwargs):
        print(3)
        return self.desc(self.subj, *args, **kwargs)


@tracer
def spam(a, b, c):
    print(a + b + c)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]


print('#' * 50)
spam(1, 2, 3)
spam(a=4, b=5, c=6)

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(sue.pay)
print(bob.lastName(), sue.lastName())


'''计时调用'''
import time

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kwargs):
        start = time.clock()
        result = self.func(*args, **kwargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result


@timer
def listcomp(N):
    return [x * 2 for x in range(N)]


@timer
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))


result = listcomp(5)
listcomp(50000)
listcomp(500000)
listcomp(1000000)
print(result)
print('allTime = %s' % listcomp.alltime)
print('')
result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print('allTime = %s' % mapcall.alltime)

print('map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))


def timer(label='', trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.clock()
            result = self.func(*args, **kwargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                formats = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(formats % values)
            return result
    return Timer


@timer(label='[CCC]==>')
def listcomp(N):
    return [x * 2 for x in range(N)]


@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))


for func in (listcomp, mapcall):
    print('')
    result = func(5)
    func(50000)
    func(500000)
    func(1000000)
    print(result)
    print('allTime = %s' % func.alltime)

print('map/comp=%s' % round(mapcall.alltime / listcomp.alltime, 3))



'''类装饰器'''
instance = {}
def getInstance(aClass, *args):
    if aClass not in instance:
        instance[aClass] = aClass(*args)
    return instance[aClass]


def singleton(aClass):
    def onCall(*args):
        return getInstance(aClass, *args)
    return onCall


@singleton
class Person(object):
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


@singleton
class Spam(object):
    def __init__(self, val):
        self.attr = val


bob = Person('Bob', 40, 10)
print(bob.name, bob.pay())

sue = Person('Sue', 50, 20)
print(sue.name, sue.pay())

X = Spam(42)
Y = Spam(99)
print(X.attr, Y.attr)


'''跟踪对象接口'''
def Tracer(aClass):
    class Wrapper:
        def __init__(self, *args, **kargs):
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)

        def __getattr__(self, attrname):
            print('Trace: ' + attrname)
            self.fetches += 1
            return getattr(self.wrapped, attrname)

    return Wrapper


@Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)


@Tracer
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


food = Spam()
food.display()
print([food.fetches])

bob = Person('Bob', 40, 50)
print(bob.name)
print(bob.pay())
print('')
sue = Person('Sue', rate=100, hours=60)
print(sue.name)
print(sue.pay())

print(bob.name)
print(bob.pay())
print([bob.fetches, sue.fetches])


'''类错误: 保持多个实例'''
class Tracer(object):
    def __init__(self, aClass):
        self.aClass = aClass

    def __call__(self, *args):
        self.wrapped = self.aClass(*args)
        return self

    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)


@Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)


@Tracer
class Person:
    def __init__(self, name):
        self.name = name


food = Spam()
food.display()

# 只保存一个实例
bob = Person('Bob')
print(bob.name)
# 覆盖bob
Sue = Person('Sue')
print(sue.name)
# 只保存最后一个实例 (解决 放弃基于类的装饰器)
print(bob.name)


'''
定义一个装饰器,既应用于函数也应用于类,把对象添加到一个基于字典的注册中
返回对象本身而不是一个包装器,没有拦截随后的调用
'''
registry = {}
def register(obj):
    registry[obj.__name__] = obj
    return obj


@register
def spam(x):
    return (x ** 2)


@register
def ham(x):
    return (x ** 3)


@register
class Eggs:
    def __init__(self, x):
        self.data = x ** 4

    def __str__(self):
        return str(self.data)


print('Registry:')
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))

print('\nManual calls:')
print(spam(2))