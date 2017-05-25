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