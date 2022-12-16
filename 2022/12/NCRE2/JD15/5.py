#
# 在……上补充一行或多行代码
#
import jieba
fo = open('data.txt', 'w', encoding='utf-8')

s = input("请输入一个中文字符串，包含逗号和句号：")
k=jieba.lcut(s)
dict1 = {}
for i in k:
    if len(i) >= 2:
        dict1[i] = dict1.get(i, 0) + 1
for i in dict1:
    fo.write(f'{i}：{dict1[i]}\n')

# 借助平台优势，宣传推广相应产品，并为技术从业者提供更多学习、交流、探讨的机会，从而促进技术交流、企业互通、 人才培养，促进技术的发展。