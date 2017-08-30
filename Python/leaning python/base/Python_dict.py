
D = {'a': 1, 'd': 3, 'c': 2}
print(D)
Ks = list(D.keys())
Ks.sort()

for key in Ks:
    print(key, '=>', D[key])

for key in sorted(D):
    print(key, '=>', D[key])

for c in 'moonboss':
    print(c.upper())


if 'f' in D:
    print(D['f'])