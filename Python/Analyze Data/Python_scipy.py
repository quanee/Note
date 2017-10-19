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
