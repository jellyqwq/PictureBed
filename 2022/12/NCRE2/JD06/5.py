# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准


data = input()  # 课程名 考分
li = [] 
while data:
    if data == '':
        break
    li.append(data.split(' '))
    data = input()

li.sort(key= lambda x:int(x[1]), reverse=True)
c = 0
for i in li:
    c += int(i[1])
print("最高分课程是{}{}, 最低分课程是{}{}, 平均分是{:.2f}".format(li[0][0], li[0][1], li[-1][0], li[-1][1], c/len(li)))
