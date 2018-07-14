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


grp.move('dataset', 'new_dataset_name')
dset2 = grp.create_dataset('dataset', (50, ))
print(f['softlink'] == dset)
# 只识别名字
print(f['softlink'] == dset2)

# 软链接在创建时不会检查
f['broken'] = h5py.SoftLink('/some/nonexistent/object')
# print(f['broken'])  # KeyError: 'Unable to open object (component not found)'

# 外部链接
with h5py.File('file_with_resource.hdf5', 'w') as f1:
    f1.create_group('mygroup')
f1.close()

f2 = h5py.File('linking_file.hdf5', 'w')
f2['linkname'] = h5py.ExternalLink('file_with_resource.hdf5', 'mygroup')

grp = f2['linkname']
print(grp.name)
print(grp.file)
print(f2)

# .parent指向外部文件根组
print(f2['/linkname'].parent == f2['/'])
# 创建时检查文件和对象名 3.X貌似不检查
f2['anotherlink'] = h5py.ExternalLink('missing.hdf5', '/')

# 对象名字注解
grp = f.create_group(u'e_with_accent_\u00E9')
print(grp.name)
f.close()

# 用get决定对象类型
f = h5py.File('get_demo.hdf5', 'w')
f.create_group('subgroup')
f.create_dataset('dataset', (100, ))

for name in f:
    print(name, f.get(name, getclass=True))


f['softlink'] = h5py.SoftLink('/subgroup')
with h5py.File('get_demo_ext.hdf5', 'w') as f2:
    f2.create_group('egroup')

f['extlink'] = h5py.ExternalLink('get_demo_ext.hdf5', '/egroup')

for name in f:
    print(name, f.get(name, getlink=True))

for name in f:
    print(name, f.get(name, getclass=True, getlink=True))
f.close()
# require
# h5py不能直接重写组内成员
f = h5py.File('require_demo.hdf5', 'w')
f.create_group('x')
f.create_group('y')
del f['y']
f['y'] = f['x']

# require版本会检查组或数据集是否存在,若存在则直接返回该对象
# require版本会额外检查形状和类型是否和已存在的数据集一致(不一致则抛出异常)
f.require_dataset('dataset', (100, ), dtype='int64')
# 异常
# f.require_dataset('dataset', (100, ), dtype='float64')
# 使用numpy转换规则检查
f.require_dataset('dataset', (100, ), dtype='int32')

# 迭代和容器
'''
在HDF5文件中, 组成员以B树的数据结构索引
'''
f = h5py.File('iterationdemo.hdf5', 'w')
f.create_group('1')
f.create_group('2')
f.create_group('10')
f.create_dataset('data', (100, ))
print([x for x in f.keys()])
print([x for x in f])
print([x for x in f.values()])
print([(x, y) for x, y in f.items()])

# 测试存在性