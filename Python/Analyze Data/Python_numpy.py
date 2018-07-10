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

# 查看ndarray数据类型
print(set(np.typeDict.values()))

# 结构数组
goodslist = np.dtype([('name', np.str_, 50), ('location', np.str_, 30), ('price', np.float16), ('volume', np.int32)])

goods = np.array([('Gree Airconditioner', 'JD.com', 6245, 1),
                  ('Sony Blueray Player', 'Amazon,com', 3210, 2),
                  ('Apple Mackbook Pro 13', 'Tmall.com', 12388, 5),
                  ('iPhoneSE', 'JD.com', 4588, 2)], dtype=goodslist)

print(goods)

# 使用字典定义结果数组
goodsdict = np.dtype({'names': ['name', 'location', 'price', 'volume'], 'formats': ['S50', 'S30', 'f', 'i']})

goods_new = np.array([('Gree Airconditioner', 'JD.com', 6245, 1),
                      ('Sony Blueray Player', 'Amazon,com', 3210, 2),
                      ('Apple Mackbook Pro 13', 'Tmall.com', 12388, 5),
                      ('iPhoneSE', 'JD.com', 4588, 2)], dtype=goodsdict)

print(goods_new)


# 索引与切片

# ":"分割起止位置与间隔 ","表示不同维度 "..."遍历剩余维度
a = np.arange(1, 20, 2)

print(a)
print(a[3])
print(a[1:4])
print(a[:2])
print(a[-2])
print(a[::-1])

b = np.arange(24).reshape(2, 3, 4)
print(b)
print(b.shape)
print(b[1, 1, 2])
print(b[0, 2, :])
print(b[0, 2])
print(b[0, ...])
print(b[0])
print(b[:, 1])
print(b[:, :, 1])
print(b[..., 1])
print(b[0, ::2, -2])
print(goods['name'])
print(goods[3])
print(goods[3]['name'])
print(sum(goods['volume']))

# 逻辑索引(布尔索引 条件索引)
print(b[b >= 15])
print(b[~(b >= 15)])
# 逻辑运算符and, or, 在布尔数组中无效
print(b[(b >= 5) & (b <= 15)])
b_bool1 = np.array([False, True], dtype=bool)
print(b[b_bool1])
b_bool2 = np.array([False, True, True], dtype=bool)
b_bool3 = np.array([False, True, True, False], dtype=bool)
print(b[b_bool1, b_bool2])
print(b[b_bool1, b_bool2, b_bool3])

# 花式索引
print(b[[[0], [1, 2], [2, 3]]])
# ix_函数将若干一维整数数组转换为一个用于选取矩形区域的索引器
print(b[np.ix_([1, 0])])
print(b[np.ix_([1, 0], [2, 1])])
print(b[np.ix_([1, 0], [2, 1], [0, 3, 2])])

'''
数组切片是原始数组的视图, 与原始数组共享同一块数据存储空间
'''
b_slice = b[0, 1, 1:3]
b_copy = b[0, 1, 1:3].copy()
print(b_slice)
print(b_copy)
b_slice[1] = 666
print(b_slice)
print(b)
b_copy[1] = 999
print(b_copy)
print(b)

# 数组属性
ac = np.arange(12)
ac.shape = (2, 2, 3)
print(ac)
# 数组形状
print(ac.shape)
# 数组各元素类型
print(ac.dtype)
# 数组维数
print(ac.ndim)
# 数组元素总个数
print(ac.size)
# 数组元素在内存中所占字节数
print(ac.itemsize)
# 数组元素所占存储空间(size与itemsize)
print(ac.nbytes)
# 转置数组
print(ac.T)
# 数组扁平迭代器(像遍历一维数组一样去遍历任意多维数组)
print(ac.flat)

# 数组排序
s = np.array([1, 2, 4, 3, 1, 2, 2, 4, 6, 7, 2, 4, 8, 4, 5])
# 返回排序后的数组
print(np.sort(s))
# 返回数组排序后的下标
print(np.argsort(s))
# 降序排序
print(s[np.argsort(-s)])
# 就地排序
s.sort()
print(s)

# 多维数组排序
s_r = np.array([3, 23, 52, 34, 52, 3, 6, 645, 34, 7, 85, 23]).reshape(6, 2)
print(s_r)
s_r.sort(axis=1)
print(s_r)
s_r.sort(axis=0)
print(s_r)
s_r.sort(axis=-1)
print(s_r)

# 指定排序顺序
a = [1, 5, 1, 4, 3, 4, 4]
b = [9, 4, 0, 4, 0, 2, 1]
# 先按a排序 再按b排序
ind = np.lexsort((b, a))
print([(a[i], b[i]) for i in ind])


# 数组维度
# 展平
b = np.arange(24).reshape(2, 3, 4)
print(b)
print(b.ndim)
# 展平为一维数组(返回视图)
br = np.ravel(b)
print(br)
print(br.ndim)
# reshape函数也可以达到相同效果, 但维度不变
brsh = b.reshape(1, 1, 24)
print(brsh)
print(brsh.ndim)
# 展平为一维数组(返回新对象, 分配内存)
print(b.flatten())

# 维度改变
# 返回视图
bd = b.reshape(4, 6)
print(bd)
b.shape = (1, 1, 24)
print(b)
# 直接修改数组
b.resize(1, 1, 24)
print(b)

# 转置
b.shape = (3, 4, 2)
print(b)
# 等价于 b.T
print(np.transpose(b))

# 数组组合
# 水平组合
a = np.arange(9).reshape(3, 3)
print(a)
b = np.array([[0, 11, 22, 33], [44, 55, 66, 77], [88, 00, 00, 11]])
print(b)