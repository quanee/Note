
L = [1, 2, 3, 'abc']

# if type(L) == type([]):
#     print('list')

# if type(L) == list:
#     print('list')

# if isinstance(L, list):
#     print('list')

# 引用VS拷贝
X = [1, 2, 3]
L = ['a', X, 'b']
D = {'x': X, 'y': 2}

X[1] = 'surprise'

print(L)
print(D)

# 拷贝的实现方法(顶层复制)
# 序列 无条件值分片L[:]
# 字典 X.copy()
# 内置函数 list(L)
# copy标准库

# 深度拷贝
# copy.deepcopy(Y)

L = [4, 5, 6]
X = L * 4
Y = [L] * 4

print(X)