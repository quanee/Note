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