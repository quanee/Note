from collections import Iterator

# 迭代器 生成器
"""
可迭代(Iterable)
    list, tuple, dict, set, str
    generator, yield function
可迭代对象(isinstance(x, Iterator))
    generator
"""

# 生成器创建方式
# (x for x in range(123)) 列表生成式
# yield

# 列表生成式
a = [x for x in range(10)]

print(a)


def f(n):
    return n ** 2


b = [f(x) for x in range(10)]

print(b)

t = ['123', 8]

a, b = t
print(a[0], b)


# 生成器 需要时生成 不能随机访问
# 生成器都是迭代器 迭代器不一定是生成器
# 生成器在创建时已经决定能生成多少个值
# 生成器方法
s = (x * 2 for x in range(10))
print(s.__next__())  # 特殊方法
print(next(s))  # Python3 内置方法 Python2 s.next()


def fib(max):
    n, before, after = 0, 0, 1
    while n < max:
        print(before)