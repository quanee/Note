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

f.move('mydata2', 'mydata3')
out = f[grp1.attrs['dataset']]
print(out == dset)

# 引用是一种数据类型
dt = h5py.special_dtype(ref=h5py.Reference)
print(repr(dt))
print(dt.kind)

ref_dset = f.create_dataset('references', (10, ), dtype=dt)
out = ref_dset[0]
print(out)

print(bool(out))
print(bool(grp1.ref))