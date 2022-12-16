# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

import jieba
fi = open('data.txt', 'r', encoding='utf-8')
fo = open('out1.txt','w', encoding='utf-8')

ls = jieba.lcut(fi.read())
alrealy = []
for i in ls:
    if len(i) >= 3 and i not in alrealy:
        alrealy.append(i)
        fo.write(f'{i}\n')

fi.close()
fo.close()
