import h5py
import numpy as np
from timeit import timeit
'''分块和压缩'''



# 一个包含100张640x480的灰阶图像的数据集
f = h5py.File("imagetest.hdf5")
dset = f.create_dataset("Images", (100, 480, 640), dtype='uint8')
image = dset[0, :, :]
print(image.shape)
# 数据以640字节分块存储(和数据集最后一维长度相符)读取第一张图像是, 从磁盘读取480个这样的块
# 处理磁盘数据的原则: 位置原则:如果数据被存储在一起, 通常读起来更快

# 读取一张图像角落上64x64的像素块
tile = dset[0, 0:64, 0:64]
print(tile.shape)