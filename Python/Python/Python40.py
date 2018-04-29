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
x = itertools.count(start=20, step=-1)
print(list(itertools.islice(x, 0, 10, 1)))

# 循环指定的列表和迭代器
x = itertools.cycle('ABC')
print(list(itertools.islice(x, 0, 10, 1)))

# 按照真值函数丢弃掉列表和迭代器前面的元素
x = itertools.dropwhile(lambda e: e < 5, range(10))
print(list(x))

# 保留对应真值为False的元素
x = itertools.filterfalse(lambda e: e < 5, (1, 5, 3, 6, 9, 4))
print(list(x))

# 按照分组函数的值对元素进行分组
x = itertools.groupby(range(10), lambda x: x < 5 or x > 8)
for condition, numbers in x:
    print(condition, list(numbers))

# 对迭代器进行切片
x = itertools.islice(range(10), 0, 9, 2)
print(list(x))

# 产生指定数目的元素的所有排列(顺序有关)
x = itertools.permutations(range(4), 3)
print(list(x))

# 简单的生成一个拥有指定数目元素的迭代器
x = itertools.repeat(0, 5)
print(list(x))

# 类似map
x = itertools.starmap(str.islower, 'aBCDefGhI')
print(list(x))


# 与dropwhile相反，保留元素直至真值函数值为假。
x = itertools.takewhile(lambda e: e < 5, range(10))
print(list(x))


# 生成指定数目的迭代器
x = itertools.tee(range(10), 2)
for letters in x: