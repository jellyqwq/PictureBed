a = input()  # 请输入填充符号
c = input()  # 请输入要显示的字符串
flag = 1
while flag:
    try:
        b = eval(input())  # 请输入字符串总长度
    except:
        flag = 1
        print("请输入一个正整数")
    else:
        if type(b)== int and b>0:
            flag = 0
        else:
            flag = 1
            print("请输入一个正整数")
print('{0:{1}^{2}}'.format(c,a,b))