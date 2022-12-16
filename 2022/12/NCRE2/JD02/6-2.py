# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

d = {}
with open('earpa001.txt', 'r', encoding='utf-8') as fi:
    li = fi.readlines()
for i in li:
    a = i.strip('\n').split(',')
    key = f'{a[-2]}-{a[-1]}'
    d[key] = d.get(key, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True) # 该语句用于排序

with open('earpa001_count.txt', 'w+', encoding='utf-8') as fo:
    for i in ls:
        fo.write('{},{}\n'.format(i[0], i[1]))

