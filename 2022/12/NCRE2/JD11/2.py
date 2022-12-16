#
# 在____________上补充代码
#

s = input("请输入中文和字母的组合: ")
count =0
for c in s:
    if c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 \n':
        count += 1
print(count)
