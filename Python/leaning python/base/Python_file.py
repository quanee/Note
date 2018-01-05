import pickle

D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')

pickle.dump(D, F)

F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)

print(E)

F.close()



import struct

F = open('data.bin', 'wb')
data = struct.pack('>i4sh', 7, b'moon', 8)
print(data)
F.write(data)
F.close()

F = open('data.bin', 'rb')
data = F.read()