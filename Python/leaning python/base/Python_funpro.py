
# 计算嵌套子列表结构中所有数字的总和
def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot


L = [1, [2, 3, [4, 5]]]
print(sumtree(L))


def make(label):
    def echo(message):
        print(label + ':' + message)

    return echo


F = make('moon')
F('boss')


# 函数内省
print(make.__name__)
print(dir(make.__name__))
print(make.__code__)
print(dir(make.__code__))
print(make.__code__.co_varnames)
print(make.__code__.co_argcount)
