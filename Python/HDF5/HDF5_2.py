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