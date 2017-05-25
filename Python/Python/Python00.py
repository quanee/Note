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
for i in dic.items():
    print(i)
# keys()　　---返回一个包含字典中所有键的列表
# values()　　---返回一个包含字典中所有值的列表
# pop(key, [default])　　---若字典中key键存在，删除并返回dict[key]，若不存在，且未给出default值，引发KeyError异常
# popitem()　　---删除任意键值对，并返回该键值对，如果字典为空，则产生异常KeyError
# setdefault(key,[default])　　---若字典中有key，则返回vlaue值，若没有key，则加上该key，值为default，默认None
# update(dict2)　　---把dict2的元素加入到dict中去，键字重复时会覆盖dict中的键值
# viewitems()　　---返回一个view对象，（key, value）pair的列表，类似于视图。优点是，如果字典发生变化，view会同步发生变化。在迭代过程中，字典不允许改变，否则会报异常
# viewkeys()　　---返回一个view对象，key的列表




# 字符串拼接
a = 'abcd'
b = '1234'
c = 'ABCD'
d = a + b + c
print(d)   # 效率低
d = '**'.join([a, b, c])
print(d)

# 字符串内置方法
strbin = 'hello pangdahai'

print(strbin.count('l'))    # 统计字符出现次数
print(strbin.capitalize())  # 首字母大写
print(strbin.center(40, '+'))  # 填充字符
print(strbin.endswith('y'))  # 判断结束字符
print(strbin.startswith('he'))  # 判断开始字符
strbin = 'he\tllo pangdahai'
print(strbin.expandtabs(tabsize=10))
strbin = 'hello pangdahai'
print(strbin.find('p'))  # 查找到第一个字符位置,并返回索引值
strbin = 'hello {name}, age is {age}'
print(strbin.format(name='pangdahai', age=21))  # 替换变量
print(strbin.format_map({'name': 'pangdahai', 'age': 21}))    # 替换变量(字典)
# print(strbin.index('a'))
print('asd'.isalnum())
print('15'.isdecimal())  # 是否为十进制
print('15'.isdigit())   # 是否为整型
print('15'.isidentifier())   # 是否符合规范
print('Abc'.islower())  # 是否全为小写
print('Abc'.isupper())  # 是否全为大写
print('Ab c'.isspace())  # 是否为空格
print('Abc'.istitle())  # 判断标题
print('Abc'.upper())    # 转为大写
print('Abc'.lower())    # 转为小写
print('title'.rjust(30, '+'))   # 左填充'+' 默认空格
print('title'.ljust(30, '+'))   # 右填充
print(' title \n'.strip())  # 去除空格,换行符
print(' title \n'.lstrip())  # 去除空格,换行符
print(' title \n'.rstrip())  # 去除空格,换行符
print(' hello moonboss '.replace('moonboss', 'pangdahai'))
print(' hello moonboss , very good !'.split(' '))
print(' hello moonboss , very good !'.rsplit(' ', 1))  # 从右边分割, 分割一次

# 2017/10/28 18:53:04
# Python编码解码
'''
二进制
ASCII:英文和拉丁字符, 一个字符一个字节,8位一个字节
gb2312:只有6700多个中文,1980
gbk1.0:2000多个字符, 1995
gb18030:27000多个中文 2000

unicode:utf-32 一个字符4个字节
unicode:utf-16 一个字符2个字节或2个以上,65535
unicode:utf-8 英文用ASCII码来存,中文占3个字节
'''
s = "烫烫"
# 编码
s = s.encode('utf-8')
print(s)
# 解码
s = s.decode('utf-8')
print(s)


# 2017/10/28 19:53:58
# 文件
'''
r   open and reading
w   open and writing
x   create and open
a   open and appending
b   binary
t   text
+   reading and writing
U
'''
f = open('text.txt', 'w', encoding='utf-8')
print(f.fileno())  # 文件描述符
f.write("一骑红尘妃子笑,\n无人知是荔枝来.\n")

f = open('text.txt', 'r', encoding='utf-8')
print(f.fileno())  # 文件描述符
# data = f.read()
# print(data, "\n------------------\n")
# 推荐方式
for i in f.readlines():
    print(i.strip())

f = open('text.txt', 'r+', encoding='utf-8')
for i, v in enumerate(f.readlines()):
    print(i, v.strip())
print(f.tell())  # 当前指针位置
f.close()
# seek()
f = open('text.txt', 'rb')
f.seek(6)   # 指针移动指定位数
for i in f.readlines():
    print(i.strip().decode('utf-8'))
f.close()

f = open('text.txt', 'w', encoding='utf-8')
print(f.fileno())  # 文件描述符
f.write("一骑红尘妃子笑,\n无人知是荔枝来.\n")
# 刷新缓存数据到磁盘
f.flush()

import sys
import time

# for i in range(30):
#     sys.stdout.write("+")
#     sys.stdout.flush() # 实时刷新显示
#     time.sleep(0.1)

for i in range(30):
    print('>', end='', flush=True)
    # time.sleep(0.1)
print('\n', f.isatty())
f.truncate(18)  # 从指定字节位置开始清除,默认从开始清除


# 2017-11-19 08:46:49
# 深浅拷贝

# 浅拷贝
# copy(被拷贝对象可变,只拷贝第一层地址,被拷贝对象不可变,直接引用)
# deepcopy(依次拷贝所有内容)
s = [1, 3, "sdf", 3]

s1 = s.copy()

s[1] = 6

print(s)
print(s1)

# 深拷贝
s = [[1, 5], 3, "sdf", 3]
# 只拷贝第一层地址(s1指向s指向的地址)
s1 = s.copy()
# 修改第二层地址
s1[0][1] = 3

print(s)
print(s1)

a = [2, 4, 5, 6]
b = a