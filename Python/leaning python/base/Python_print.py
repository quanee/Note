import sys

a, b, c = 1, 2, 3
# sep 分隔符 默认空格 (Python3 特有)
# end 末尾字符 默认\n
# file 文本发送对象 默认sys.out
log = open('data.txt', 'a')
print(a, b, c, sep='$', end='%\n', file=log)

# 打印重定向
sys.stdout.write('hello world\n')

tmp = sys.stdout
sys.stdout = log

print('sys.out = log')