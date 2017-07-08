from __future__ import division
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as mping
import jieba
import plotly
import plotly.plotly as py
import seaborn as sns

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.font_manager import FontProperties
from PIL import Image
from pandas.plotting import table
from pandas.plotting import scatter_matrix
from pandas.plotting import radviz
from pandas.plotting import parallel_coordinates
from pandas.plotting import andrews_curves
from wordcloud import WordCloud
from scipy.misc import imread
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from wordcloud import ImageColorGenerator



def clf_cla_close(p):
    p.clf()  # 清除图像
    p.cla()  # 清除坐标
    p.close()  # 关闭图像



# 图像中文乱码
myfont = FontProperties(fname='/usr/share/fonts/user_font/simhei.ttf')
stock = np.dtype([('name', np.str_, 4), ('time', np.str_, 10), ('opening_price', np.float64), ('closing_price', np.float64), ('lowest_price', np.float64), ('highest_price', np.float64), ('volume', np.int32)])
jd_stock = np.loadtxt('data.csv', delimiter=',', dtype=stock)
jddf = pd.read_table('data.csv', sep=',', header=None, names=['name', 'time', 'opening_price', 'closing_price', 'lowest_price', 'highest_price', 'volume'])
jddf['Market'] = list(map(lambda x: 'Good' if x > 0 else ('Bad' if x < 0 else 'OK'), jddf['closing_price'] - jddf['opening_price']))


# 绘制一条从(0, 0)到(1, 1)的直线
plt.plot([0, 1], [0, 1])
# 设置图形标题
plt.title('a strait line')
# 设置x轴标签
plt.xlabel('x value')
# 设置y轴标签
plt.ylabel('y value')
# 显示图像
# plt.show()
clf_cla_close(plt)
# 存储图像
# plt.savefig('Python_matplotlib.svg', bbox_inches='tight')

# 创建多项式 (2x^4 - 3.5x^3 + 1.6x^2 - 2x + 9)
a = np.array([2, -3.5, 1.6, -2, 9])
p = np.poly1d(a)
print(p)

# 创建x轴数值 在-10~10之间产生30个服从均匀分布的随机数
x = np.linspace(-10, 10, 30)
# 利用多项式创建多项式的值
y = p(x)
# plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
# plt.show()
clf_cla_close(plt)

# p的一阶导函数
p1 = p.deriv(m=1)
y1 = p1(x)
plt.plot(x, y, x, y1)
# plt.show()
clf_cla_close(plt)

# 'b|'表示绘制以竖线为数据点的蓝色曲线 'k-.'为黑色点线
# plt.plot(x, y, 'b| ', x, y1, 'k-.')
# plt.show()

u = np.linspace(-3, 3, 30)
x, y = np.meshgrid(u, u)
r = 0.6