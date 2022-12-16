#
# 编写代码替换横线
#

s = input("请输入5个小写字母：")
sl = [i.upper() for i in s]
print(','.join(sl[::-1]))
