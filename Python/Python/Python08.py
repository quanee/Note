'''json 序列化'''



dic = str({'a': '124', 'b': '454'})
f = open('test', 'w')
f.write(dic)
f.close()
f = open('test', 'r')
dic = f.read()