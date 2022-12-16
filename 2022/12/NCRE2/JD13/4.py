from turtle import *

color = ['red', 'green', 'blue']
rs = [10, 30, 60]

for i in range(3):
    penup()
    goto(0,-rs[i])
    pendown()
    pencolor(color[i])
    circle(rs[i])
done()