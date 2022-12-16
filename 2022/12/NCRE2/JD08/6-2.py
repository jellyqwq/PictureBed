# 请在______处使用一行或多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

# 不一定是大学和学院结尾的

fi = open("univ.txt", "r", encoding='utf-8')

daxue = 0
xueyuan = 0

for i in fi:
    i = i.strip('\n')
    if '大学生' in i:
        continue
    elif '大学' in i:
        daxue += 1
        print(i)
    elif '学院' in i:
        xueyuan += 1
        print(i)

fi.close()
print("包含大学的名称数量是{}".format(daxue))
print("包含学院的名称数量是{}".format(xueyuan))