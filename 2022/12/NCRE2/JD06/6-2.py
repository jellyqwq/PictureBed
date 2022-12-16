# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

import jieba
fi = open('data.txt', 'r', encoding='utf-8')
fo = open('out2.txt','w', encoding='utf-8')

ls = jieba.lcut(fi.read())
d = {}
for i in ls:
    if len(i) >= 3:
        d[i] = d.get(i, 0) + 1

li = list(d.items())
li.sort(key=lambda x:x[1], reverse=True)
for i in li:
    fo.write(f'{i[0]}:{i[1]}\n')
fi.close()
fo.close()
