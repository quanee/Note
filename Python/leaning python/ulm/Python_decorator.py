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