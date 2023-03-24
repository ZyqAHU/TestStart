import urllib.parse
import requests
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from scipy.interpolate import make_interp_spline
import re
import json


keyword=['机器学习','深度学习','物联网','云计算','计算模型','大数据','数学建模','图像处理','计算机视觉','计算机体系结构','理论计算机科学','计算机科学','区块链','人工智能']
year_data_all = []
keyword_all =[]

#cookie = 'Ecp_ClientId=5210628102801308911;cnkiUserKey=b261114d-5456-f7a0-d218-29c90a247b35;Ecp_ClientIp=58.34.66.42;_pk_ref=%5B%22%22%2C%22%22%2C1627001927%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D;ASP.NET_SessionId=wx2bvmuixh3bq3r5meb5tnk5;SID_kns8=123123;CurrSortFieldType=desc;SID_kcms=124101;CurrSortField=%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27);Ecp_IpLoginFail=21072358.34.66.42, 10.210.0.12;_pk_id=fc0ebc8f-840b-44c6-b064-37d1205b7bcc.1624847325.3.1627002597.1627001927.;SID_kns_new=kns123110;'
def getInfo(targetUrl):
    #伪造浏览器请求头
    fake_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
        #'Cookie':cookie,  #cookie测试，不需要cookie也获取
        #'Referer':'https://kns.cnki.net/kcms/detail/knetsearch.aspx?sfield=kw&skey=%E5%8C%BA%E5%9D%97%E9%93%BE&code=&v=9tzIsR7LVgUKQ_Ucqcy13H0PVvC_8a71XDfdwE8ntLnmoNnjXXC3V0UrNnvhguYG'
        'Referer':'https://www.cnki.net/'       #Referer测试，需要Referer，否则获取值为空
    }

    try:
        response =  requests.get(targetUrl,headers =fake_headers)
        print("目标网站：" + targetUrl + ";" + "\n请求结果代码：" + str(response.status_code))
    except:
        getInfo(targetUrl)
    return response

def prase(response):
    '''
    """
    调式阶段，把网页内容存至本地进行解析。避免写代码调试时一直向目标服务器请求。
    解析完成后再将此段代码注释，添加：html = response.content.decode('utf-8')
    将请求与解析合并
    """
    # 以写格式打开文件
    UnParseResponse = open('UnParseResponse.html', 'w', encoding="utf-8")
    # 将初步请求结果写入文件
    UnParseResponse.write(response.content.decode('utf-8'))
    UnParseResponse.close()
    # 以读方式打开文件名为html_file1.html的文件
    UnParseResponse = open('UnParseResponse.html', 'r', encoding="utf-8")
    # 把文件的内容全部读取出来并赋值给html变量
    html = UnParseResponse.read()
    # 关闭文件对象
    UnParseResponse.close()
    '''
    html = response.content.decode('utf-8')     #当上述代码注释时，将这条添加上
    # 初始化BeautifulSoup
    soup = BeautifulSoup(html,'lxml')
    #print(soup)  打印请求到的数据
    div=soup.find('div',class_ = 'listcont')
    data = div.find('script').string
    #print(data)  #需要的字符串，这里还可以尝试将数据转化成json，但本人习惯使用字符串提取的方式
    name = re.findall("name:\"(.+?)\"", str(data)) #正则表达式：从字符串中提取出介于  name:“ 和  ” 之间的关键词名称
    year_data = re.findall("data:(.+?)}", str(data))  # 从字符串中提取出年份与数量 type:str
    #防止找不到字符串从而返回的列表为空，添加异常处理
    try:
        name = name[0]
        keyword_all.append(name)
        year_data = json.loads(year_data[0])  # 将字符串转换为列表 type:list shpae:[[]]
        year_data_all.append(year_data)
        #print(year_data_all)
        #print(keyword_all)
    except:
        print("发生异常，字符串提取错误：name="+str(name)+"year_data="+str(year_data))

def data_format(year_data,keyword_data):
    year=[]   #年份长度，每一个关键字爬取的年份是不一样的，这里将所有关键字的年份拼接，并排序，再删去重复值
    for i in range(len(year_data)):
        for j in range(len(year_data[i])):
            year.append(year_data[i][j][0])     #年份拼接
    year.sort()     #排序
    year=list(set(year))    #删除重复值
    #print(year)
    data_df = pd.DataFrame(index=year, columns=keyword_data)     #创建dataframe格式的表格
    #data_df.at[1980,'机器学习']=1;          #测试:给df的对应坐标赋值

    for i in range(len(year_data)):
        for j in range(len(year_data[i])):
            data_df.at[year_data[i][j][0],keyword_data[i]] = year_data[i][j][1];   #注意此处：year_data[i]对于的是keyword_data[i],是按照爬取时的顺序
    print(data_df)
    return data_df

def draw_visual(data):
    # 设置字体为楷体
    plt.rcParams['font.sans-serif'] = ['KaiTi']
    data=data.fillna(0)  #将NaN转为0
    #颜色表
    color_list=['silver','lightcoral','steelblue','orange','springgreen','lightseagreen','teal','deepskyblue','lightskyblue','grey','violet','darkseagreen','darkviolet','tomato']
    for i in range(0,data.shape[1]):
        x = data.index  # x轴
        y =  list(data[data.columns[i]])  #y轴
        x_new = np.linspace(x.min(), x.max(), 300)      #300表示我需要在x的最小值和最大值之间分割的点数
        y_smooth = make_interp_spline(x,y)(x_new)       #将原来的x坐标系向密度更大的坐标系拟合，达到平滑的效果
        #plt.plot(data.index,list(data[data.columns[i]]),c=color_list[i],label=str(data.columns[i]))
        plt.plot(x_new, y_smooth,c=color_list[i], label=str(data.columns[i]))       #画图
        plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))    #设置横坐标密度
    plt.title(u'各计算机领域学术研究关注度指数发展趋势',fontsize=20)  # 设置标题
    plt.xlabel('年份',fontsize=15)  # 设置x，y轴的标签
    plt.ylabel('关注度指数',fontsize=15)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    #url = "https://kns.cnki.net/kcms/detail/knetsearch.aspx?sfield=kw&skey="+ urllib.parse.quote(keyword[0])

    for i in range(len(keyword)):
        url = "https://kns.cnki.net/kcms/detail/frame/knetlist.aspx?name="+urllib.parse.quote(keyword[i])+"&infotype=9&codetype=j&catalogName=%E5%85%B3%E6%B3%A8%E5%BA%A6%E6%8C%87%E6%95%B0%E5%88%86%E6%9E%90&vl=9tzIsR7LVgUKQ_Ucqcy13H0PVvC_8a71XDfdwE8ntLnvQsAEFaVMjFwHdnwGLpbu"
        response = getInfo(url)
        prase(response)     #对每一个关键词爬取到的数据存储一起存储到两个列表year_data_all[]和keyword_all[]中，正常情况下，keyword_all[]与keyword[]应该是一致的
    #print(year_data_all)
    #print(keyword_all)
    data = data_format(year_data_all, keyword_all)     #处理数据,将数据格式化为dataframe的二维表格模式
    draw_visual(data)



