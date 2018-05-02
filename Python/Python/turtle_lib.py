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
color() 设置画笔的颜色
begin_fill() 填充图形前，调用该方法
end_fill() 填充图形结束
filling() 返回填充的状态，true为填充，false为未填充
clear() 清空当前窗口，但不改变当前画笔的位置
reset() 清空当前窗口，并重置位置等状态为默认值
screensize() 设置画布的长和宽
hideturtle() 隐藏画笔的turtle形状
showturtle() 显示画笔的turtle形状
isvisble() 如果turtle可见，则返回ture
wirte() 输出font字体的字符串
'''

turtle.pensize(3)
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.circle(40, steps=3)

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps=4)

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(40, steps=5)

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.circle(40, steps=6)

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.circle(40)
turtle.down()
