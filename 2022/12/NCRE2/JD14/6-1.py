
#读取文件内容到列表ls中
with open('webpage.txt', 'r', encoding='utf-8') as f:
    ls = f.readlines()

fo = open('images.txt', 'w', encoding='utf-8')
#统计url个数
num= 0  #统计个数的初始值为0
###
import re
for i in ls:
    r = re.findall('src="(.*?\.JPG)"', i)
    if r != []:
        fo.write(f'{r[0]}\n')
fo.close()
###
# print(num)  #输出个数
