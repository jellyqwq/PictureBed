#
# 在____________上补充代码
#


s = input("请输入一组数据: ")
ls = s.split(',')
lt = []
for i in ls:
    lt.append(int(i))
print(max(lt))
