# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

#PY301-1

f = open("score.txt","r", encoding='utf-8')
D = [] #单个学生的数据
L = [] #所有学生原始成绩和总成绩
#读取学生单科成绩并计算总成绩
for line in f.readlines():
    D.append((line.strip().split(' ')))
for i in D:
    soc = i[2:].copy()
    n = 0
    for j in soc:
        n += int(j)
    i.append(n)
    L.append(i)
f.close()
L.sort(key=lambda x:x[-1],reverse=True) #按学生总成绩从大到小排序

# N = []
for i in L:
    i[-1] = str(i[-1])

f = open('candidate0.txt','w', encoding='utf-8')
for i in range(10): #前十个学生数据写入文件中
    s = ''
    for j in L[i]:
        s += j + ' '
    s.strip()
    s += '\n'
    f.write(s)
f.close()
    

    
