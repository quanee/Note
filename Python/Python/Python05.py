'''
time模块
random模块
os模块
sys模块
hashlib模块
logging模块
'''



import time

print(time.clock())  # 返回处理器时间,3.3开始已废弃 , 改成了time.process_time()测量处理器运算时间,不包括sleep时间,不稳定,mac上测不出来
print(time.altzone)  # 返回与utc时间的时间差,以秒计算\
print(time.asctime())  # 返回时间格式'Fri Aug 19 11:14:16 2016',
print(time.localtime())  # 返回本地时间 的struct time对象格式
print(time.gmtime(time.time() - 800000))  # 返回utc时间的struc时间对象格式

print(time.asctime(time.localtime()))  # 返回时间格式'Fri Aug 19 11:14:16 2016',
print(time.ctime())  # 返回Fri Aug 19 12:38:29 2016 格式, 同上

# 日期字符串 转成  时间戳
string_2_struct = time.strptime('2016/05/22', '%Y/%m/%d')  # 将 日期字符串 转成 struct时间对象格式
print(string_2_struct)

struct_2_stamp = time.mktime(string_2_struct)  # 将struct时间对象转成时间戳
print(struct_2_stamp)

# 将时间戳转为字符串格式
print(time.gmtime(time.time() - 86640))  # 将utc时间戳转换成struct_time格式
print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))  # 将utc struct_time格式转成指定的字符串格式

# 时间加减
import datetime

print(datetime.datetime.now())  # 返回 2016-08-19 12:47:03.941925
print(datetime.date.fromtimestamp(time.time()))  # 时间戳直接转成日期格式 2016-08-19
print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3))  # 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))  # 当前时间+30分


c_time = datetime.datetime.now()
print(c_time.replace(minute=3, hour=2))  # 时间替换


import random


print(random.random())
print(random.randint(1, 2))
print(random.randrange(1, 10))

checkcode = ''
for i in range(4):
    current = random.randrange(0, 4)
    if current != i:
        temp = chr(random.randint(65, 90))
    else:
        temp = random.randint(0, 9)
    checkcode += str(temp)
print(checkcode)


import os
# os模块 与操作系统交互

print(os.getcwd())  # 获取当前工作目录，即当前python脚本工作的目录路径
# os.chdir('../')  # 改变当前脚本工作目录；相当于shell下cd
print(os.curdir)  # 返回当前目录: ('.')
print(os.pardir)  # 获取当前目录的父目录字符串名：('..')
os.makedirs('./adir/bdir')  # 可生成多层递归目录
os.removedirs('./adir/bdir')  # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('./adir')  # 生成单级目录；相当于shell中mkdir dirname
os.rmdir('./adir')  # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
print(os.listdir('./'))  # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove('data.bin')  # 删除一个文件
os.rename('datafile.pkl', 'data.bin')  # 重命名文件/目录
print(os.stat('./Python05.py'))  # 获取文件/目录信息
print(os.sep)  # 输出操作系统特定的路径分隔符，win下为'\\',Linux下为'/'
print(os.linesep)  # 输出当前平台使用的行终止符，win下为'\t\n',Linux下为'\n'