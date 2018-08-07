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