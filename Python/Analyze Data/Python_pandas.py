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
# 使用字典创建
dfdata = {'Name': ['Zhang San', 'Li Si', 'Wang Laowu', 'Zhao Liu', 'Qian Qi', 'Sun Ba'], 'Subject': ['Literature', 'History', 'English', 'Maths', 'Physics', 'Chemics'], 'Score': [98, 76, 84, 70, 93, 83]}
scoresheet = pd.DataFrame(dfdata)
scoresheet.index = ['No1', 'No2', 'No3', 'No4', 'No5', 'No6']
print(scoresheet)
# 查看前几行 默认5
print(scoresheet.head())
print(scoresheet.columns)
print(scoresheet.values)

dfdata2 = {'Name': {101: 'Zhang San', 102: 'Li Si', 103: 'Wang Laowu', 104: 'Zhao Liu', 105: 'Qian Qi', 106: 'Sun Ba'},
           'Subject': {101: 'Literature', 102: 'History', 103: 'English', 104: 'Maths', 105: 'Physics', 106: 'Chemics'},
           'Score': {101: 98, 102: 76, 103: 84, 104: 70, 105: 93, 106: 83}}
scoresheet2 = pd.DataFrame(dfdata2)
print(scoresheet2)


# numpy创建DataFrame
numframe = np.random.randn(10, 5)
framenum = pd.DataFrame(numframe)
print(framenum.head())
# 打印数据框属性信息
print(framenum.info())
# 打印每列属性
print(framenum.dtypes)

stock = np.dtype([('name', np.str_, 4), ('time', np.str_, 10), ('opening_price', np.float64), ('closing_price', np.float64), ('lowest_price', np.float64), ('highest_price', np.float64), ('volume', np.int32)])
jd_stoct = np.loadtxt('data.csv', delimiter=',', dtype=stock)
jd = pd.DataFrame(jd_stoct)
print(jd.head())
print(jd.info())

# 直接读入csv文件构造DataFrame
jddf = pd.read_csv('data.csv', header=None, names=['name', 'time', 'opening_price', 'closing_price', 'lowest_price', 'highest_price', 'volume'])
# header=None 不自动把数据的第一行 第一列设置成行,列索引
# name 指定索引
print(jddf.head())

# 直接读入excel文件构造DataFrame
jddf = pd.read_excel('data.xlsx', header=None, names=['name', 'time', 'opening_price', 'closing_price', 'lowest_price', 'highest_price', 'volume'])
print(jddf.head())

'''
其他数据源构造DataFrame
  * read_table: 读入具有分隔符的文件
  * read_sql: 输入SQL数据库文件
  * read_sas: 读入SAS的xpt或sas7bdat格式的数据集
  * read_stata: 读入STATA数据集
  * read_json: 读入json数据
  * read_html: 读入网页中的表
  * read_clipboard: 读入剪贴板中的数据内容
  * read_fwf: 读入固定宽度格式化数据