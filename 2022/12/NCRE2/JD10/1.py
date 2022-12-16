#
# 在____________上补充代码
#


n = input('请输入一个正整数:')                    #请输入一个正整数:
for i in range(int(n)):
    print('{:0>2} {}'.format(i + 1, '>'*(i+1)))
