#
# 在____________上补充代码
#


while True:
    try:
        a = eval(input('请输入一个正整数: '))    
        if a > 0 and type(a) == int:
            print(a)
            break
        else:
            print("请输入正整数")
    except:
        print("请输入正整数")

