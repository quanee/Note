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
