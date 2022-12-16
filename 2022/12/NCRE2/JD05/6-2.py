# 请在______处使用一行代码或表达式替换
#
# 可修改给出的任何代码

import jieba
f = open('out.txt','r', encoding='utf-8')    #以读的方式打开文件
words = f.readlines()
f.close()
D={}
for w in words:        #词频统计
    w = w.strip('\n ')
    D[w]=D.get(w, 0) + 1
print("曹操出现次数为:{}  ".format(D['曹操']))
