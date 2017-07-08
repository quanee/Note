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
mux = 0
muy = 0
sx = 1
sy = 1
z = (1 / (2 * 3.1415926535 * sx * sy * np.sqrt(1 - r * r))) * np.exp((-1 / (2 * (1 - r * r))) * (((x - mux) ** 2) / (sx ** 2) - 2 * r * (x - mux) * (y - muy) / (sx * sy) + ((y - muy) ** 2) / (sx ** 2)))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.Greys)
# plt.show()
clf_cla_close(plt)


# 绘制随机折线图
plt.plot(np.random.randn(100), linewidth=2.0)
# plt.show()
clf_cla_close(plt)


# jd_stock
plt.plot(jd_stock['opening_price'])
# plt.show()
clf_cla_close(plt)


# 图像基本设置
# 创建图例
plt.plot(jd_stock['opening_price'], label='Opening Price')
plt.plot(jd_stock['closing_price'], label='Closing Price')
# fromeon是否有框
plt.legend(loc='lower right', frameon=False)
'''
图例标位置参数
    upper right: 1
    upper left: 2
    lower left: 3
    lower right: 4
    right: 5
    center left: 6
    center right: 7
    lower center: 8
    uppercenter: 9
    center: 10
'''
# plt.show()
clf_cla_close(plt)

# 刻度设置
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C, '--')
plt.plot(X, S)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

# 图像注解
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle='--')
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')

plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$', xy=(t, np.sin(t)), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle='--')
plt.scatter([t, ], [np.sin(t), ], 50, color='red')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$', xy=(t, np.cos(t)), xycoords='data', xytext=(-90, -50), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
clf_cla_close(plt)


# 图像大小
plt.plot(jd_stock['opening_price'], label='Opening Price')
plt.plot(jd_stock['closing_price'], label='Closing Price')
plt.legend(loc='upper left', frameon=True)
plt.xticks([xticks for xticks in range(71)], list(jd_stock['time']), rotation=40)
# 设置图像对象名为fig
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
# 显示网格
plt.grid()
clf_cla_close(plt)
