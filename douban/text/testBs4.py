# -*- codeing = utf-8 -*-
# @Time : 2022/4/3 20:42
# @Author : ahu_zyq
# @File : testBs4.py
# @softwawre : PyCharm

#将复杂的html

from bs4 import BeautifulSoup
file = open("./baidu.html","rb")
htlm = file.read().decode("utf-8")
bs = BeautifulSoup(htlm,"html.parser")
# # print(bs.title)
# print(bs.title.string)

#文档搜索
import re
#findall
#字符串过滤：会查找与字符串完全相匹配的内容
# t_list = bs.find_all("a")
# print(t_list)

#正则表达式搜索
# t_list2 = bs.find_all(re.compile("a"))
# print(t_list2)

#方法搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)
# for item in t_list:
#     print(item)
# # print(t_list)


#2.kwargs 指定参数进行搜索
# t_list = bs.find_all(class_ = True)
# for item in t_list:
#     print(item)

#3.text参数

# t_list = bs.find_all(text = "hao123")
# t_list = bs.find_all(text = ["hao123","地图","贴吧"])
# t_list = bs.find_all(text = re.compile("\d"))
# for item in t_list:
#     print(t_list)



#4.limit参数
# t_list = bs.find_all("a",limit=3)
# for item in t_list:
#     print(t_list)

#css选择器
# t_list = bs.select('title')#通过标签查找
# t_list = bs.select("a[class='bri']")#通过属性查找
# t_list = bs.select("head > title")#通过子标签查找
# t_list = bs.select(".mnav")#通过类名查找
# t_list = bs.select("#U1")#通过id查找
# for item in t_list:
#     print(t_list)