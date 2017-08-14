'''杨辉三角'''


def triangles():
    b = [1]
    while True:
        yield b
        b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]


n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break



import pprint

message = 'It was a bridge cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1


pprint.pprint(count)


import pyperclip

pyperclip.copy('Hello world!')
print(pyperclip.paste())


import shelve

shelfFile = shelve.open('myfile')
cats = ['zophie', 'pooka', 'simon']
shelfFile['cats'] = cats
shelfFile.close()


import shutil
import os
'''复制 移动 改名 删除文件'''

# 复制文件 并命名
shutil.copy('./rf.py', './test.py')
# 复制文件夹
shutil.copytree('../sp', './test')
# 文件/文件夹移动改名
shutil.move('./test', './tests')
# 删除文件
os.unlink('./test.py')
# 删除空文件夹
# shutil.rmdir('')
# 删除文件夹(不可恢复)
shutil.rmtree('./tests')


import send2trash