# 请在______处使用一行或多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

import re

fi = open("data.txt", "r", encoding='utf-8')
fo = open("univ.txt", "w", encoding='utf-8')

ml = re.findall(r'alt=\"(.*?)\"', fi.read())
for i in ml:
    fo.write(f'{i}\n')

fi.close()
fo.close()