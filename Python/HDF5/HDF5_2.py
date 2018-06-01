import h5py


f = h5py.File("name.hdf5")
f.close()

'''
f = h5py.File("name.hdf5", "w")  # 创建或覆盖文件
f = h5py.File("name.hdf5", "r")  # 只读打开(文件已存在)
f = h5py.File("name.hdf5", "r+")  # 读写打开(文件已存在)
f = h5py.File("name.hdf5", "a")  # 读写打开(不存在则创建)
f = h5py.File("name.hdf5", "w-")  # 防止覆盖(存在则打开失败)
'''

with h5py.File("name.hdf5", "w") as f:
    print(f)

print(f)

'''
文件驱动
    core驱动: 将整个文件保存在内存中, 能存储的数据量有限, 超快速的读写
            f = h5py.File("name.hdf5", driver="core")
            在磁盘上创建一个"备份存储", 当内存文件映像关闭时, 其内容保存到磁盘上