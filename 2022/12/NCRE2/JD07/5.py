# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

f = open("vote.txt", 'r', encoding="utf-8")
names = f.readlines()
f.close()
n = 0
for name in names:
    name = name.strip('\n')
    num = len(name.split(' '))
    if num == 1:
        n+=1
print("有效票{}张".format(n))
