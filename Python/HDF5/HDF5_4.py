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
 *  为数据集指定最自然的访问方式
 *  分块不要太小(至少大于10KB)
 *  分块不要太大(至少小于1MB)
'''
# 可变性数据集
# 手动指定分块
dset1 = f.create_dataset('timetraces1', (1, 1000), maxshape=(None, 1000), chunks=(1, 1000))
dset2 = f.create_dataset('timetraces2', (5000, 1000), maxshape=(None, 1000), chunks=(1, 1000))

# 方法一 (简单添加)
def add_trace_1(arr):
    dset1.resize((dset1.shape[0] + 1, 1000))
    dset1[-1, :] = arr


# 方法二 (超额分配 结束时削减)
ntraces = 0
def add_trace_2(arr):