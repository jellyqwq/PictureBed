#
# 请在此文件作答
#
f_data = open('data.txt', 'r', encoding="utf-8")
# f_studs = open('studs.txt', 'w', encoding="utf-8")

d={}
for i in f_data:
    a = i.strip('\n').replace(':', ',').split(',')
    d[a[1]] = d.get(a[1], [0, 0])
    d[a[1]][0] += 1
    d[a[1]][1] += float(a[2])

for k in d:
    print('{}:{:.2f}'.format(k,d[k][1]/d[k][0]))

f_data.close()
# f_studs.close()
