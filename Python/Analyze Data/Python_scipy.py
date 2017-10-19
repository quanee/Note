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