import h5py
import numpy as np


# 对象引用
# 创建
f = h5py.File('refs_demo.hdf5', 'w')
grp1 = f.create_group('group1')