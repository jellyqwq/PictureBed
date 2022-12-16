# 请在______处使用一行代码或表达式替换
#该模板仅是提示作用，你可以全部删除重新作答，输出一致即可正确得分。
#请删除横线， 不要在横线上作答。

def F(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return F(x-1)+F(x-2)

y = 0
n = 0
while True:
    y = F(n)
    if y > 100:
        break
    print(y, end=',')
    n += 1
