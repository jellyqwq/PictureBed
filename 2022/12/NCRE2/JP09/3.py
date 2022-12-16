#请在...上填写多行代码
#可以修改其他代码

fi = open("data.txt", 'r', encoding='utf-8')
for l in fi:
    l = l.split(',')
    s = 0.0
    n = len(l)
    for i in l:
        s += float(i.split(':')[1].strip())
    print("总和是：{}，平均值是：{:.2f}".format(s,s/n))
fi.close()