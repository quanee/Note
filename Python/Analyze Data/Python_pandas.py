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

# 为Male列添加标签
student_profile['Gender_Value'] = student_profile['Gender'].astype('category')
student_profile['Gender_Value'].cat.categories = ['Female', 'Male', 'Unconfirmed']
print(student_profile)
student_profile['Gender_Value'].cat.categories = ['male', 'FeMale', 'Unconfirmed']
print(student_profile)

# 对数值型数据分段标签
labels = ["{0}-{1}".format(i, i + 10) for i in range(160, 200, 10)]
student_profile['Height_Group'] = pd.cut(student_profile.Height, range(160, 205, 10), right=False, labels=labels)
print(student_profile)


# 时间序列
# 创建时间序列
# 将当前时间转化为时间戳
print(pd.Timestamp('now'))

# 利用时间戳创建时间序列
dates = [pd.Timestamp('2017-07-05'), pd.Timestamp('2017-07-06'), pd.Timestamp('2017-07-07')]
ts = pd.Series(np.random.randn(3), dates)
print(ts)
print(ts.index)
print(type(ts.index))

dates = pd.date_range('2017-07-05', '2017-07-07')
tsdr = pd.Series(np.random.randn(3), dates)
print(tsdr)
print(type(tsdr.index))

dates = [pd.Period('2017-07-05'), pd.Period('2017-07-06'), pd.Period('2017-07-07')]
tsp = pd.Series(np.random.randn(3), dates)
print(tsp)
print(type(tsdr.index))

jd_ts = jddf.set_index(pd.to_datetime(jddf['time']))
print(type(jd_ts.index))
print(jd_ts.head())


# 索引与切片
print(jd_ts['2017-02'])
print(jd_ts['2017-02':'2017-03'])  # Empty
print(jd_ts.truncate(after='2017-01-06'))
print(jd_ts[['opening_price', 'closing_price']].truncate(after='2017-01-20', before='2017-01-13'))  # Empty


# 范围和偏移量
'''
pd.date_range(start=None, end=None, periods=None, freq='D', tz=None, normalize=False, name=None, closed=None)
start:时间日期字符串指定起始时间日期
end:时间日期字符串指定终止时间日期
periods:时间日期的个数
freq:时间日期的频率
tz:时区
normalize:生成日期范围之前 将开始/结束日期标准化为午夜
name:命名时间日期索引
closed:生成的时间日期索引是/否包含start和end
'''
print(pd.date_range(start='2017/07/07', periods=3, freq='M'))
print(pd.date_range('2017/07/07', '2018/07/07', freq='BMS'))

'''
B       工作日                  Q       季度末
C       自定义工作日            QS      季度初
D       日历日                  BQ      季度末工作日
W       周                      BQS     季度初工作日
M       月末                    A       年末
SM      半月及月末              BA      年末工作日
BM      月末工作日              AS      年初
CBM     自定义月末工作日        BAS     年初工作日
MS      月初                    BH      工作小时
SMS     月初及月中              H       小时
BMS     月初工作日              T,min   分钟
CBMS    自定义月初工作日        S       秒
                                L,ms    毫秒
                                U,us    微秒
                                N       纳秒
'''

print(pd.date_range('2017/07/07', periods=10, freq='1D2h20min'))
print(pd.date_range('2017/07/07', '2018/01/22', freq='W-WED'))

ts_offset = pd.tseries.offsets.Week(1) + pd.tseries.offsets.Hour(8)
print(ts_offset)
print(pd.date_range('2017/07/07', periods=10, freq=ts_offset))

# 时间移动及运算
sample = jd_ts['2017-01-01': '2017-01-10'][['opening_price', 'closing_price']]
print(sample)
# 将时序数据向后移2期
print(sample.shift(2))
# 将时序数据按天向前移2天
print(sample.shift(-2, freq='1D'))
# 时间序列运算
date = pd.date_range('2017/01/01', '2017/01/08', freq='D')
s1 = pd.DataFrame({'opening_price': np.random.randn(8), 'closing_price': np.random.randn(8)}, index=date)
print(s1)
print(s1 + sample)

# 频率转换及重采样
sample.asfreq(freq='D')
# 重采样
# 按照12小时频率进行上采样,并指定缺失值按当日最后一个有效观测值来填充