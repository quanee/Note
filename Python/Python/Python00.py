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
