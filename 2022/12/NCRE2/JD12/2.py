#
# 在____________上补充代码
#


import time
t = input("请输入一个浮点数时间信息: ")
s = time.ctime(eval(t))
ls = s.split()
print(ls[3].split(':')[0])
