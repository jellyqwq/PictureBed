fi = open('candidate0.txt', 'r', encoding='utf-8')
fo = open('candidate.txt', 'w', encoding='utf-8')

L = []
for i in fi:
    n = i.strip(' \n')
    l = n.split(',')
    A = []
    for o, j in enumerate(l):
        if o == 1:
            A.append(j)
        else:
            A.append(int(j))
    # c = 0
    # for j in range(2, 11):
    #     c += A[j]
    # A.append(c)
    L.append(A)

for i in L:
    ok = True
    for j in range(2, 11):
       if i[j] < 60:
        ok = False 
        break
    if ok:
        fo.write(f'{i[0]} {i[1]}\n')

fi.close()
fo.close()