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