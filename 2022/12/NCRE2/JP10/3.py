#在......上填写一段代码

def reverse_dict(dic):
    nd = {}
    for i in dic.items():
        nd[i[1]] = i[0]
    a = list(nd)
    a = sorted(a, reverse=True)
    res = {}
    for k in a:
        res[k] = nd[k]
        print(k, nd[k])
    return res
#请输入一个字典
# dic = eval(input(""))
dic = eval('{"alice":1001,"john":1003,"kate":1002}')
reverse_dict(dic)