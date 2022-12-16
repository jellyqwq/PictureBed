# 请在______处使用一行代码或表达式替换
#该模板仅是提示作用，你可以全部删除重新作答，输出一致即可正确得分。
#请删除横线， 不要在横线上作答。


n = eval(input("请输入数量："))
percost = 160
if n == 1:
    x = 1
elif 2 <= n <= 4:
    x = 0.9
elif 5 <= n <= 9:
    x =0.8
elif n >= 10:
    x = 0.7
cost = x*percost*n
print("总额为:",int(cost))
