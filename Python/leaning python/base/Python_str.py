

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
print(vars())

# 3.x格式化方法
print('{0}, {1} and {2}'.format('moon', 'boss', 'max'))
print('{name}, {nicname}, {age}'.format(name='moonboss', nicname='MaxKim', age='23'))
print('{name}, {0}, {age}'.format('MaxKim', name='moonboss', age='23'))


import sys
# 键
print('My {1[name]} runs {0.platform}'.format(sys, {'name': 'laptop'}))
# 属性
print('My {config[name]} runs {sys.platform}'.format(sys=sys, config={'name': 'laptop'}))
# 偏移值
somelist = list('SPAM')
print('first={0[0]}, third={0[2]}'.format(somelist))
print('first={0}, last={1}'.format(somelist[0], somelist[-1]))

parts = somelist[0], somelist[-1], somelist[1:3]
print('first={0}, last={1}, middle={2}'.format(*parts))

# 具体格式化
# [[fill]align][sign][#][0][width][.precision][typecode]
# align	<, >, =, ^
print('{0:10} = {1:10}'.format('spam', 123.4567))
print('{0:>10} = {1:<10}'.format('spam', 123.4567))
print('{0.platform:>10} = {1[item]:<10}'.format(sys, dict(item='laptop')))

# 类型
print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))

# 十六进制 八进制 二进制
print('{0:X}, {1:o}, {2:b}'.format(255, 255, 255))

# 格式化参数 硬编码
print('{0:.2f}'.format(1 / 3.0))

# 格式化参数 从参数获取
print('{0:.{1}f}'.format(1 / 3.0, 4))
# 星号语法
print('%.*f' % (4, 1 / 3.0))

# 单项格式化
print(format(1.2345, '.2f'))