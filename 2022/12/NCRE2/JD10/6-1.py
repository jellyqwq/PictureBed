# 
# 以下代码仅供参考。
# 

import jieba
with open('data.txt', 'r', encoding='utf-8') as f:
    s = f.read()
fo = open('clean.txt', 'w', encoding='utf-8')
# for i in '，。！？“”‘’：、……；  ()\n【】《》——\{\}（）':
for i in ["，", "。", "“", "”", "，", "（", "）", "【", "】", "{", "}", "《", "》", "！", "：", "、", "？", "……", "；", "—", "\n"," "]:
    s = s.replace(i,'')
fo.write(s)
fo.close()