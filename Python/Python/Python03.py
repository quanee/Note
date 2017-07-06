from collections import Iterator

# 迭代器 生成器
"""
可迭代(Iterable)
    list, tuple, dict, set, str
    generator, yield function
可迭代对象(isinstance(x, Iterator))
    generator
"""

# 生成器创建方式
# (x for x in range(123)) 列表生成式
# yield

# 列表生成式
a = [x for x in range(10)]

print(a)


def f(n):
    return n ** 2


b = [f(x) for x in range(10)]

print(b)

t = ['123', 8]

a, b = t
print(a[0], b)


# 生成器 需要时生成 不能随机访问
# 生成器都是迭代器 迭代器不一定是生成器
# 生成器在创建时已经决定能生成多少个值
# 生成器方法
s = (x * 2 for x in range(10))
print(s.__next__())  # 特殊方法
print(next(s))  # Python3 内置方法 Python2 s.next()


def fib(max):
    n, before, after = 0, 0, 1
    while n < max:
        print(before)
        before, after = after, before + after
        n = n + 1


fib(8)


def fib1(max):
    n, before, after = 0, 0, 1
    while n < max:
        yield before
        before, after = after, before + after
        n = n + 1


fib1(8)


#  yield模拟伪并发
def consumer(name):
    print("%s 准备吃包子啦！" % name)
    while True:
        baozi = yield

        print("包子[%s]来了，被[%s]吃了！" % (baozi, name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    # 生成器不能直接调用send()函数(不能确定生成器是否有对象)
    c.__next__()  # 等价于next(c) 等价于c.send(None)
    c2.__next__()
    print("%s开始准备做包子啦！" % name)
    for i in range(10):
        print("做了2个包子！")
        c.send(i)  # 先执行yield，后将i赋给yield的变量
        c2.send(i)


producer("pangdahai")

# 迭代器
# 有iter()方法
# 有next()方法

a = [1, 2, 3, 4]
# next(a)