#请在.....处填写多行表达式或语句
#请在_____处填写一行表达式或代码
#不得修改其他代码

sumtime = 0
percls = []
ts = {}
with open('out.txt', 'r', encoding='utf-8') as f:
    for i in f.read().splitlines():
        s = i.split(',')
    # percls.append([s[0], eval(s[1]), eval(s[2])])
        sumtime += float(s[1])
        ts[s[0]] = float(s[2])
print('the total execute time is ', sumtime)

tns = list(ts.items())
tns.sort(key=lambda x: x[1], reverse=True)
for i in range(3):
    print('the top {} percentage time is {}, spent in "{}" operation'.format(i, tns[i][1],tns[i][0]))
