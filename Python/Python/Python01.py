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
# 过滤器 只过滤，不做任何操作
str = ['a', 'b', 'c', 'd']


def func3(s):
    if s != 'b':
        return s


ret = filter(func3, str)
print(list(ret))


# map 对字符串做处理
def func4(s):
    return s + "xxx"


ret = map(func4, str)
print("map:", list(ret))


# reduce
def add1(x, y):
    return x + y


print(reduce(add1, range(1, 10)))  # 1+2+...+9


# lambda
add2 = lambda a, b: a + b

print(add2(4, 5))


# _init_方法　　在类的一个对象被创建时调用该方法；相当于c++中的构造函数。

# _del方法　　在类的对象被销毁时调用该方法；相当于c++中的析构函数。在使用del删除一个对象时也就调用del_方法。

'''
存储器 python提供一个标准的模块，成为pickle，使用它可以在一个文件中存储任何python对象，
之后可以完整的取出来，这被称为持久地存储对象；还有另外一个模块成为cPickle，
它的功能和pickle完全一样，只不过它是用c写的，要比pickle速度快(大约快1000倍)。
'''


# 装饰器
# 运用装饰器
def run(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('time:', end - start)
    return inner


@run
def dog():
    print('dog is running')


dog()


# 指定参数，可变参数*args，可变**kwgs
def printpara(num, *args, **kwgs):
    print(num)
    print(args)
    print(kwgs)


printpara(10, 1, "strap", ["strn", "2"], name="pangdahai", ptype="hahaha")


# 类装饰器
# 类装饰函数时，在装饰阶段，__init__ 函数执行；在被装饰的函数被调用时，__call__ 执行。

class decorador:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwgs):
        print("addr:%d" % id(self))
        self.func(*args, **kwgs)
        print("do after")


@decorador
def saytext(text):
    print(text)


# 测试
saytext("hello")
'''输出
addr:140061401007720
hello
do after
'''
saytext("world")
'''输出
addr:140061401007720
world
do after
'''


class decorador1:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwgs):
        print("addr:%d" % id(self))
        obj = self.cls(*args, **kwgs)
        print("do after")
        return obj


# 类装饰类，示例拦截每个person对象的创建。
@decorador1
class person():
    def __init__(self, *args, **kwgs):
        self.para = args
        self.kwgs = kwgs

    def saytext(self, text):
        print(text)
        print(self.para)


# 测试
ming = person("ming", "man")
'''输出
addr:140118207480272
do after
'''
ming.saytext("hello")
'''输出
hello
('ming', 'man')
'''
lili = person("lili", "woman")
'''输出
addr:140118207480272
do after
'''
lili.saytext("world")
'''输出
world
('lili', 'woman')
'''
lili.saytext("test")
'''输出
test
('lili', 'woman')
'''


# 类装饰器可以把类的名称重新绑定另一个类
def decorador2(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapper = cls(*args)

        def __getatter__(self, name):
            return getattr(self.wrapper, name)
    return Wrapper


@decorador2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 测试
start = Point(6, 7)

end = Point(1, 2)


# 装饰器的镶套
'''
@animal
@person
@student
def func():
    pass

# 等价于
animal(person(student(func)))
'''
# 闭包
# 闭包(closure)是函数式编程的重要的语法结构。

# 定义：如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包(closure).
# 被装饰函数带参数


def show_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("time=%s" % (start_time - end_time))

    return wrapper

# 装饰器函数带参数


def time_logger(flag=0):
    def show_time(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print("time:%s" % (end_time - start_time))

            if flag:
                print("将操作记录到日志")

        return wrapper
    return show_time


# 调用


@time_logger(3)
def add(*args, **kwargs):
    time.sleep(1)
    sum = 0
    for i in args:
        sum += i
    print(sum)
