#
# 请在此文件作答
#
f_data = open('data.txt', 'r', encoding="utf-8")
f_studs = open('studs.txt', 'w', encoding="utf-8")

for i in f_data:
    a = i.strip('\n').replace(':', ',').split(',')
    f_studs.write(f'{a[0]}:{a[2]}\n')

f_data.close()
f_studs.close()
