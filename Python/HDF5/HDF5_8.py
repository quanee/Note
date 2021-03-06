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

# 区域引用
# 创建
print(dset.name)
print(dset.shape)
print(dset.regionref)

ref_out = dset.regionref[10: 90]
print(ref_out)

# dset.regionref.shape(ref_out)(100, )
# dset.regionref.selechion(ref_out)(80, )
# data = dset[ref_out]
# print(data)

# 复杂索引
dset_random = f.create_dataset('small_example', (3, 3))
dset_random[...] = np.random.random((3, 3))
print(dset_random[...])

index_arr = dset_random[...]
print(index_arr)

# random_ref = dset_random.regionref[index_arr]
# print(dset_random.regionref.selection(random_ref))

# 维度标尺
dset = f.create_dataset('temperatures', (100, 100, 100), dtype='f')
dset.attrs['temp_units'] = 'C'
dset.attrs['steps'] = [10000, 10000, 100]
dset.attrs['axes'] = ['x'.encode(), 'y'.encode(), 'z'.encode()]

# 创建维度标尺
# 删除特征
for name in dset.attrs:
    del dset.attrs[name]


print(dset.dims)
f.create_dataset('scale_x', data=np.arange(100) * 10e3)
f.create_dataset('scale_y', data=np.arange(100) * 10e3)
f.create_dataset('scale_z', data=np.arange(100) * 100)

dset.dims.create_scale(f['scale_x'], 'Simulation X (North) axis')
dset.dims.create_scale(f['scale_y'], 'Simulation Y (East) axis')
dset.dims.create_scale(f['scale_z'], 'Simulation Z (Vertical) axis')

for key, val in f['scale_x'].attrs.items():
    print(key, ':', val)


# 在数据集上添加标尺
dset.dims[0].attach_scale(f['scale_x'])
dset.dims[1].attach_scale(f['scale_y'])
dset.dims[2].attach_scale(f['scale_z'])


print(dset.dims[0][0])
print(dset.dims[0][0][...])

print(dset.dims[0]['Simulation X (North) axis'])

# 给数据集坐标轴打标签
dset.dims[0].label = 'x'
dset.dims[1].label = 'y'
dset.dims[2].label = 'z'





