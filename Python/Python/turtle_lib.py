import turtle
import time
'''
控制画笔绘制状态的方法
pendown() 放下画笔，移动指定点后继续绘制
penup() 提起画笔，用于另起一个地方绘制时用，与pendown()配对使用
pensize(widh) 设置画笔线条的粗细为指定大小

turtle运动方法
forward() 沿着当前方向前进指定距离
backward() 沿着当前相反方向后退指定距离
right(angle) 向右旋转angle角度
left(angle) 向左旋转angle角度
goto(x,y) 移动到绝对坐标（x，y）处
setx() 将当前x轴移动到指定位置
sety() 将当前y轴移动到指定位置
setheading(angle) 设置当前朝向为angle角度
home() 设置当前画笔位置为原点，朝向东
circle() 绘制一个指定半径，角度，以及步骤的圆圈
dot(r) 绘制一个指定直径和颜色的原点
undo() 撤销画笔最后一步动作
speed() 设置画笔的绘制速度，参数为0-10之间

turtle颜色和字体绘制方法