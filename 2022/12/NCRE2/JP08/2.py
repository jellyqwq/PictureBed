ls = eval(input())
for i in range(len(ls)):
    ls[i] = ls[i][0].upper() + ls[i][1:]
print(ls)