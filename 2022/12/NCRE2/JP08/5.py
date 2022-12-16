fp = open("out.txt", 'w+')
ch = input("请输入字符串：\n")
while True: # < 粘贴过去少了个冒号
    if '@' in ch:
        fp.write(ch[:ch.index('@')])
        break
    else:
        fp.write(ch + " ")
    ch = input()
fp.close()