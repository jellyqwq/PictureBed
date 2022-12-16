#在......上完善代码
#可以修改程序框架及变量名称
import jieba
with open("sgld.txt","r",encoding ="utf-8") as f:
    lssgld = f.readlines()
d = {}
for i in lssgld:
    for j in '，。；“”‘’ \n':
        i = i.replace(j,'')
    cls = jieba.lcut(i)
    for c in cls:
        d[c] = d.get(c,0) + 1
ls = list(d.items())                              #要理解这行代码
ls.sort(key=lambda x:x[1], reverse = True)        #要理解这行代码
for i in range(5):
    print(ls[i][0], end='、')