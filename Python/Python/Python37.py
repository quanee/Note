import hashlib

f = open('./Python37.py', 'rb')

sh = hashlib.sha256()
sh.update(f.read())
print(sh.hexdigest())

f.close()

# 计算字符串md5
src = ''