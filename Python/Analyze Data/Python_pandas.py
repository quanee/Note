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
  * read_hdf: 读入分布式存储系统中的文件
'''

jddf = pd.read_excel('data.xlsx', sep=',', header=None, names=['name', 'time', 'opening_price', 'closing_price', 'lowest_price', 'highest_price', 'volume'])
jddfsetindex = jddf.set_index(jddf['time'])
print(jddfsetindex.head())
print(type(jddfsetindex.index))


# 数据导出
# jddf.to_csv('jdstockdata.csv')
# jddf.to_excel('jdstockdata.xlsx')

# 索引和切片
print(scoresheet.Subject)
print(scoresheet[['Name', 'Score']])
print(scoresheet[:'No4'])
print(scoresheet.ix[['No1', 'No3', 'No6']])
print(scoresheet.ix[3:6, ['Name', 'Score']])
print(scoresheet['Subject'])
# print(scoresheet.ix[3:6, [1, 3]])
# print(scoresheet.iloc[[1, 4, 5], [0, 3]])
print(scoresheet.loc[['No1', 'No5'], ['ID', 'Score']])
print(scoresheet[(scoresheet.Score > 80) & (scoresheet.Score <= 90)])
print(scoresheet[['Name', 'Score']][(scoresheet.Score > 80) & (scoresheet.Score <= 90)])

# 行列操作
scoresheet = pd.DataFrame(dfdata, columns=['ID', 'Name', 'Subject', 'Score'], index=['No1', 'No2', 'No3', 'No4', 'No5', 'No6'])
print(scoresheet)
print(scoresheet.reindex(columns=['Name', 'Subject', 'ID', 'Score']))

# 修改行/列数据
# 新增列
scoresheet['Homeword'] = 90
print(scoresheet)
# 修改列名
scoresheet.rename(columns={'Homeword': 'Homework'}, inplace=True)
print(scoresheet)

scoresheet['ID'] = np.arange(6)
print(scoresheet)

# 替代精确匹配的索引的值
fixed = pd.Series([97, 76, 83], index=['No1', 'No3', 'No6'])
scoresheet['Homework'] = fixed
print(scoresheet)

# 删除行/列数据
# 删除列
del scoresheet['Homework']
print(scoresheet)

# 删除行或列 (inplace=True直接修改元数据内存值 inplace=False返回修改后的值)
scoresheet.drop('ID', axis=1, inplace=True)  # axis=1 列 axis=0 行
print(scoresheet)
scoresheet.drop(['No1', 'No5', 'No6'], axis=0, inplace=True)
print(scoresheet)

# 排序
ssort = pd.Series(range(5), index=['b', 'a', 'd', 'e', 'c'])
print(ssort.sort_index())
print(ssort.sort_index(ascending=False))

scoresheet2.index = [102, 101, 106, 104, 103, 105]
print(scoresheet2)
print(scoresheet2.sort_index())
print(scoresheet2.sort_index(axis=0, ascending=False))
print(scoresheet2.sort_index(axis=1, ascending=False))
print(scoresheet2.sort_index(by='Score', ascending=False))
print(scoresheet2.sort_values(by='Score', ascending=False))

# 排名
rrank = pd.Series([10, 12, 9, 9, 14, 4, 2, 4, 9, 1])
print(rrank.rank())
print(rrank.rank(ascending=False))
'''
average  平均分配排名
min  最小排名
max  最大排名
first  按出现顺序排名
'''
print(rrank.rank(method='first'))
print(rrank.rank(method='max'))
print(scoresheet2.rank())

# 运算
cs1 = pd.Series([1.5, 2.5, 3, 5, 1], index=['a', 'c', 'd', 'b', 'e'])
cs2 = pd.Series([10, 20, 30, 50, 10, 100, 20], index=['c', 'a', 'e', 'b', 'f', 'g', 'd'])
print(cs1 + cs2)

cdf1 = pd.DataFrame(np.arange(10).reshape((2, 5)), columns=list('bcaed'))
cdf2 = pd.DataFrame(np.arange(12).reshape((3, 4)), columns=list('abcd'))
print(cdf1 + cdf2)
print(cdf1.add(cdf2, fill_value=0))

# 函数应用与映射
reversef = lambda x: -x
print(reversef(cs2))

rangef = lambda x: x.max() - x.min()
print(rangef(cs2))
print(rangef(cdf1.add(cdf2, fill_value=0)))
print((cdf1.add(cdf2, fill_value=0)).apply(rangef, axis=0))
print((cdf1.add(cdf2, fill_value=0)).apply(rangef, axis=1))


def statistics(x):
    return pd.Series([x.min(), x.max(), x.max() - x.min(), x.mean(), x.count()], index=['Min', 'Max', 'Range', 'Mean', 'N'])


outformat = lambda x: '%.2f' % x
# 格式化
print(((cdf1.add(cdf2, fill_value=0)).apply(statistics)).applymap(outformat))
# apply 的操作对象是DataFrame的一列或一行数据
# applymap是元素级的 只支持一个函数 作用于每个DataFrame的每个数据
# map也是元素级的, 对Series中的每个数据调用一次函数

# 分组 (python2 map返回list python3 map返回map对象)
jddf['Market'] = list(map(lambda x: 'Good' if x > 0 else ('Bad' if x < 0 else 'OK'), jddf['closing_price'] - jddf['opening_price']))
print(jddf.head())

jddfgrouped = jddf.groupby(jddf['Market'])
print(jddfgrouped.describe())

# 合并
c1 = pd.DataFrame({'Name': {101: 'Zhang San', 102: 'Li Si', 103: 'Wang Laowu', 104: 'Zhao Liu', 105: 'Qian Qi', 106: 'Sun Ba'},
                   'Subject': {101: 'Literature', 102: 'History', 103: 'English', 104: 'Maths', 105: 'Physics', 106: 'Chemics'},
                   'Score': {101: 98, 102: 76, 103: 84, 104: 70, 105: 93, 106: 83}})
print(c1)

c2 = pd.DataFrame({'Gender': {101: 'Male', 102: 'Male', 103: 'Male', 104: 'Female', 105: 'Female', 106: 'Male'}})
print(c2)

c = pd.concat([c1, c2], axis=1)
print(c)

print(c1.append(c2))
print(pd.concat([c1, c2], axis=0))

# 按照指定关键字合并
c3 = pd.DataFrame({'Name': {101: 'Zhang San', 102: 'Li Si', 103: 'Wang Laowu', 104: 'Zhao Liu', 105: 'Qian Qi', 106: 'Sun Ba'},
                   'Gender': {101: 'Male', 102: 'Male', 103: 'Male', 104: 'Female', 105: 'Female', 106: 'Male'}})
print(c3)

# 按照相同列合并(类SQL JOIN)
print(pd.merge(c1, c3, on='Name'))


# 分类数据
student_profile = pd.DataFrame({'Name': ['Morgan Wang', 'Jackie Li', 'Tom Ding', 'Erricson John', 'Juan Saint', 'Sui Mike', 'Li Rose'],
                                'Gender': [1, 0, 0, 1, 0, 1, 2],
                                'Blood': ['A', 'AB', 'O', 'AB', 'B', 'O', 'A'],
                                'Grade': [1, 2, 3, 2, 3, 1, 2],
                                'Height': [175, 180, 168, 170, 158, 183, 173]})
print(student_profile)
