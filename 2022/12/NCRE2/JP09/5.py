#请在......处填写多行代码
#请在_______处填写一行代码

def is_prime(n):
    bol = True
    for i in range(2,n):
        if n % i == 0:
            bol = False
    return bol
            

ls = [23,45,78,87,11,67,89,13,243,56,67,311,431,111,141]
for i in ls.copy():
    if is_prime(i) == True:
        ls.remove(i)
print(len(ls))