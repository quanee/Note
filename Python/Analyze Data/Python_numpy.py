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