# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改


fi = open('score.txt', 'r', encoding='utf-8')
fo = open('candidate0.txt', 'w', encoding='utf-8')

L = []
for i in fi:
    n = i.strip(' \n')
    l = n.split(' ')
    A = []
    for o, j in enumerate(l):
        if o == 1:
            A.append(j)
        else:
            A.append(int(j))
    c = 0
    for j in range(2, 11):
        c += A[j]
    A.append(c)
    L.append(A)

L.sort(key=lambda x:x[-1], reverse=True)
for i in range(10):
    O = []
    for p in range(len(L[i])-1):
        j = L[i][p]
        O.append(str(j))
    w = ','.join(O)
    fo.write(f'{w}\n')
fi.close()
fo.close()
