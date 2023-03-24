# -*- codeing = utf-8 -*-
# @Time : 2022/4/4 15:51
# @Author : ahu_zyq
# @File : testRe.py
# @softwawre : PyCharm

#正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re
#创建模式对象
# pat = re.compile("AA")#此处的AA是正则表达式，用来验证其他的字符串（创建正则表达式）
# m = pat.search("CBAAAAAbaaAAB")#被校验的内容
# m = re.search("asd","Aasd")
# print(m)

# print(re.findall("a+","adsdafADaab"))#前面是正则表达式，后面是规则
#
# #sub(分隔，替换)
# print(re.sub("a","A","AaaabjabcAAB"))#找到a用A替换，在第三个字符串查找

#建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题（忽略转义内容）
a = r"\aabd\'"
print(a)
