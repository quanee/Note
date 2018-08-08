

# 位置:从左至右匹配
# func(value)
#
# 关键字参数:通过参数名匹配 (name=value)
# func(name=value)
# func(**dict)
#
# 默认参数:为没有传入值的参数定义参数值 (name=value)
#
# 可变参数:收集任意多基于位置或关键字的参数 *开头
# func(*sequence)
#
# 可变参数解包: 传递任意多基于位置或关键字的参数 *开头
#
# Keyword-only参数: 参数必须按照名称传递
#
# 位置参数, 关键字参数, *sequence形式组合, **dict

'''
参数匹配步骤:
        通过位置分配非关键字参数
        通过变量名分配关键字参数
        其他额外的非关键字参数分配到*name元组
        其他额外的关键字参数分配到**name字典中
        用默认值分配给在头部未得到分配的参数
'''

def f(a, b, c):
    print(a, b, c)


# 位置参数
f(1, 2, 3)
# 关键字参数
f(c=3, a=1, b=2)

f(1, c=3, b=2)


# 默认参数
def f(a, b=2, c=3):
    print(a, b, c)


f(1)
f(a=1)
f(1, 4)
f(1, 4, 5)
# 跳过默认参数
f(1, c=6)


# 关键字参数和默认参数混合
def func(moon, boss, mas=0, kim=0):
    print((moon, boss, mas, kim))


func(1, 2)  # (1, 2, 0, 0)
func(1, kim=1, boss=0)  # (1, 0, 0, 1)
func(moon=1, boss=2)  # (1, 2, 0, 0)
func(mas=1, boss=2, moon=3)  # (3, 2, 1, 0)
func(1, 2, 3, 4)  # (1, 2, 3, 4)


# 任意参数
# 收集参数
def f(*args):
    print(args)


f()  # ()
f(1)  # (1,)
f(1, 2, 3, 4)  # (1, 2, 3, 4)


def f(**args):
    print(args)


f()  # {}
f(a=1, b=2)  # {'a': 1, 'b': 2}
