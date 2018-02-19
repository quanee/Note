'''
反射:
通过字符串的形式,导入模块;
通过字符串的形式,去模块寻找指定函数,并执行.
利用字符串的形式去对象(模块)中操作(查找/获取/删除/添加)成员,一种基于字符串的事件驱动!
'''
"""
imp = input('输入模块名:')
dd = __import__(imp)

inp_func = input('输入函数名:')

f = getattr(dd, inp_func, None)

f()
"""


for item in [lambda x: i * x for i in range(4)]:
    print(item(2))  # 6 6 6 6


for item in [lambda x, i=i: i * x for i in range(4)]:
    print(item(2))  # 0 2 4 6


for item in (lambda x, i=i: i * x for i in range(4)):
    print(item(2))  # 0 2 4 6


def fun():
    for i in range(4):
        yield lambda x: i * x


for item in fun():
    print(item(2))  # 0 2 4 6


from functools import partial  