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