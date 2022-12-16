# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

'''
输入文件 ： candidate0.txt
输出文件 ： candidate.txt
'''
f = open("candidate0.txt",'r', encoding='utf-8')
A = []
for i in f:
    A.append(i.strip('\n').strip().split(' '))

lines = []
for i in A:
    ok = True
    for j in range(2, 12):
        if int(i[j]) < 60:
            ok = False
    if ok:
        lines.append(i)
f.close()
f = open('candidate.txt','w', encoding='utf-8')
for line in lines:
    f.write(line[0]+line[1]+'\n')
f.close() 
