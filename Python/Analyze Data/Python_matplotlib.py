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


# 创建子图
x = np.linspace(-10, 10, 30)
y = p(x)
p2 = p.deriv(m=2)
y2 = p2(x)
p3 = p.deriv(m=3)
y3 = p3(x)
plt.subplot(221)  # 2行2列第1个

plt.plot(x, y)
plt.title('Polynomial')
plt.subplot(222)
plt.plot(x, y1, 'r')
plt.title('First Derivative')
plt.subplot(223)
plt.plot(x, y2, 'r')
plt.title('Second Derivative')
plt.subplot(224)
plt.plot(x, y3, 'r')
plt.title('Third Derivative')
plt.subplots_adjust(hspace=0.4, wspace=0.3)
clf_cla_close(plt)


# 其他绘图函数
x = np.linspace(-10, 10, 30)
y = p(x)
x1 = jddf['opening_price']
y1 = jddf['closing_price']
plt.figure(figsize=(10, 6))

plt.subplot(231)
plt.plot(x, y)
plt.title('折线图', fontproperties=myfont)

plt.subplot(232)
plt.scatter(x1, y1)
plt.title('散点图', fontproperties=myfont)

plt.subplot(233)
plt.pie(y)
plt.title('饼图', fontproperties=myfont)

plt.subplot(234)
plt.bar(x, y)
plt.title('直方图', fontproperties=myfont)

x2 = y2 = np.arange(-5.0, 5.0, 0.005)
X, Y = np.meshgrid(x2, y2)
Z = Y + X ** 2

plt.subplot(235)
plt.contour(X, Y, Z)
plt.colorbar()
plt.title('等高线图', fontproperties=myfont)

img = mping.imread('logo.png')

plt.subplot(236)
plt.imshow(img)
plt.title('调用已有图片', fontproperties=myfont)
plt.subplots_adjust(hspace=0.25)

clf_cla_close(plt)


# 面向对象绘图
'''
fig.set_alpha(0.2 * fig.get_alpha())
fig.set(alpha=0.2, zorder=2)
# gca(): 返回当前的Axes实例本身
# gcf(): 返回当前Figure实例本身
'''
# 防止图形叠加
fig = Figure()
canvas = FigureCanvas(fig)

# 指定图像在子图中的位置
ax1 = fig.add_axes([0.1, 0.6, 0.2, 0.3])

line = ax1.plot([0, 1], [0, 1])
ax1.set_title('Axes2')

ax2 = fig.add_axes([0.4, 0.1, 0.4, 0.5])
# 绘制散点图
sc = ax2.scatter(jd_stock['opening_price'], jd_stock['closing_price'])
ax2.set_title('Axes2')
sc.set(alpha=0.2, zorder=2)

# 将figure对象以指定的文件存储
canvas.print_figure('figure_line&scatter.png')
# 将所存储图片显示
# Image.open('figure_line&scatter.png').show()
clf_cla_close(plt)

# 绘图样式
# 查看所有样式
print(plt.style.available)
plt.style.use('ggplot')
plt.plot(jd_stock['opening_price'], label='Opening Price')
plt.plot(jd_stock['closing_price'], label='Closing Price')
plt.legend(loc=8, frameon=False, bbox_to_anchor=(0.5, -0.3))
# plt.show()

# 恢复默认风格
plt.style.use('default')
clf_cla_close(plt)



