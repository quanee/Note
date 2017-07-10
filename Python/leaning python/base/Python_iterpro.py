
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


print(M[1])
print(M[1][2])

print([row[1] for row in M])
print([M[row][1] for row in (0, 1, 2)])
print([M[i][i] for i in range(len(M))])

print([M[row][col] * N[row][col] for row in range(3) for col in range(3)])
print([[M[row][col] * N[row][col] for col in range(3)] for row in range(3)])


# 生成器
def gen():
    for i in range(10):
        X = yield i
        print(X)


G = gen()
print(next(G))  # send(None)
print(G.send(77))
print(G.send(88))


# 生成器 VS 列表解析
# 列表解析
print([x ** 2 for x in range(4)])
# 生成器表达式
print((x ** 2 for x in range(4)))

G = (x ** 2 for x in range(4))
print(next(G))
print(next(G))
print(next(G))

print(sum(x ** 2 for x in range(4)))
print(sorted(x ** 2 for x in range(4)))
print(sorted((x ** 2 for x in range(4)), reverse=True))


# 生成器函数 VS 生成器表达式
G = (c * 4 for c in 'MOON')
print(list(G))


def timesfour(S):