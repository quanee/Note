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