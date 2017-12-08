import statsmodels.api as sm
import numpy as np
import pandas as pd

from scipy import stats
from numpy import array



pop = np.array([2, 4, 6, 8])
# 总体方差
print(pop.var(ddof=0))
# 总体均值
print(pop.mean())

miu = np.array([2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 8])
print(miu.var(ddof=0))
print(miu.mean())



# 单总体均值的参数估计
moisture = pd.read_csv('moisture.csv')
print(moisture.head())
# 正态估计区间
print(sm.stats.DescrStatsW(moisture['moisture']).zconfint_mean(alpha=0.05))
# t分布的估计区间
print(sm.stats.DescrStatsW(moisture['moisture']).tconfint_mean(alpha=0.05))
# t分布下的均值估计结果
moisture_mean, moisture_var, moisture_std = stats.bayes_mvs(moisture['moisture'], alpha=0.95)
print(moisture_mean)

# 单总体方差
print(moisture_var)
# 单总体标准差
print(moisture_std)

m, v, s = stats.mvsdist(moisture['moisture'])
# 95%置信度下总体均值的置信区间
print(m.interval(0.95))
# 95%置信度下总体方差的置信区间
print(v.interval(0.95))
# 95%置信度下总体标准差的置信区间
print(s.interval(0.95))
# 均值的估计标准误差
print(m.std())


print(sm.stats.proportion_confint(95, 100, alpha=0.01, method='binom_test'))
# 总体均值Z检验
print(sm.stats.DescrStatsW(moisture['moisture']).ztest_mean(value=4, alternative='larger'))


mobile = pd.read_csv('mobile.csv')
print(mobile.head())
# 检测单侧P值