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
print(os.pathsep)    # 输出用于分割文件路径的字符串
print(os.name)    # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system('dir')  # 运行shell命令，直接显示
print(os.environ)  # 获取系统环境变量
print(os.path.abspath('./'))  # 返回path规范化的绝对路径
print(os.path.split('./'))  # 将path分割成目录和文件名二元组返回
print(os.path.dirname('./'))  # 返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.basename('./'))  # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.exists('./'))  # 如果path存在，返回True；如果path不存在，返回False
print(os.path.isabs('./'))  # 如果path是绝对路径，返回True
print(os.path.isfile('./'))  # 如果path是一个存在的文件，返回True。否则返回False
print(os.path.isdir('./'))  # 如果path是一个存在的目录，则返回True。否则返回False
# print(os.path.join())  # 将多个路径path1[, path2[, ...]]组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.getatime('./'))  # 返回path所指向的文件或者目录的最后存取时间
print(os.path.getmtime('./'))  # 返回path所指向的文件或者目录的最后修改时间
print(os.path.getsize('./Python02.py'))  # 返回文件大小


import sys
# sys模块 与Python解释器交互

print(sys.argv)  # 命令行参数List，第一个元素是程序本身路径
sys.exit(0)  # 退出程序，正常退出时exit(0)
print(sys.version)  # 获取Python解释程序的版本信息
print(sys.maxint)  # 最大的Int值
print(sys.path)  # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.platform)  # 返回操作系统平台名称
sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]


import hashlib

m = hashlib.md5()
m.update(b'Hello')
m.update(b'''It's me''')
print(m.digest())
m.update(b'''It's been a long time since last time we ...''')

print(m.digest())  # 2进制格式hash
print(len(m.hexdigest()))  # 16进制格式hash
'''
def digest(self, *args, **kwargs): # real signature unknown
    """ Return the digest value as a string of binary data. """
    pass

def hexdigest(self, *args, **kwargs): # real signature unknown
    """ Return the digest value as a string of hexadecimal digits. """
    pass

'''

# ######## md5 ########

hash = hashlib.md5()
hash.update('admin')
print(hash.hexdigest())

# ######## sha1 ########

hash = hashlib.sha1()
hash.update('admin')
print(hash.hexdigest())

# ######## sha256 ########

hash = hashlib.sha256()
hash.update('admin')
print(hash.hexdigest())


# ######## sha384 ########

hash = hashlib.sha384()
hash.update('admin')
print(hash.hexdigest())

# ######## sha512 ########

hash = hashlib.sha512()
hash.update('admin')
print(hash.hexdigest())


import logging

# DEBUG < INFO < WARNING < ERROR < CRITICAL
logging.basicConfig(filename='test.log', level=logging.INFO)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')

# %(name)s 	Logger的名字

# %(levelno)s 数字形式的日志级别

# %(levelname)s 	文本形式的日志级别

# %(pathname)s 	调用日志输出函数的模块的完整路径名，可能没有

# %(filename)s 	调用日志输出函数的模块的文件名

# %(module)s 	调用日志输出函数的模块名

# %(funcName)s 	调用日志输出函数的函数名

# %(lineno)d 	调用日志输出函数的语句所在的代码行

# %(created)f 	当前时间，用UNIX标准的表示时间的浮 点数表示

# %(relativeCreated)d 	输出日志信息时的，自Logger创建以 来的毫秒数

# %(asctime)s 	字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒

# %(thread)d 	线程ID。可能没有

# %(threadName)s 	线程名。可能没有

# %(process)d 	进程ID。可能没有

# %(message)s 	用户输出的消息

# create logger