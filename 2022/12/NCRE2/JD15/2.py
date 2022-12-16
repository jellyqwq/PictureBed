#
# 编写代码替换横线
#

myinput = input("") #请输入：
ls = myinput.split(',')
s = 0
for c in ls:
    if c.strip(" ").isdigit():
        s += int(c.strip(" "))
print("数字和是：" + str(s))