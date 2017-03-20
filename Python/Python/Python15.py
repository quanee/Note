'''反射'''


class Foo(object):
    def __init__(self, name):
        self.name = name

    def show(self):
        return self.name


b = 'name'
obj = Foo('moon')
name = obj.__dict__[b]
print(name)

# 属性
v = getattr(obj, b)
print(v)

# 方法
func = getattr(obj, 'show')
print(func)

s = func()
print(s)

print(hasattr(obj, 'name'))

setattr(obj, 'key', 'value')
print(obj.key)

delattr(obj, 'key')

# 模块
import rf

print(rf.NAME)
print(rf.func())

name = getattr(rf, 'NAME')
print(name)
func = getattr(rf, 'func')
print(func())

cls = getattr(rf, 'Foo')
print(cls)
obj = cls()
print(obj.name)