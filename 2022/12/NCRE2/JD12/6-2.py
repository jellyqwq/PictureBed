# import jieba
# import re

# def cot(li):
#     d = {}
#     for i in li:
#         d[i] = d.get(i, 0) + 1
#     l = list(d.items())
#     l.sort(key=lambda x:x[1], reverse=True)
#     return l

# d={}
# with open('八十天环游地球.txt', 'r', encoding='utf-8') as f:
#     title = ''
#     for line in f.read().splitlines():
#         mp = re.match(r'第.*?章', line)
#         if mp:
#             title = mp.group()
#             d[title] = []
#         else:
#             for word in jieba.lcut(line):
#                 if len(word) >= 2:
#                     d[title].append(word)
# for s in d:
#     title = s
#     name, num = cot(d[s])[0][0], cot(d[s])[0][1]
#     print(f'{title} {name} {num}')


import jieba
import re

strf = '八十天环游地球.txt'

with open(strf, encoding='utf-8') as f:
    lines = f.read()
    t = re.findall('(第.{1,3}章.*)', lines)


with open(strf, encoding='utf-8') as f:
    lines = f.read()
    s = re.sub('(第.{1,3}章.*)', '$', lines)
    x = s.split('$')
    x = x[1:]

# 计算词频并输出结果。
for i, j in zip(t, x):
    counts = {}
    txt = jieba.lcut(i+j)
    for word in txt:
        if len(word) >= 2:
            counts[word] = counts.get(word, 0) + 1
    li = list(counts.items())
    li.sort(key=lambda x: x[1], reverse=True)
    word_max, count_max = li[0]
    chapter = re.findall('(第.*章)', i)[0]
    print(chapter + ' ' + word_max + ' ' + str(count_max))