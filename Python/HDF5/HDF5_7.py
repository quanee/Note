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