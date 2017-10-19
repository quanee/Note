import numpy as np
import pandas as pd
from scipy import stats


# 统计量
# 集中趋势
# 均值
stock = np.dtype([('name', np.str_, 4), ('time', np.str_, 10), ('opening_price', np.float64), ('closing_price', np.float64), ('lowest_price', np.float64), ('highest_price', np.float64), ('volume', np.int32)])