#请在.....处填写多行表达式或语句
#不得修改其他代码

img = [0.69,0.292,0.33,0.131,0.61,0.254]
filter = [0.1, 0.8, 0.1]
res = []
for i in range(len(img)-2):
    k = 0
    for j in range(len(filter)):
        k += img[i+j] * filter[j]
        # k = img[i]*filter[0] + img[i+1]*filter[1]+ img[i+2]*filter[2]
        print('k={:.3f} ,filter[{}]={:.3f},img[{}+{}]={:.3f}'.format(
            k,
            j,
            filter[j],
            i,
            j,
            img[i+j]
        ))
    res.append(k)
for r in res:
    print('{:.3f}'.format(r), end=' ')