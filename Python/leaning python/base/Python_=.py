moon = 'moon'

# 元组分解赋值
moon, boss = 'yum', 'YUM'
# 列表分解赋值
[moon, boss] = ['yum', 'YUM']
# 序列赋值
a, b, c, d = 'moon'
print(a, b)
# 扩展序列解包赋值
a, *b = 'moon'
print(a, b)
# 多重目标赋值
moon = boss = 'lunch'
# 增强赋值
moon += 's'

string = 'moon'

a, b, c = string[0], string[1], string[2:]
print(a, b, c)

(a, b), c = string[:2], string[2:]
print(a, b, c)

((a, b), c) = ('mo', 'on')
print(a, b, c)

*a, b = string
print(a, b)


# + 创建新对象