'''
pandas基本绘图
语法:
pandas对象.plot(x=None, y=None, kind='line', ax=None, subplots=False, sharex=None, sharey=False, layout=None, figsize=None, use_index=True, title=None, grid=None, legend=True, style=None, logx=False, logy=False, loglog=False, xticks=None, colormap=None, table=False, yerr=None, xerr=None, secondary_y=False, sort_columns=False, **kwargs)
'kind'指定可绘制的图形类型:
    'line': 折线图
    'bar': 竖直条形图
    'barh': 水平条形图
    'hist': 直方图
    'box': 盒须图
    'kde': 核密度估计曲线图
    'density': 同'kde'
    'area': 面积图
    'pie': 饼图
    'scatter': 散点图
    'hexbin': 六边形箱图
其他参数:
    x: 指定x轴标签或位置
    y: 指定y轴标签或位置
    ax: matplotlib的轴对象
    subplots: True或False 是否为每列单独绘制一副图 默认把所有列绘制在一个图形中
    sharex: True或False 是否共享x轴 默认False
    sharey: True或False 是否共享y轴 默认False
    layout: 用一个元组来设计子图的布局
    figsize: 用一个元组来设置图像的尺寸
    use_index: True或False 是否使用索引作为x轴的刻度 默认False
    title: 设置图形的标题
    grid: True或False 是否设置图形网格线 默认False
    legend: True或False或reverse 放置图例
    style: 使用列表或字典分别为每一列设置matplotlib绘制线条的风格
    logx: True或False 将x轴对数化 默认False
    logy: True或False 将y轴对数化 默认False
    loglog: True或False 将x轴和y轴同时对数化 默认False
    xticks: 使用一个序列设置x轴的刻度
    yticks: 使用一个序列设置y轴的刻度
    xlim: 使用2个元素的元组/列表设置x的上下界
    ylim: 使用2个元素的元组/列表设置y的上下界
    rot: 使用一个整数来设置刻度的旋转方向
    fontsize: 使用一个整数来设置x轴和y轴刻度的字号
    colormap: 设置图像的色系
    colorbar: True或False 如设置True 则绘制colorbar
    position: 用一个浮点数来设置图形的相对位置 取值从0到1 默认值为0.5
    table: True或False 设置图形中是否绘制统计表
    yerr和xerr: True或False 绘制残差图
    stacked: True或False 绘制堆积图形
    sort_columns: True或False 对图形列的名称进行排序放置 默认False
    secondary_y: True或False 是否放置第2个y轴 默认不放置
    mark_right: True或False 当使用第2个y轴时 自动在图例中标记为right 默认False
    kwds: 选项关键字
'''



# 基本统计图形
# 折线图
plt.plot(jddf['opening_price'])

# 计算开盘价的5期移动平均
meanop = jddf['opening_price'].rolling(5).mean()
stdop = jddf['opening_price'].rolling(5).std()
plt.plot(range(71), jddf['opening_price'])
plt.fill_between(range(71), meanop - 1.96 * stdop, meanop + 1.96 * stdop, color='b', alpha=0.2)
clf_cla_close(plt)

# pandas的plot方法绘图
jddf = jddf.set_index('time')
jddf[['opening_price', 'closing_price']].plot(use_index=True, grid=True)
clf_cla_close(plt)

# pandas的plot方法绘制第2个y轴
jddf['closing_price'].plot(use_index=True, grid=True)
jddf['volume'].plot(use_index=True, secondary_y=True, grid=True)
clf_cla_close(plt)

# 绘制自带统计量图
fig, ax = plt.subplots(1, 1)
table(ax, np.round(jddf[['opening_price', 'closing_price']].describe(), 2), loc='upper right', colWidths=[0.2, 0.2])
jddf.plot(ax=ax, ylim=(25, 45))
plt.legend(loc='upper left', frameon=False)
fig.set_size_inches(9, 6)
clf_cla_close(plt)

# 面积图
jddf[['opening_price', 'closing_price', 'highest_price', 'lowest_price']].plot.area(ylim=(25, 35), stacked=False, cmap='tab10_r')
clf_cla_close(plt)

# 直方图
# 参数: 待绘制的定量数据 划分区间个数
plt.hist(jddf['opening_price'], 10)
plt.xlabel('Opening Price')
plt.ylabel('Frequency')
plt.title('Opening Price of JD Stock')
clf_cla_close(plt)
# pandas对象使用hist和plot方法绘制直方图
jddf['opening_price'].hist()
clf_cla_close(plt)

jddf[['opening_price', 'closing_price']].plot(kind='hist', alpha=0.5, colormap='tab10_r', bins=8)
plt.legend(loc=8, frameon=False, bbox_to_anchor=(0.5, -0.3))
clf_cla_close(plt)

# 利用hist方法中的by参数指定分类变量按照其分类分别绘制图形
jddf[['opening_price', 'closing_price']].hist(by=jddf['Market'], stacked=True, bins=8, color=['gray', 'lightblue'])


# 条形图
N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)
width = 0.45

p1 = plt.bar(ind, menMeans, width, color='grey', yerr=menStd)
p2 = plt.bar(ind, womenMeans, width, color='lightblue', bottom=menMeans, yerr=womenStd)
clf_cla_close(plt)


# 数据集
salary_fmt = np.dtype([('position', np.str_, 8), ('id', np.int32), ('gender', np.str_, 1), ('education', np.int32), ('salary', np.float64), ('begin_salary', np.float64), ('jobtime', np.int32), ('age', np.int32)])
salary = pd.DataFrame(np.loadtxt('salary.csv', delimiter=',', skiprows=1, dtype=salary_fmt))
print(salary.head())

