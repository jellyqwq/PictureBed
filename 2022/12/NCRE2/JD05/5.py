#请完善如下代码
#在....处填写多行代码，不得修改其他代码
#PY202.py

import re
cint = re.compile(r'\d+')
while True:
    s = input("请输入不带数字的文本:")
    if len(re.findall(cint,s)) == 0:
        break
print(len(s))
