import itertools
"""返回迭代器对象"""


# 累加
x = itertools.accumulate(range(10))
print(list(x))

# 连接多个列表或迭代器
x = itertools.chain(range(3), range(4), [3, 2, 1])
print(list(x))

# 求列表或生成器中指定数目的元素不重复的所有组合
x = itertools.combinations(range(4), 3)
print(list(x))