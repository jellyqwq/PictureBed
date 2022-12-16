# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

f = open('PY301-SunSign.csv', 'r', encoding='utf-8')
ls = []
f.readline()
for i in f:
    l = []
    b = i.strip('\n').split(',')
    b[1] = b[1].strip()
    l.append(b[0])
    l.append(b[1])
    l.extend([b[2][:-2], b[2][-2:]])
    l.extend([b[3][:-2], b[3][-2:]])
    l.append(b[4])
    ls.append(tuple(l))
search = input('请输入星座中文名称（例如，双子座）：')
for i in ls:
    if i[1] == search:
        print("{}的生日位于{}-{}之间".format(search,i[2]+i[3], i[4]+i[5]))


