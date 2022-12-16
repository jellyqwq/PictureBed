# 
# 以下代码仅供参考。
# 

import jieba

d = {}
with open('政府工作报告2019.txt', 'r', encoding='utf-8') as f:
    ls = jieba.lcut(f.read())
for i in ls:
    if len(i) >= 2:
        d[i] = d.get(i, 0) + 1

lt = list(d.items())
lt.sort(key = lambda x:x[1],reverse = True)
op = []
for i in range(10):
    op.append(f'{lt[i][0]}:{lt[i][1]}')
s = ','.join(op)
print(f'2019:{s}')

d = {}
with open('政府工作报告2018.txt', 'r', encoding='utf-8') as f:
    ls = jieba.lcut(f.read())
for i in ls:
    if len(i) >= 2:
        d[i] = d.get(i, 0) + 1

lt = list(d.items())
lt.sort(key = lambda x:x[1],reverse = True)
op = []
for i in range(10):
    op.append(f'{lt[i][0]}:{lt[i][1]}')
s = ','.join(op)
print(f'2018:{s}')
