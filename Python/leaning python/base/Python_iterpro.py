
print(list(map(ord, 'moon')))
print([ord(x) for x in 'moon'])

print([x for x in range(5) if x % 2 == 0])
print(list(filter((lambda x: x % 2 == 0), range(5))))


# 列表嵌套循环
print([x + y for x in [0, 1, 2] for y in [100, 200, 300]])
print([x + y for x in 'moon' for y in 'MOON'])

print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])


# 列表解析和矩阵
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]