# 请在______处使用一行代码或表达式替换
#该模板仅是提示作用，你可以全部删除重新作答，输出一致即可正确得分。
#请删除横线， 不要在横线上作答。
a, b, c = tuple(input().split(','))
ls = []
for i in range(int(c)):
    ls.append(int(a)+int(b)*i)
print(ls)

