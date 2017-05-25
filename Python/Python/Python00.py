# __auther__:pangdahai
# __date__:2017/10/26 22:30:15
import copy

# Python 2.x ASSIC (#!-*- coding:UTF-8 -*-)/(#coding:utf-8)
# Python 3.x unicode

# unicode 兼容GBK,GB
# UTF-8 unicode的扩展

# 单行注释
'''多行注释'''
"""多行注释"""

# 用户输入,所有输入数据都是字符串
# inVal = input("input value:")

name = "pangdahai"
age = 22
job = "student"
salary = 1000

# 格式化字符串 %s占位符

msg = '''
----- info of %s -----
Name:%s
Age:%s
Job:%s
Salary:%s
----- end -----
''' % (name, name, age, job, salary)

print(msg)
print(type(msg))
# True+True=2
print("True+True=", True + True)
# True+False=1
print("True+False=", True + False)
# True=1 False=0

# break 跳出循环
# for循环    开始值 结束值 步长
for i in range(1, 100, 2):
    print(i)
    if i == 3:
        break
# for循环   默认从0开始 步长为1
for i in range(100):
    print(i)
    if i == 2:
        break

# while循环
# continue跳出本次循环
con = 0
while con < 3:
    con += 1
    if con == 2:
        continue
    print("cont")

# 2017/10/27 13:50:30


# 列表
# count(str)统计str出现的次数
li = ['a', 'b', 'c', 'd', 'e', 'a']
print(li.count('a'))

# y.extend(x)将x添加到y后面
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

# m.index(str)获取m中str的索引(从0开始计数)
m = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(m.index('c'))

# 切片
# m[x:]从截取m中第x个以后的元素
n = m[3:]
print(n)
# m[x:y]从截取m中第x个到y的元素(y负数则倒数)
n = m[3:-1]
print(n)
# m[x:y:z]从截取m中x到y的元素,每z个元素取一次(z为负数则从右往左取)
n = m[3:-1:2]
print(n)

# 添加 append insert
m = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# append（value）　　---向列表尾添加项value
m.append('j')  # 返回值为None
print(m)
# count(value)　　---返回列表中值为value的项的个数
print(m.count('a'))
# m.insert(x, 'n')将n插入到m的第x
# insert(i, value) ---向列表i位置插入项vlaue，如果没有i，则添加到列表尾部
m.insert(0, '9')
print(m)
# extend(list2)　　---向列表尾添加列表list2
m.extend(n)
try:
    print(m.index('b'))
except ValueError:
    print("ValueError")

# 修改
m = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# m[x]='n'修改修改m的第x个元素为n
m[0] = '0'
print(m)

# 删除
# 通过值删除元素
# remove(value)　　---删除列表中第一次出现的value，如果列表中没有vlaue，则异常ValueError
m.remove('0')
# 通过索引删除元素
# pop([i])　　---返回i位置项，并从列表中删除；如果不提供参数，则删除最后一个项；如果提供，但是i超出索引范围，则异常IndexError
m.pop(0)    # 返回被删除的元素
del m[0]    # 无返回值
print(m)
del m       # 直接从内存删除变量名

# reverse()　　---列表反转

# index
# index(value, [start, [stop]])　　---返回列表中第一个出现的值为value的索引，如果没有，则异常 ValueError
m = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# 返回元素在列表中的位置
print(m.index('a'))

# reverse 反向排列
m = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
m.reverse()
print(m)
# sort 逆序排序
# sort(cmp=None, key=None, reverse=False)　　---列表排序
m.sort(reverse=True)
print(m)

'''
生成唯一识别码
'''
import time
import os
time = str(hex(int(time.time() * 10000000))[2:])
pid = str(hex(os.getpid())[2:])
print(time + pid)


###########################################################
# 2017/10/28 13:03:54
# 元组(只读列表 不可修改 其他属性与列表类似)
# count(value)　　---返回元组中值为value的元素的个数
# index(value, [start, [stop]])　　---返回列表中第一个出现的值为value的索引，如果没有，则异常 ValueError
tup = (1, 2, 3, 4, 5)
print(tup)
print(tup[1:])
print(tup[1:3])
print(tup[1:4:2])

###########################################################
# 字典 对key进行哈希函数运算,确定value的存储位置
dic = {'name': 'pangdahai', 'age': '21', 'id': '123456'}
print(dic)
print(dic['name'])
dic1 = dict((('name', 'pangdahai'), ('age', '21'), ('id', '123456')))
dic2 = dict({'name': 'pangdahai', 'age': '21', 'id': '123456'})
print(dic1, dic2)

# 增
dic = {'name': 'pangdahai'}
dic['age'] = '21'
print(dic)

# setdefault(key,value)如果key不存在,则添加到字典中
#                      如果key存在,则返回key对应的value
dic.setdefault('age', '123456')
print(dic)

# 查
dic = {'name': 'pangdahai', 'age': '21', 'id': '123456'}
print(list(dic.keys()))
print(list(dic.values()))
print(dic['name'])
print(dic.get('name'))

# get(key,[default])　　---返回字典dict中键key对应值，如果字典中不存在此键，则返回default 的值(default默认值为None)

# has_key(key)　　---判断字典中是否有键key

# 改
dic = {'name': 'pangdahai', 'age': '21', 'id': '123456'}
dic['name'] = 'moonboss'
print(dic)
# update用另一个字典,存在则修改,不存在则添加
dic1 = {'name': 1, 'b': 2, 'c': 3}
dic.update(dic1)
print(dic)

# 删
dic = {'name': 'pangdahai', 'age': '21', 'id': '123456'}

# 删除指定键值
del dic['name']
print(dic)
# 删除整个字典对象
# del dic
# print(dic)

dic = {'name': 'pangdahai', 'age': '21', 'id': '123456', 'x': 'abcd'}
# pop返回删除的值
print(dic.pop('name'))
# popitem删除并返回字典最后一个值
print(dic.popitem())
print(dic)
# 清空整个字典
# clear()　　---删除字典中所有元素
dic.clear()
print(dic)

# copy()　　---返回字典的一个副本(浅复制)

dic = dict.fromkeys(['host', 'localhost'], 'test')
print(dic)

dic = dict.fromkeys(['host', 'localhost'], ['test', 'test2'])
print(dic)

dic['host'][0] = 'test3'
print(dic)

# 排序
dic = {'name': 'pangdahai', 'age': '21', 'id': '123456'}
# dict.fromkeys(seq,val=None) ---创建并返回一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值(默认为None)
# sorted()默认按key排序
print(sorted(dic))
# 排序并输出key-value
print(sorted(dic.items()))

# 字典遍历
dic = {'name': 'pangdahai', 'age': '21', 'id': '123456'}
# items()　　---返回一个包含字典中(键, 值)对元组的列表