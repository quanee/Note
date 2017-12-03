import h5py
import numpy as np

# 定长字符串
f = h5py.File('typesdemo.hdf5')
dt = np.dtype('S10')
dset = f.create_dataset('fixed_string', (100, ), dtype=dt)
dset[0] = 'Hello'.encode()
print(dset[0])
# 超出长度部分截断
dset[0] = 'aksdjfhaksdfjhasdfjahsdkfjhasdk'.encode()
print(dset[0])

dt = np.dtype('S3')
a = np.array(['a', 'ab', 'abc', 'abcd'], dtype=dt)
print(a)

dt = h5py.special_dtype(vlen=str)
print(repr(dt))
print(dt.kind)

dset = f.create_dataset('vlen_dataset', (100, ), dtype=dt)
dset[0] = 'Hello'
dset[1] = np.string_('Hello2')
dset[3] = 'X' * 10000

# 读取一个元素时 返回str
out = dset[0]
print(type(out))

# 读取多个元素时 返回object
print(dset[0:2])
out = dset[0:1]
print(out.dtype)

