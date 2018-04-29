import itertools
"""返回迭代器对象"""


# 累加
x = itertools.accumulate(range(10))
print(list(x))

# 连接多个列表或迭代器
x = itertools.chain(range(3), range(4), [3, 2, 1])