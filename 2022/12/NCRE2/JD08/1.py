# 请在______处使用一行代码或表达式替换
#该模板仅是提示作用，你可以全部删除重新作答，输出一致即可正确得分。
#请删除横线， 不要在横线上作答。
a = [3,6,9]
b = eval(input()) #例如：[1,2,3]
x = []
for i in range(len(a)):
    x.append(b[i])
    x.append(a[i])
x.extend(b[len(a):])
print(x)
