import h5py
import numpy as np

# 定长字符串
f = h5py.File('typesdemo.hdf5')
dt = np.dtype('S10')
dset = f.create_dataset('fixed_string', (100, ), dtype=dt)
dset[0] = 'Hello'.encode()