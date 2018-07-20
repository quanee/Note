
# 计算嵌套子列表结构中所有数字的总和
def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot


L = [1, [2, 3, [4, 5]]]
print(sumtree(L))


def make(label):
    def echo(message):
        print(label + ':' + message)

    return echo


F = make('moon')
F('boss')


# 函数内省
print(make.__name__)
print(dir(make.__name__))
print(make.__code__)
print(dir(make.__code__))
print(make.__code__.co_varnames)
print(make.__code__.co_argcount)

# 向函数添加自定义属性
make.count = 0
make.count += 1
print(make.count)

make.handles = 'Button-Press'
print(make.handles)
print(dir(make))


# 函数注解
def func(a: 'moon', b: (1, 10), c: float) -> int:
    return a + b + c


print(func(1, 2, 3))
print(func.__annotations__)

for arg in func.__annotations__:
    print(arg, '=>', func.__annotations__[arg])


def func(a: 'moon', b, c: 99):
    return a + b + c


print(func(1, 2, 3))
print(func.__annotations__)


for arg in func.__annotations__:
    print(arg, '=>', func.__annotations__[arg])


# 参数:注解 = 默认值