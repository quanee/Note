'''特殊变量 应用'''



import os

print(__file__)
print(os.path.dirname(os.path.abspath(__file__)))

print(__name__)

import shelve

s = shelve.open('test')
s['info'] = {'name': 'moon', 'age': '34'}