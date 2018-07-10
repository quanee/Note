import numpy as np


v = np.arange(10)
print(v)
print(v.dtype)
print(v.shape)

# 返回列表
vstep = np.arange(0, 10, 0.5)
print(vstep)
print(vstep * 10)

# 等差数列 初始值1 终止值19 元素个数为10
print(np.linspace(1, 19, 10))

# 等比数列
from math import e
print(np.logspace(1, 20, 10, endpoint=False, base=e))

# 创建全0整型向量
print(np.zeros(10, np.int))
print(np.empty(10, np.int))

# 创建随机数向量
print(np.random.randn(10))


s = 'Hello, Python!'
print(np.fromstring(s, dtype=np.int8))


def multiply99(i, j):
    return (i + 1) * (j + 1)


print(np.fromfunction(multiply99, (9, 9)))


# 数组
a = np.array([np.arange(3), np.arange(3)])
print(a)
print(a.shape)  # 形状
print(a.ndim)  # 维度

# 单位矩阵
print(np.identity(9).astype(np.int8))
print(a.tolist())
print(type(a.tolist()))
