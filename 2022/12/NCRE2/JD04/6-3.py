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
search = input('请输入星座序号（例如，5）：')
while True:
    sli = search.split(' ')
    for i in sli:
        for j in ls:
            if 1 <= int(i) <= 12:
                if i == j[0]:
                    print("{}({})的生日是{}月{}日至{}月{}日之间".format(j[1], j[6], j[2], j[3], j[4], j[5]))
            else:
                print("输入星座序号有误！")
                break
    search = input('请输入星座序号（例如，5）：')


