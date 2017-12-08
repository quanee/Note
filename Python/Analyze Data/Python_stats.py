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


