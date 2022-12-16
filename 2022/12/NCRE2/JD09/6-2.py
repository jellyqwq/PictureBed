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
op2019 = []
for i in range(10):
    op2019.append(lt[i][0])

d = {}
with open('政府工作报告2018.txt', 'r', encoding='utf-8') as f:
    ls = jieba.lcut(f.read())
for i in ls:
    if len(i) >= 2:
        d[i] = d.get(i, 0) + 1

lt = list(d.items())
lt.sort(key = lambda x:x[1],reverse = True)
op2018 = []
for i in range(10):
    op2018.append(lt[i][0])


a = []
for i in op2019.copy():
    if i in op2018:
        a.append(i)
        op2019.remove(i)
        op2018.remove(i)
print('共有词语:'+','.join(a))
print('2019特有:'+','.join(op2019))
print('2018特有:'+','.join(op2018))