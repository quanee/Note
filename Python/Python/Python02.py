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