
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
    for c in S:
        yield c * 4


G = timesfour('moon')
print(list(G))

# 手动迭代
G = (c * 4 for c in 'MOON')
It = iter(G)
print(next(It))
print(next(It))


G = timesfour('moon')
It = iter(G)
print(next(It))
print(next(It))


# 生成器是单迭代对象
G = (c * 4 for c in 'spark')
I1 = iter(G)
print(next(I1))
print(next(I1))

I2 = iter(G)
print(next(I2))
print(next(I2))

# 列表支持多个迭代器
L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)

print(next(I1))
print(next(I1))

print(next(I2))
print(next(I2))


# 生成器模拟map
# yield
def mymap(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)

# (...)
def mymap(func, *seqs):
    return (func(*args) for args in zip(*seqs))


# 生成器模拟zip
def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res


def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res


S1, S2 = 'abc', 'xyz123'
print(myzip(S1, S2))  # [('a', 'x'), ('b', 'y'), ('c', 'z')]
print(mymapPad(S1, S2))  # [('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]
print(mymapPad(S1, S2, pad=99))  # [('a', 'x'), ('b', 'y'), ('c', 'z'), (99, '1'), (99, '2'), (99, '3')]


# 生成器模拟zip
# yield
def myzip(*seqs):
    seqs = [list(S) for S in seqs]

    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)


def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]

    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)


S1, S2 = 'abc', 'xyz123'
print(list(myzip(S1, S2)))  # [('a', 'x'), ('b', 'y'), ('c', 'z')]
print(list(mymapPad(S1, S2)))  # [('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]
print(list(mymapPad(S1, S2, pad=99)))  # [('a', 'x'), ('b', 'y'), ('c', 'z'), (99, '1'), (99, '2'), (99, '3')]
