# 请在......处写多行代码
# 建议不修改其他代码

import jieba

f = "红楼梦.txt"
sf = "停用词.txt"

with open(f, 'r', encoding='utf-8') as f:
    p = f.read()
li = jieba.lcut(p)
tyc = []
with open(sf, 'r', encoding='utf-8') as f:
    for line in f.read().splitlines():
        tyc.append(line)
txtx = [i for i in li if i not in tyc]
d = {}
for word in txtx:
    if len(word) == 1:  # 跳过标点符号和字
        continue
    elif word == '凤姐儿' or word == '凤丫头':
        rword = '凤姐'
    elif word == '二爷' or word == '宝二爷':
        rword = '宝玉'
    elif word == '颦儿' or word == '林妹妹' or word == '黛玉道':
        rword = '黛玉'
    elif word == '宝丫头':
        rword = '宝钗'
    elif word == '老祖宗':
        rword = '贾母'
    elif word == '袭人道':
        rword = '袭人'
    elif word == '贾政道':
        rword = '贾政'
    elif word == '琏二爷':
        rword = '贾琏'
    else:
        rword = word
    d[rword] = d.get(rword, 0) + 1
items = list(d.items())
items.sort(key=lambda x:x[1], reverse=True)
# 此行语句可以对items列表进行递减排序
o = open('result.csv', 'w+', encoding='utf-8')
for i in items:
    if i[1] < 40:
        break
    o.write(f'{i[0]},{i[1]}\n')
  