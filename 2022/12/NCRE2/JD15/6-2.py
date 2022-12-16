#
# 请在此文件作答
#
import jieba
dict_words = {}
with open('data3.txt', 'r', encoding='GBK') as f:
    ls = jieba.lcut(f.read())
for word in ls:
    if len(word) >= 2 and word != '\n':
        dict_words[word] = dict_words.get(word, 0) + 1
li=list(dict_words.items())
li.sort(key=lambda x:x[1], reverse=True)

max_word = li[0][0]
fo = open('out.txt', 'w', encoding='utf-8')
import re
with open('data3.txt', 'r', encoding='GBK') as f:
    s = re.sub('，|。|\n', '$', f.read())
    li = s.split('$')
    for i in li:
        if max_word in i:
            fo.write(f'{i}\n')