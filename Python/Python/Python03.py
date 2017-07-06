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