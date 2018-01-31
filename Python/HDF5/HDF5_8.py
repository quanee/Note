import h5py
import numpy as np


# 对象引用
# 创建
f = h5py.File('refs_demo.hdf5', 'w')
grp1 = f.create_group('group1')
grp2 = f.create_group('group2')
dset = f.create_dataset('mydata', shape=(100, ))
print(grp1.ref)
out = f[grp1.ref]
print(out == grp1)

# 只能定位本文件内对象
out = grp2[grp1.ref]
print(out == grp2)


grp1.attrs['dataset'] = dset.name
print(grp1.attrs['dataset'])
out = f[grp1.attrs['dataset']]
print(out == dset)
f.move('mydata', 'mydata2')
# out = f[grp1.attrs['dataset']]  # KeyError: "Unable to open object (object 'mydata' doesn't exist)"


grp1.attrs['dataset'] = dset.ref
print(grp1.attrs['dataset'])

out = f[grp1.attrs['dataset']]
print(out == dset)