# 绘制不同职位人员分布的条形图
# 创建一个字典 对职称的每一个类型进行频数统计
gradeGroup = {}

for grade in salary['position']:
    gradeGroup[grade] = gradeGroup.get(grade, 0) + 1

xt = gradeGroup.keys()
xv = gradeGroup.values()
# bar函数创建条形图
# #1: 柱的横坐标 #2: 柱的高度 align: 条或柱的对齐方式
plt.bar(range(3), [gradeGroup.get(xticks, 0) for xticks in xt], align='center', color='lightblue')

# 设置条或柱的文字说明
# 1#: 文字说明的横坐标 #2: 文字说明内容 #3: 设置排列方向
plt.xticks((0, 1, 2), xt, rotation='horizontal')
plt.xlabel('position')
plt.ylabel('frequency')
plt.title('job position')


def autolabel(rects):
    # 为条形图中的条挂上数据标签
    i = -1
    for rect in rects:
        i += 1
        # 1, 2#: 数据值标签在x, y轴上的坐标 3#: 数据值标签
        plt.text(i, rect - 10, '%d' % rect, ha='center', va='bottom')


autolabel(xv)
clf_cla_close(plt)


# 分类对比条形图
plt.figure()
count_f = [206, 0, 10]
count_m = [-157, -71, -27]
plt.barh(range(3), count_f, color='r', alpha=.5, label='female')
plt.barh(range(3), count_m, color='b', alpha=.5, label='male')
plt.yticks(range(3), xt)
plt.legend(loc=1)
plt.axvline(0, color='k')
clf_cla_close(plt)

# pandas绘制
salary['position'].value_counts().plot.bar(rot=0, colormap='summer')
clf_cla_close(plt)
crosssalary = pd.crosstab(salary['position'], salary['gender'])
crosssalary.columns = ['female', 'male']
crosssalary.plot.bar(rot=0, colormap='autumn', stacked=True)
clf_cla_close(plt)


# 龙卷风图
yt = ('student', 'employee', 'worker', 'manager', 'lawyer', 'driver', 'fireman', 'singer', 'composer', 'professor', 'journalist')
count_f = [78, 70, 90, 110, 80, 110, 150, 120, 196, 180, 220]
count_m = [-10, -21, -27, -34, -89, -84, -78, -90, -100, -123, -212]
plt.barh(range(11), count_f, color='r', alpha=.5, label='female')
plt.barh(range(11), count_m, color='b', alpha=.5, label='male')
plt.yticks(range(11), yt)
plt.xticks([-150, 150], ['male', 'female'])
clf_cla_close(plt)

# 饼图
sizes = {}
total = sum(gradeGroup.values())
explode = (0, 0.3, 0)
colors = ['yellowgreen', 'gold', 'lightskyblue']
for i in xt:
    sizes[i] = gradeGroup[i] / total

plt.pie(sizes.values(), labels=sizes.keys(), explode=explode, autopct='%1.2f%%', colors=colors, shadow=True, startangle=45)
clf_cla_close(plt)

# pandas饼图
piedf = pd.DataFrame({'percent of position': [0.7707, 0.0573, 0.17201]}, index=['employee', 'director', 'manager'])
piedf['percent of position'].plot.pie(colors=colors, labeldistance=0.85, autopct='%1.2f%%', fontsize=12, explode=explode, startangle=45)
piedf['percent of position'].plot(kind='pie', labeldistance=0.85, colors=colors, autopct='%1.2f%%', fontsize=12, explode=explode, startangle=45)
clf_cla_close(plt)


# 阶梯图
# 1#: 绘制的定量数据 2#: 划分的区间数 density: 参数是否无量纲化 histtype: 绘制阶梯状曲线
plt.hist(salary['salary'], 10, density=True, histtype='step', cumulative=True)
plt.xlabel('current salary')
plt.ylabel('frequency')
plt.title('salary of U.S. enterpriceses')
clf_cla_close(plt)

# pandas阶梯图
salary['salary'].plot.hist(bins=10, density=True, histtype='step', cumulative=True)
plt.xlabel('current salary')
plt.ylabel('frequency')
plt.title('salary of U.S. enterpriceses')
clf_cla_close(plt)


# 盒须图
# 1#: 数据 2#: 盒子形状 0默认矩形 1凹型 3#: 异常值数据标志形状 4#: 绘制水平盒须图
plt.boxplot(salary['salary'], 1, 'r', 0, labels=['current salary'])
plt.title('salary of U.S. enterpriceses')
clf_cla_close(plt)

