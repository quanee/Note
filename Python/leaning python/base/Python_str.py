

# 格式化表达式
# 4(可以是变量)指定精度
print('%f, %.2f, %.*f' % (1 / 3.0, 1 / 3.0, 4, 1 / 3.0))

# 字典键值
print('%(n)d %(x)s' % {'n': 1, 'x': 'abc'})

reply = '''
Greetings...
Hello %(name)s!
Your age squared is %(age)s
'''

values = {'name': 'moonboss', 'age': 40}

print(reply % values)

# vars()返回字典 包含本函数调用时存在的变量