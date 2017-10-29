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
    global ntraces
    dset2[ntraces, :] = arr
    ntraces += 1


def done():
    dset2.resize((ntraces, 1000))


def setup():
    global data, N, dset1, dset2, ntraces
    data = np.random.random(1000)
    N = 10000
    dset1.resize((1, 1000))
    dset2.resize((10001, 1000))
    ntraces = 0


def test1():
    for idx in range(N):
        add_trace_1(data)


def test2():
    for idx in range(N):
        add_trace_2(data)


print(dset1.chunks)
print(dset2.chunks)

# print(timeit(test1, setup=setup, number=1))
# print(timeit(test2, setup=setup, number=1))


# 过滤器和压缩
# 压缩过滤器
dset = f.create_dataset('BigDataset', (1000, 1000), dtype='float64', compression='gzip', compression_opts=9)
# compression_opts 压缩级别 0-9 越大压缩率越高
print(dset.compression)
dset[...] = 42.0
print(dset[0, 0])
print(dset.compression_opts)
print(dset.chunks)

'''
szip压缩器
NASA专利压缩技术
  仅支持(1, 2, 4, 8字节, 有/无符号)整型和浮点(4/8字节)类型
  快速压缩解压
'''
# dset = f.create_dataset('BigDataset', (1000, 1000), dtype='float64', compression='szip')

'''
LZF压缩器
  支持HDF5所有类型
  超快的压缩和解压
  仅可用于Python C代码开源
'''
# dset = f.create_dataset('BigDataset', (1000, 1000), dtype='float64', compression='lzf')

'''
shuffle过滤器
    将数据重新分块打包 提高压缩率
    所有HDF5发行版可用
    超快
    仅可与GZIP或LZF等过滤器共同使用
'''
dset = f.create_dataset('BigDatasets', (1000, 1000), dtype='float64', compression='gzip', shuffle=True)
dset[...] = 50.0
print(dset.shuffle)

'''
FLETCHER32过滤器 (校验和过滤器 弗莱彻校验的32位实现)
    每个分块被写入文件时计算一个校验和保存在分块的元数据中
    读取时 再次计算并比对校验和 如果不匹配 会抛出一个错误 读取失败
    所有HDF5发行版可用
    很快
    兼容所有无损过滤器
'''
dset = f.create_dataset('Data', (1000, ), fletcher32=True)