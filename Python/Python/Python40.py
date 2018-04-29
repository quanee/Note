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

# 允许重复元素的组合
x = itertools.combinations_with_replacement('ABC', 2)
print(list(x))

# 按照真值表筛选元素
x = itertools.compress(range(5), (True, False, True, True, False))
print(list(x))

# 计数器,可以指定起始位置和步长