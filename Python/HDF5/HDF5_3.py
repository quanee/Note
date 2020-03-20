import numpy as np
import h5py
'''数据集'''

f = h5py.File("testfile.hdf5", "w")
arr = np.ones((5, 2))
f["my dataset"] = arr
dset = f["my dataset"]
print(dset)

# 类型和形状
print(dset.dtype)
print(dset.shape)

# 读和写
out = dset[...]
print(out)
print(type(out))

# 局部更新
dset[1:4, 1] = 2.0
print(dset[...])

# 创建空数据集
dset = f.create_dataset("test1", (10, 10))
print(dset)
dset = f.create_dataset("test2", (10, 10), dtype=np.complex)
print(dset)

# 创建一个一维数据集能够装下4GB数据
dset = f.create_dataset("big dataset", (1024**3, ), dtype=np.float32)
dset[0:1024] = np.arange(1024)
f.flush()
f.close()

bigdata = np.ones((100, 1000))
print(bigdata.dtype)
print(bigdata.shape)

with h5py.File('big1.hdf5', 'w') as f1:
    f1['big'] = bigdata

with h5py.File('big2.hdf5', 'w') as f2:
    f2.create_dataset('big', data=bigdata, dtype=np.float32)

f1 = h5py.File('big1.hdf5')
f2 = h5py.File('big2.hdf5')
print(f1['big'].dtype)
print(f2['big'].dtype)

# 自动类型转换和直读
dset = f2['big']
print(dset.dtype)  # float32
print(dset.shape)
# 创建双精度数组
big_out = np.empty((100, 1000), dtype=np.float64)
# 将数据直接读入输出数组 不需要转换
dset.read_direct(big_out)

# 用astype读
with dset.astype('float64'):
    out = dset[0, :]

print(out.dtype)

# 转换成'较小'的类型时对值进行取整或'截断'
f = h5py.File("testfile.hdf5", "w")
f.create_dataset('x', data=1e256, dtype=np.float64)
print(f['x'][...])

f.create_dataset('y', data=1e256, dtype=np.float32)
print(f['y'][...])

# 改变形状
'''
imagedata.shape
(100, 480, 640)
f.create_dataset('newshape', data=imagedata, shape=(100, 2, 240, 640))
'''

# 默认填充值
dset = f.create_dataset('empty', (2, 2), dtype=np.int32)
print(dset[...])

dset = f.create_dataset('filled', (2, 2), dtype=np.int32, fillvalue=42)
print(dset[...])
print(dset.fillvalue)

# 读写数据
# 高效率切片
dset = f2['big']
print(dset)
# 切片
out = dset[0:10, 20: 70]
print(out.shape)
'''
切片操作细节
        1. h5py计算结果数组对象形状是(10, 50)
        2. 分配一个空的Numpy数组 形状为(10, 50)
        3. HDF5选出数据集中相应部分
        4. HDF5将数据集中的数据复制给空的numpy数组
        5. 返回填充好的NumPy数组
'''

# 选择合理的切片大小
for ix in range(100):
    for iy in range(1000):
        val = dset[ix, iy]
        if val < 0:
            dset[ix, iy] = 0
# 进行100000次切片操作

for ix in range(100):
    val = dset[ix, :]
    val[val < 0] = 0
    dset[ix, :] = val
# 进行100次切片操作


'''
Some_dset[0:10, 20:70] = out*2
产生步骤:
        1. h5py计算切片大小并检查是否跟输入的数组大小匹配
        2. HDF5选出数据集中相应的部分
        3. HDF5从输入数组读取并写入文件
'''
# start-stop-step索引
dset = f.create_dataset('range', data=np.arange(10))
print(dset[...])
print(dset[4])
print(dset[4:8])

a = np.arange(10)
print(a)
print(a[::-1])

# h5py不支持数组翻转

# 多维切片和标量切片
# ... Ellipsis 指定不想特别指定的维度
dset = f.create_dataset('4d', shape=(100, 80, 50, 20))
print(dset[0, ..., 0].shape)
print(dset[...].shape)

dset = f.create_dataset('1d', shape=(1, ), data=42)
print(dset.shape)
print(dset[0])  # 返回元素本身
print(dset[...])  # Ellipsis返回一个具有一个1个元素的数组

dset = f.create_dataset('0d', data=42)
print(dset.shape)
print(dset[...])
print(dset[()])
'''
Ellipsis获取数据集中的所有元素, 结果永远是一个数组
'()'获取数据集中的所有元素, 对于1维或更高维数据集, 结果是一个数组, 0维则是一个标量
'''

