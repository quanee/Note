
D = {'a': 1, 'd': 3, 'c': 2}
print(D)
Ks = list(D.keys())
Ks.sort()

for key in Ks:
    print(key, '=>', D[key])