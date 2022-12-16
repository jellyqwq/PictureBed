# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

data = input()  # 姓名 年龄 性别
li = [] 
while data:
    if data == '':
        break
    name, age, gender = tuple(data.split(' '))
    li.append((name,int(age),gender,))
    data = input()
agec = 0
for i in li:
    agec += i[1]
c = 0
for i in li:
    if i[2] == '男':
        c += 1
print("平均年龄是{:.2f} 男性人数是{}".format(agec/len(li), c))
