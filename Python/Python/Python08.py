'''json 序列化'''



dic = str({'a': '124', 'b': '454'})
f = open('test', 'w')
f.write(dic)
f.close()
f = open('test', 'r')
dic = f.read()
f.close()
print(eval(dic)['b'])

import json

# json dumps loads
dic = {'name': 'boss', 'age': '48'}
data = json.dumps(dic)
f = open('test', 'w')
f.write(data)
f.close()

f = open('test', 'r')
data = f.read()
f.close()
data = json.loads(data)

print(data['name'])

import pickle

# pickle dumps loads
dic = {'name': 'boss', 'age': '48'}
data = pickle.dumps(dic)
f = open('test', 'wb')
f.write(data)
f.close()

f = open('test', 'rb')
data = f.read()