# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

f = open('sensor.txt', 'r', encoding='utf-8')
fo = open('earpa001.txt', 'w+', encoding='utf-8')
for line in f:
    a = line.split(',')
    if a[1].strip() == 'earpa001':
        fo.write('{},{},{},{}'.format(a[0],a[1],a[2],a[3]))