plt.boxplot([salary['salary'], salary['begin_salary']])
plt.title('salary of U.S. enterpriceses')
combinebox = plt.subplot(111)
combinebox.set_xticklabels(['current salary', 'begin_salary'])
clf_cla_close(plt)

jd_box_data = [jd_stock['opening_price'], jd_stock['closing_price'], jd_stock['highest_price'], jd_stock['lowest_price']]
bplot = plt.boxplot(jd_box_data, vert=True, patch_artist=True)

# 盒子上色
colors = ['pink', 'lightblue', 'lightgreen', 'cyan']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

combinebox = plt.subplot(111)
combinebox.set_xticklabels(['opening_price', 'closing_price', 'highest_price', 'lowest_price'])
clf_cla_close(plt)

colors = dict(boxes='lightgreen', whiskers='lightblue', medians='lightgreen', caps='cyan')
bplot = jddf[['opening_price', 'closing_price', 'highest_price', 'lowest_price']].plot.box(color=colors, vert=False, positions=[1, 3, 4, 8], patch_artist=True)
clf_cla_close(plt)


# 小提琴图
axex = plt.subplots(nrows=1, ncols=1, figsize=(8, 5))
vplot = plt.violinplot(jd_box_data, showmeans=False, showmedians=True)
colors = ['pink', 'lightblue', 'lightgreen', 'yellow']
for patch, color in zip(vplot['bodies'], colors):
    patch.set_facecolor(color)

plt.grid(True)
plt.xticks([1, 2, 3, 4], ['opening_price', 'closing_price', 'highest_price', 'lowest_price'])
clf_cla_close(plt)


# 散点图
plt.scatter(salary['salary'], salary['begin_salary'], c='darkblue', alpha=0.4)
plt.xlabel('current salary')
plt.ylabel('begin_salary')
clf_cla_close(plt)

# pandas绘制散点图
salary.plot.scatter(x='salary', y='begin_salary', c='cyan', alpha=0.45)
clf_cla_close(plt)

# 叠加散点图
sc1 = jddf.plot.scatter(x='opening_price', y='closing_price', c='blue', label='opening & closing')
# ax#: 把指定的scl绘图对象叠加到本次所绘的图形中
jddf.plot.scatter(x='highest_price', y='lowest_price', c='red', label='highest & lowest', ax=sc1)
clf_cla_close(plt)
# c#: 使用其他变量标注散点
jddf.plot.scatter(x='opening_price', y='closing_price', cmap='Blues_r', c='volume', grid=True)
clf_cla_close(plt)

# 散点图矩阵
scatter_matrix(jddf[['opening_price', 'closing_price', 'highest_price', 'lowest_price']], alpha=0.5, figsize=(9, 9), diagonal='kde')
clf_cla_close(plt)
# 概率密度曲线图
jddf['opening_price'].plot(kind='kde')
clf_cla_close(plt)


# 气泡图(散点图延伸 气泡越大数值越大)
colors = np.random.rand(71)
plt.scatter(jd_stock['opening_price'], jd_stock['closing_price'], marker='o', c=colors, s=jd_stock['volume'] / 10000, alpha=0.6)
plt.xlabel('opening_price', fontsize=12)
plt.ylabel('closing_price', fontsize=12)
clf_cla_close(plt)


# 六边形箱图(蜂窝图)
# pandas绘图
# gridsize#: x轴方向分箱数目 默认100
salary.plot.hexbin(x='salary', y='begin_salary', gridsize=25)
clf_cla_close(plt)
# 描述类似气泡图的散点值
salary.plot.hexbin(x='salary', y='begin_salary', C='age', reduce_C_function=np.min, gridsize=25)
clf_cla_close(plt)


# 雷达坐标图(属性图)
fig = plt.figure()
# 1#: 要分析对象 2#: 分类变量
radviz(salary[['salary', 'begin_salary', 'age', 'education', 'jobtime', 'position']], 'position')
clf_cla_close(plt)


# 轮廓图(横坐标表示需要分析的变量 纵坐标各个指标的值)
# 1#: 要分析对象 2#: 分类变量
parallel_coordinates(salary[['salary', 'begin_salary', 'jobtime', 'position']], 'position')
clf_cla_close(plt)


# 调和曲线图(根据三角变换方法将高维空间上的点映射到二维平面的曲线上)
andrews_curves(salary[['salary', 'begin_salary', 'jobtime', 'position']], 'position')
clf_cla_close(plt)


# 等高线图
u = np.linspace(-3, 3, 30)
x, y = np.meshgrid(u, u)