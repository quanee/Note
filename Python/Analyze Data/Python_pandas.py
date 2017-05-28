import pandas as pd
import numpy as np
from scipy import interpolate

# 数据结构
# Series
s1 = pd.Series([100, 78, 59, 63])
print(s1)
print(s1.values)
print(s1.index)

s1.index = ['No.1', 'No.2', 'No.3', 'No.4']
print(s1)

s2 = pd.Series([100, 78, 59, 63], index=['Maths', 'English', 'Literature', 'History'])
print(s2)
print(s2[['English', 'History']])

# 有字典创建
d3 = {'Name': 'Zhang San', 'Gender': 'Male', 'Age': 19, 'Height': 178, 'Weight': 66}
s3 = pd.Series(d3)
print(s3)

student_attrib = ['ID', 'Name', 'Gender', 'Age', 'Grade', 'Height', 'Weight']
s4 = pd.Series(d3, index=student_attrib)
print(s4)

print(pd.isnull(s4))

print(s3 + s4)

s4.name = 'Student\'s profie'
s4.index.name = 'Attrubute'
print(s4)

# 按照指定顺序实现重新索引(返回视图)
print(s4.reindex(index=['Name', 'ID', 'Age', 'Gender', 'Height', 'Weight', 'Grade']))

# index必须是单调
s4.index = ['b', 'g', 'a', 'c', 'e', 'f', 'd']
print(s4)

# 重新索引 增加'h' 并填充 0
print(s4.reindex(index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], fill_value=0))

s4.index = [0, 2, 3, 6, 8, 9, 11]
print(s4.reindex(range(10), method='ffill'))


# =======================================================
# DataFrame
# 创建DataFrame