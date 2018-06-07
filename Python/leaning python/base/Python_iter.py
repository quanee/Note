
f = open('data.txt', 'r')

print(f.__next__(), end='')
print(f.__next__(), end='')
print(f.__next__(), end='')

print(next(f), end='')
print(next(f), end='')
print(next(f), end='')


E = enumerate('moon')

I = iter(E)

print(next(I))
print(next(I))
print(next(I))

print(list(enumerate('boss')))


# 自动使用迭代协议来扫描文件 返回最高(最低)的字符串的值行
print(max(open('Python_dict.py', 'r', encoding='utf8')), )
print(min(open('Python_dict.py', 'r', encoding='utf8')))


X = (1, 2)
Y = (3, 4)