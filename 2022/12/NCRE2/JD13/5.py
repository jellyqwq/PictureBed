#
# 在……上补充一行或多行代码
#
import jieba
s = input("请输入一段中文文本，句子之间以逗号或句号分隔：")
slist = jieba.lcut(s)
m = 0
for i in slist:
    if i in "，。":
        continue
    else:
        print(i, end='/')
        m+=1

      
print("\n中文词语数是：{}\n".format(m))

jh = s.split('。')
for i in jh:
    x = i.split('，')
    for j in x:
        if j != '':
            print('{: ^20}'.format(j))
