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