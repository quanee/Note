import numpy as np
import pandas as pd
from scipy import stats


# 统计量
# 集中趋势
# 均值
stock = np.dtype([('name', np.str_, 4), ('time', np.str_, 10), ('opening_price', np.float64), ('closing_price', np.float64), ('lowest_price', np.float64), ('highest_price', np.float64), ('volume', np.int32)])
jd_stock = np.loadtxt('data.csv', delimiter=',', dtype=stock)
jddf = pd.read_table('data.csv', sep=',', header=None, names=['name', 'time', 'opening_price', 'closing_price', 'lowest_price', 'highest_price', 'volume'])
# 样本平均值
print(np.mean(jd_stock['opening_price']))
# 加权平均值
print(np.average(jd_stock['opening_price']))
print(np.average(jd_stock['closing_price'], weights=jd_stock['volume']))
print(jddf['opening_price'].mean())

# 截尾均值(去掉头尾若干最大最小的数据)
print(stats.tmean(jddf['opening_price']))
print(stats.tmean(jddf['opening_price'], (25, 30)))  # 截尾的上, 下界

# 缩尾均值(把原始数据中最小的N个值用第N+1小的数值替换, 最大的N个值用第N+1大的数值替换)
print(stats.mstats.winsorize(jddf['opening_price'], (0.05, 0.05)).mean())
# 几何平均数
print(stats.gmean(jddf['opening_price']))
# 调和平均数
print(stats.hmean(jddf['opening_price']))

# 中位数
print(np.median(jd_stock['opening_price']))
print(jddf['opening_price'].median())
# print(stats.nanmedian(jddf['opening_price']))

# 分位数
# 计算指定分位点的分位数
print(stats.scoreatpercentile(jddf['opening_price'], [10, 20, 25, 50, 75, 100]))
# 计算指定数值所处的分位点
print(stats.percentileofscore(jddf['opening_price'], 30.27))

print(stats.mstats.mquantiles(jddf['opening_price'], prob=0.50))
print(stats.mstats.hdquantiles(jddf['opening_price'], prob=0.50))

# 众数
m = np.array([1, 2, 3, 4, 3, 2, 3, 3, 4, 4, 4, 7, 8])
print(stats.mode(m))
print(stats.mode(jd_stock['opening_price']))
print(stats.mode(jddf['opening_price']))
# 错误
m1 = np.array([1, 2, 3, 4, 7, 8])
print(stats.mode(m1))

md = pd.DataFrame(m)
print(md.mode())

md1 = pd.DataFrame(m1)
print(md1.mode())

# 离散程度
# 极差
print(np.ptp(jd_stock['opening_price']))
print(np.max(jd_stock['opening_price']) - np.min(jd_stock['opening_price']))
print(jddf['opening_price'].max() - jddf['opening_price'].min())
print(stats.mstats.mquantiles(jddf['opening_price'], prob=1) - stats.mstats.mquantiles(jddf['opening_price'], prob=0))

# 四分位差
print(stats.scoreatpercentile(jddf['opening_price'], 75) - stats.scoreatpercentile(jddf['opening_price'], 25))

# 方差和标准差
print(np.var(jd_stock['opening_price'], ddof=1))
print(jd_stock['opening_price'].var(ddof=1))
print(np.std(jd_stock['opening_price'], ddof=1))
print(jddf['opening_price'].var(), jddf['opening_price'].std())
# print(stats.tvar(jddf['opening_price']), stats.nanstd(jddf['opening_price']))

# 协方差
print(np.cov((jd_stock['opening_price'], jd_stock['closing_price']), bias=1, ddof=1))
print(jddf['opening_price'].cov(jddf['closing_price']))

# 变异系数
cv = jd_stock['closing_price'].var() / jd_stock['closing_price'].mean()
print('CV of closing_price:', cv)


# 分布形状
# 偏度(数据分布对称性的测度  K=E(x-u)^3/o^3)
print(jddf['opening_price'].skew())
print(stats.skew(jddf['opening_price'], bias=False))

# 峰度(反映数据分布曲线陡峭或扁平程度的指标)
print(jddf['opening_price'].kurt())
print(stats.kurtosis(jddf['opening_price'], bias=False))



# 统计表
print(jddf.describe())
print(stats.describe(jddf[['opening_price', 'closing_price', 'lowest_price', 'highest_price', 'volume']]))
# 统计表的编制
storesales = pd.read_csv('storesales.csv')
print(storesales.head())

storesales['store'] = storesales['store'].astype('category')
storesales['store'].cat.categories = ['SANFORD', 'MILLENIA', 'OCOEE', 'KISSIMMEE']
storesales['store'].cat.set_categories = ['SANFORD', 'MILLENIA', 'OCOEE', 'KISSIMMEE']
storesales['method'] = storesales['method'].astype('category')
storesales['method'].cat.categories = ['On Line', 'In Store']
storesales['method'].cat.set_categories = ['On Line', 'In Store']

storesales_grouped = storesales.groupby(storesales['method'])
print(storesales_grouped['sales', 'orders'].agg('sum'))

'''
pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')
data: 指定为pandas中的DataFrame
index, columns, values: 分别对应数据透视表中的行,列和值, 他们都应当是data所指定DataFrame中的列
aggfunc: 指定汇总的函数, 默认为mean函数