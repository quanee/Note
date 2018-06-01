import h5py


f = h5py.File("name.hdf5")
f.close()

'''
f = h5py.File("name.hdf5", "w")  # 创建或覆盖文件
f = h5py.File("name.hdf5", "r")  # 只读打开(文件已存在)