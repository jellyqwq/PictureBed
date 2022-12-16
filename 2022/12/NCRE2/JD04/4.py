# 请在______处使用一行或多行代码替换
# 注意：请不要修改其他已给出代码
#该题系统无法图形识别，评阅默认正确，请自己核对答案。

import turtle
turtle.pensize(2)
d = -45
for i in range(4):
    turtle.seth(d)
    d  += 90
    turtle.fd(200)