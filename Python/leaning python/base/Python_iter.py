
f = open('data.txt', 'r')

print(f.__next__(), end='')
print(f.__next__(), end='')
print(f.__next__(), end='')

print(next(f), end='')
print(next(f), end='')
print(next(f), end='')

