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

for n, i in enumerate(li):
    if n == 10:
        break
    print(f'{i[0]}:{i[1]}')