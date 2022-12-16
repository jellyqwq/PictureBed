#
# 请在此文件作答
#
f_data = open('data.txt', 'r', encoding="utf-8")
# f_studs = open('studs.txt', 'w', encoding="utf-8")

A = []
for i in f_data:
    a = i.strip('\n').replace(':', ',').split(',')
    A.append(a)

A.sort(key=lambda x:x[2], reverse=True)
print(f'{A[0][0]}:{A[0][2]}')

f_data.close()
# f_studs.close()
