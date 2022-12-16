# 
# 以下代码仅供参考。
# 

import jieba
with open('clean.txt', 'r', encoding='utf-8') as f:
    s = f.read()

d = {}
ls = jieba.lcut(s)
for i in ls:
    if len(i) >= 3:
        d[i] = d.get(i, 0) + 1

lt = list(d.items())
lt.sort(key = lambda x:x[1],reverse = True)
s = ''
for i in range(10):
    s += f'{lt[i][0]}:{lt[i][1]},'
s = s.strip(',')
print(s)