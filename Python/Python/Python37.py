import hashlib

f = open('./Python37.py', 'rb')

sh = hashlib.sha256()
sh.update(f.read())
print(sh.hexdigest())
