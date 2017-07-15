import h5py
import numpy as np



f = h5py.File('attrsdemo.hdf5', 'w')
dset = f.create_dataset('dataset', (100, ))
print(dset.attrs)
dset.attrs['title'] = 'Dataset from third round of experiments'
dset.attrs['sample_rate'] = 100e6