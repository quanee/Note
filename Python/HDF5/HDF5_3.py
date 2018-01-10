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