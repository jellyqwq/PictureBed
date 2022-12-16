# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

f = open('命运.txt', 'r', encoding='utf-8')
s = f.read()
for c in '\n，。！？“”‘’、；：':
    s = s.replace(c, '')
d = {}
for c in s:
    d[c] = d.get(c,0) + 1
l=list(d.items())
l.sort(key = lambda x:x[1], reverse=True)
print("{}:{}".format(l[0][0],l[0][1]))
