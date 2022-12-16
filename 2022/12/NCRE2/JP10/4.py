#在_____完善一行代码

import turtle
turtle.color('red','yellow') #画笔颜色与填充设置
turtle.begin_fill()
#绘制太阳花形状
for i in range(50):
    turtle.fd(200) #先前200
    turtle.right(170)  #右转170度
turtle.end_fill()
turtle.done()