#
# 在____________上补充代码
#


s = input("请输入一个小数: ")
s = s[::-1]
cs =0
for c in s:
    if c == '.':
        break
    cs += eval(c)
print('{:*>10}'.format(cs))



