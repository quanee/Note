# 2017-11-19 15:18:43
import time
from functools import reduce
# 函数
'''
函数 != function()
计算机函数 == subroutine 子程序, procedures 过程
    * 提高代码重用
    * 方便修改,易扩展
    * 保持代码一致性
'''

# 函数的参数
# 必须参数


def func0(name, age):
    print('name:%s\nage:%d' % (name, age))


func0(age=21, name='class')


# 默认参数
def func1(name, age, sex='male'):
    print('name:%s\nage:%d\nsex:%s' % (name, age, sex))


func1(age=21, name='class')


# 关键字参数
# 不定长参数

count = 3453


def func2():
    print(count)
    # count = 334


func2()


# 内嵌函数
def outer():
    x = 23

    def inner():
        print(x)

    return inner


outer()()
f = outer()
f()

# 内置函数