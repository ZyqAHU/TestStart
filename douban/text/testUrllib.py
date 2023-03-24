# -*- codeing = utf-8 -*-
# @Time : 2022/4/3 19:41
# @Author : ahu_zyq
# @File : testUrllib.py
# @softwawre : PyCharm

import urllib.request

# respond = urllib.request.urlopen("http://www.baidu.com")
# print(respond.read().decode('utf-8'))

#获取一个post请求

import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# respond = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(respond.read().decode("utf-8"))

# try:
#     respond = urllib.request.urlopen("http://httpbin.org/get",timeout=0.1)
#     print(respond.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

# url = "http://www.douban.com"
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# headers= {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"}
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# respond = urllib.request.urlopen(req)
# print(respond.read.decode("utf-8"))


url = "http://www.douban.com"
headers= {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"}
req = urllib.request.Request(url=url,headers=headers)
respond = urllib.request.urlopen(req)
print(respond.read().decode("utf-8"))