#
# 在……上补充一行或多行代码，不得修改其他代码
#

import random as r
r.seed(0)
persons = ['Alice', 'Bob','xiaoming', 'bingbing']
flag = 3
while flag>0:
    flag -= 1
    name = input('请输入一个名字：')
    if name == 'q':
        # print('程序自动退出')
        break
    if name in persons:
        num = r.randint(1000,9999)
        print('{} {}'.format(name, num))
    else:
        print('对不起，您输入的名字不存在。')
    