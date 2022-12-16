#
# 在____________上补充代码
#


scale = 0.0001  # 成就值增量

def calv(base, day):
    val = base * pow((1+scale), day*8)
    return val

print('5年后的成就值是{}'.format(int(calv(1, 5*365))))
      
year = 1
while calv(1, year*365) < 100:
    year += 1
    
print('{}年后成就值是100'.format(year))