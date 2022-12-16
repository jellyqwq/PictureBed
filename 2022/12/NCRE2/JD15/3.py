#
# 请完善代码
#

f = open('data1.txt', 'r')
ls = []
for line in f:
      for c in line:
            if c not in ls and c != '\n':
                ls.append(c)
f.close()
print(len(ls))
