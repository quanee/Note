# coding=utf-8 文件编码格式
import sys
'''编码'''

# f = open('rf.py', 'r', encoding='utf8')
# print(f.read())

print(sys.getdefaultencoding())  # 获取默认编码

s = '我的世界'
print(len(s))
print(repr(s))
print(type(s))

s = s.encode('utf8')
print(s, type(s), repr(s))