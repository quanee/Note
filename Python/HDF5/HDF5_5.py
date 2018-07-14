import h5py
'''组, 链接和迭代: HDF5的层次性'''


# 根组和子组
f = h5py.File('Groups.hdf5')
subgroup = f.create_group('SubGroup')
print(subgroup)
print(subgroup.name)

# 组嵌套
subsubgroup = subgroup.create_group('AntoherGroup')
print(subsubgroup.name)

# 指定完整路径 HDF5自动创建所有中间组
out = f.create_group('/some/big/path')
print(out)

# 组的基本原理
# 组几乎就像字典一样工作
f['Dataset1'] = 1.0
f['Dataset2'] = 2.0
f['Dataset3'] = 3.0
subgroup['Dataset4'] = 4.0
# 字典风格的访问
dset1 = f['Dataset1']
dset4 = f['SubGroup/Dataset4']
dset4 = f['SubGroup']['Dataset4']

# print(f['BadName'])  # KeyError: 'Unable to open object (object 'BadName' doesn't exist)'

out = f.get('BadName')
print(out)

# 返回组内直接包含对象数量
print(len(f))
print(len(f['SubGroup']))

f.close()
# 特殊属性
f = h5py.File('propdemo.hdf5', 'w')
grp = f.create_group('hello')
print(grp.file == f)
print(grp.parent)
f.close()

# 硬链接 (将一个链接名字和文件中的对象关联到一起 根据文件位置)
f = h5py.File('linksdemo.hdf5', 'w')
grpx = f.create_group('x')
print(grpx.name)

# 创建链接指向该组
f['y'] = grpx
grpy = f['y']
print(grpx == grpy)
print(grpx.name)
print(grpy.name)

# 删除硬链接
del f['y']
f.close()

# 剩余空间和重新打包
# h5repack bigfile.hdf5 out.hdf5


# 软链接 (在对象内保存指向一个对象的路径 根据名字)
f = h5py.File('test.hdf5', 'w')
grp = f.create_group('mygroup')
dset = grp.create_dataset('dataset', (100, ))

f['hardlink'] = dset
print(f['hardlink'] == grp['dataset'])

# # 数据集重名名
grp.move('dataset', 'new_dataset_name')
print(f['hardlink'] == grp['new_dataset_name'])

grp.move('new_dataset_name', 'dataset')
f['softlink'] = h5py.SoftLink('/mygroup/dataset')
print(f['softlink'] == grp['dataset'])

softlink = h5py.SoftLink('/some/path')
print(softlink)
print(softlink.path)
