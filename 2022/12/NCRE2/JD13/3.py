#
# 在____________上补充代码
#

def func(n):
    s=0.0
    if not n%2 == 0:
        for i in range(1, n + 1, 2):
            s += 1 / i
    else:
        for i in range(2, n + 1, 2):
            s += 1 / i
    return s


number = int(input())
print('{:.2f}'.format(func(number)))

