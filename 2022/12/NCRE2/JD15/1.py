#
# 编写代码替换横线
#

a = input("")  #请输入填充符号，例如：#
s = "PYTHON"
print("{:{a:}^30}".format(s, a=a))