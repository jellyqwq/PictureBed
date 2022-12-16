# 请在______处使用一行代码或表达式替换
#该模板仅是提示作用，你可以全部删除重新作答，输出一致即可正确得分。
#请删除横线， 不要在横线上作答。
import random
random.seed(0)
s = 0
for i in range(5):
    n = random.randint(1, 97)  # 产生随机数
    s += n**2
print(s)
