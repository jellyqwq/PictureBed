#
# 编写代码替换横线
#

n = eval(input("请输入一个整数："))
for i in range(1,n):
    for j in range(1,n):
        if j >= i:
            print(j,end=' ')
    print()