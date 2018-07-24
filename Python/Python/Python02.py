# coding=utf-8
import re
import time
import datetime
# Python标准库
# Python标准库是随Pthon附带安装的，包含了大量极其有用的模块。


# sys模块　　sys模块包含系统对应的功能
# sys.argv　　---包含命令行参数，第一个参数是py的文件名
# sys.platform　　---返回平台类型
# sys.exit([status])　　---退出程序，可选的status(范围：0-127)：0表示正常退出，其他表示不正常，可抛异常事件供捕获
# sys.path　　　　---程序中导入模块对应的文件必须放在sys.path包含的目录中，使用sys.path.append添加自己的模块路径
# sys.modules　　---This is a dictionary that maps module names to modules which have already been loaded
# sys.stdin,sys.stdout,sys.stderr　　---包含与标准I/O 流对应的流对象


# os模块　　该模块包含普遍的操作系统功能
# os.name字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
# os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径
# os.getenv()和os.putenv()函数分别用来读取和设置环境变量
# os.listdir()返回指定目录下的所有文件和目录名
# os.remove()函数用来删除一个文件
# os.system()函数用来运行shell命令
# os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用' '，Linux使用' '而Mac使用' '
# os.sep 操作系统特定的路径分割符
# os.path.split()函数返回一个路径的目录名和文件名
# os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录
# os.path.existe()函数用来检验给出的路径是否真地存在


'''
lambda

lambda语句被用来创建新的函数对象，并在运行时返回它们。lambda需要一个参数，
后面仅跟单个表达式作为函数体，而表达式的值被这个新建的函数返回。
注意，即便是print语句也不能用在lambda形式中，只能使用表达式。
'''

'''
exec/eval
exec语句用来执行储存在字符串或文件中的Python语句；
eval语句用来计算存储在字符串中的有效Python表达式。
'''

'''
assert

assert语句用来断言某个条件是真的，并且在它非真的时候引发一个错误-- AssertionError。
'''

'''
repr函数

repr函数用来取得对象的规范字符串表示。反引号（也称转换符）可以完成相同的功能。
注意，在大多数时候有 eval(repr(object))==object。
可以通过定义类的repr方法来控制对象在被repr函数调用的时候返回的内容。
'''

# 邮箱验证
'''
[a-zA-Z0-9] 匹配大小写字母与数字

[a-zA-Z] 匹配大小写字母

@ a@b a@b (字符转义)

. a.b a.b (字符转义)

'''


# 获得一个URL地址的扩展名
# "."＋url.split(".")[－1]
def emails(e):
    if len(e) >= 5:
        if re.match("[a-zA-Z0-9]+@+[a-zA-Z0-9]+.+[a-zA-Z]", e):
            return '邮=箱=格式正确！'
    return '邮=箱=格式有误'


# e = input("请输入email:")
# print(e)
# a = emails(e)
# print(a)


def strings(url):
    listt = ['.php', '.html', '.asp', '.jsp']
    for lis in listt:
        suffix = re.findall(lis, url)
        if len(suffix) > 0:
            return lis


address = 'sadf/lsdkjflsdkj/sllls/232323.html'
a = strings(address)
print(a)

# 获得当前时间的前一天（或前一秒）
# 打印当前时间
print(time.ctime())
# 当前时间
now_time = datetime.datetime.now()
print(now_time)
# 昨天的现在
yesterday = now_time + datetime.timedelta(days=-1)
print(yesterday)
# 现在的前一秒
now_old = now_time + datetime.timedelta(seconds=-1)
print(now_old)




"""
== 判断值相等
is 判断引用相等
"""
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(b == c)
print(a is b)


a = 100
b = 100
print(a == b)
print(a is b)
a = 10000
b = 10000
print(a is b)


# 私有化
# _xx   保护属性(from xxx import * 无法导入, import xxx 可以导入)
# __xx  私有属性
# __xx__内置方法或变量名
# xx_   避免与python关键字冲突
class Test(object):

    def __init__(self):
        self.__num = 100

    def setNum(self, value):
        print('----setter----')
        self.__num = value

    def getNum(self):
        print('----getter----')
        return self.__num

    num = property(getNum, setNum)


t = Test()
print(t.getNum())
t.setNum(50)
print(t.getNum())
t.num = 200
print(t.num)


class Money(object):
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("Error:Not Int")