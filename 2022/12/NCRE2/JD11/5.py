#
# 在......上补充一行或多行代码
# 在____________上补充一行代码
# 可以修改代码
#




f = open('data.txt', 'r',encoding="utf-8")
x=[]
d = {}
for line in f:
    line = line.strip(' \n')
    if line != '':
        a = line.split(',')
        # print(a)
        d[a[2]] = d.get(a[2], [])
        d[a[2]].append(a[1])
unis = []
for i in d.items():
    unis.append([i[0], len(i[1]), ','.join(i[1])])
for d in unis:
    print('{:>4}: {:>4} : {}'.format(d[0],d[1],d[2]))