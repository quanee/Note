import random
'''随机数生成'''


print(random.random())
# 返回给定范围内均匀的随机分布
print(random.uniform(1, 9))
print(random.randrange(20))
print(random.randrange(0, 99, 3))
print(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)
print(items)
print(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 5))

weighted_choices = [('Three', 3), ('Two', 2), ('One', 1), ('Four', 4)]

population = [val for val, cnt in weighted_choices for i in range(cnt)]
print(random.choice(population))

'''
泊松分布
'''