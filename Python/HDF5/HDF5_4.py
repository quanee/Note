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

'''
分块存储
指定最适合访问模式的N维形状
当写入磁盘时 HDF5将数据分成指定形状的块 然后扁平的写入磁盘 其坐标有一个B树索引
'''

dset = f.create_dataset('chunked', (100, 480, 640), dtype='i1', chunks=(1, 64, 64))
print(dset.chunks)

# 设置分块形状
# 自动分块
dset = f.create_dataset("Image", (100, 480, 640), 'f', chunks=True)
print(dset.chunks)

'''
手动选择形状
 *  只有使用连续存储或自动分块会导致性能不佳时才手动选择分块形状