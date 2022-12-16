#请在.....处填写多行表达式或语句
#可以修改其他代码

f = open("八十天环游地球.txt", 'r' ,encoding="utf-8")
fo = open("八十天环游地球-章节.txt", 'w', encoding="utf-8")
import re
for i in f:
    if re.match(r'第.*?章', i):
        fo.write(i)

f.close()
fo.close()
