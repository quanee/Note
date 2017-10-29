import h5py
import numpy as np
from timeit import timeit
'''分块和压缩'''



# 一个包含100张640x480的灰阶图像的数据集
f = h5py.File("imagetest.hdf5")