# 布尔索引
'''
val[val < 0] = 0
布尔数组索引 如果val是一个NumPy整型数组, 表达式val<0的结果是一个布尔数组
           当val中相应元素为负是为True, 否则为False (数据筛选)
    当布尔数组索引中的元素为True时, 数据集中对应的元素被选中
'''

# 创建一个-1到1之间平均分布的随机数组
data = np.random.random(10) * 2 - 1
print(data)

# 用布尔数组将负值截断为0
data[data < 0] = 0
print(data[...])

data = np.random.random(10) * 2 - 1
print(data)
# 将负值转正
data[data < 0] = -1 * data[data < 0]
print(data[...])


# 坐标列表
dset = f['range']
print(dset[...])

print(dset[[1, 2, 7]])

# 自动广播
dset = f2['big']
print(dset.shape)

# 复制dset[0, :]的记录并覆盖所有其他值
data = dset[0, :]
for idx in range(100):
    dset[idx, :] = data

print(dset.shape)
print(dset[...])

# h5py内建的广播功能
dset[:, :] = dset[0, :]
print(dset.shape)
print(dset[...])

f.close()
f = h5py.File("testfile.hdf5", "w")

# 直读入一个已存在的数组
print(dset.dtype)
out = np.empty((100, 1000), dtype=np.float64)
dset.read_direct(out)
# 需要一次性读取整个数据集

dset.read_direct(out, source_sel=np.s_[0, :], dest_sel=np.s_[50, :])
# np.s_ 以一个数组切片格式为参数 将相应记录在numpy的一个slice对象 并返回这个对象

# 标准切片技术
out = dset[:, 0:50]
print(out.shape)
means = out.mean(axis=1)
print(means.shape)

# 使用read_direct
out = np.empty((100, 50), dtype=np.float32)
dset.read_direct(out, np.s_[:, 0:50])
means = out.mean(axis=1)

dset = f.create_dataset('perftest', (10000, 10000), dtype=np.float32)
dset[:] = np.random.random(10000)

def time_simple():
    dset[:, 0:500].mean(axis=1)


out = np.empty((10000, 500), dtype=np.float32)


def time_direct():
    dset.read_direct(out, np.s_[:, 0:500])
    out.mean(axis=1)


from timeit import timeit
print(timeit(time_simple, number=100))
print(timeit(time_direct, number=100))
f.close()
f = h5py.File("testfile.hdf5", "w")

# 数据类型注解
a = np.ones((1000, 1000), dtype='<f4')  # little-endian
b = np.ones((1000, 1000), dtype='>f4')  # big-endian

print(timeit(a.mean, number=1000))
print(timeit(b.mean, number=1000))

c = b.view('float32')
c[:] = b
b = c
print(timeit(b.mean, number=1000))

# 改变数据集形状
# 创建可变形数据集
dset = f.create_dataset('resizeable', (2, 2), maxshape=(2, 2))
print(dset.shape)
print(dset.maxshape)
# 改变形状
dset.resize((1, 1))
print(dset.shape)
dset.resize((2, 2))
print(dset.shape)

# 无线维度 None
dset = f.create_dataset('unlimited', (2, 2), maxshape=(2, None))
print(dset.shape)
print(dset.maxshape)
dset.resize((2, 3))
print(dset.shape)
dset.resize((2, 2**30))
print(dset.shape)
# 无论maxshape参数为何 不能改变维度个数 即数据集阶数是固定的 永远不能改变

# 用resize重新组织数据
a = np.array([[1, 2], [3, 4]])
print(a.shape)
print(a)
# 数据重新组织
a.resize((1, 4))
print(a)

dset = f.create_dataset('sizetest', (2, 2), dtype=np.int32, maxshape=(None, None))
dset[...] = [[1, 2], [3, 4]]
print(dset[...])
# 数据不会重新组织 而是丢掉
dset.resize((1, 4))
print(dset[...])
dset.resize((1, 10))
print(dset[...])

# 何时以及如何进行resize
# 方案一 (每次新增一条数据时, 扩展一条记录 )
dset1 = f.create_dataset('timetraces', (1, 1000), maxshape=(None, 1000))

def add_trace_1(arr):
    dset1.resize((dset.shape[0] + 1, 1000))
    dset1[-1, :] = arr


# 方案二 (记住插入的次数并在结束时'削减'数据集)
dset2 = f.create_dataset('timetraces2', (5000, 1000), maxshape=(None, 1000))

ntraces = 0
def add_trace_2(arr):
    global ntraces
    dset2[ntraces, :] = arr
    ntraces += 1


def done():
    dset2.resize((ntraces, 1000))


























import os
f.close()
f1.close()
f2.close()
os.remove('./testfile.hdf5')