# 请在______处使用一行代码或表达式替换
#该模板仅是提示作用，你可以全部删除重新作答，输出一致即可正确得分。
#请删除横线， 不要在横线上作答。

import jieba
txt = input("请输入一段中文文本:")
ls=jieba.lcut(txt)
print("{:.1f}".format(len(txt)/len(ls)))
