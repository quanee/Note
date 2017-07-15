import h5py
import numpy as np



f = h5py.File('attrsdemo.hdf5', 'w')
dset = f.create_dataset('dataset', (100, ))
print(dset.attrs)
dset.attrs['title'] = 'Dataset from third round of experiments'
dset.attrs['sample_rate'] = 100e6
dset.attrs['run_id'] = 144
print(dset.attrs['title'])
print(dset.attrs['sample_rate'])
print(dset.attrs['run_id'])
print([x for x in dset.attrs])

dset.attrs['another_id'] = 42
# 改写特征
dset.attrs['another_id'] = 100

print(dset.attrs['another_id'])
# 删除特征
del dset.attrs['another_id']

print([(name, val) for name, val in dset.attrs.items()])

print(dset.attrs.get('run_id'))
print(dset.attrs.get('missing'))

# 类型猜测
print(dset.dtype)
f.flush()
# h5ls -vlr attrsdemo.hdf5
print(np.array(144).dtype)

dset.attrs['ones'] = np.ones((100, ))
print(dset.attrs['ones'])

# try:
#     dset.attrs['ones'] = np.ones((100, 100))
# except Exception:
#     print(Exception)

# print(dset.attrs['ones'])

one_dset = f.create_dataset('one_dset', data=np.ones((100, 100)))
dset.attrs['ones'] = one_dset.ref
print(dset.attrs['ones'])
f.close()

# 显式指定类型
f = h5py.File('attrs_create.hdf5', 'w')
dset = f.create_dataset('dataset', (100, ))
dset.attrs.create('two_byte_int', 190, dtype='i2')
print(dset.attrs['two_byte_int'])
f.flush()

dset.attrs['string'] = ['Hello'.encode(), 'Another string'.encode()]
print(dset.attrs['string'])

# 指定变长字符串
dt = h5py.special_dtype(vlen=str)
dset.attrs.create('more_strings', ['Hello', 'Another string'], dtype=dt)
print(dset.attrs['more_strings'])

dset.attrs.modify('two_byte_int', 33)
print(dset.attrs['two_byte_int'])

f.close()
