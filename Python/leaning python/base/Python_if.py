
# and 和 or 返回真或假对象
# or 从左至右 返回第一个为真的对象 或最后一个假的对象
print(2 or 3)
print(0 or 3)
print({} or [] or ())

# and 从左至右 返回第一个为假的对象 或最后一个真的对象
print({} and [])
print(3 and [])
print(3 and 5)

# if/else三元表达式
A = 'moon' if 't' else 'boss'
print(A)

A = (('t' and 'moon') or 'boss')
print(A)

# 列表索引