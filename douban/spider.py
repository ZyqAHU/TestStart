# -*- codeing = utf-8 -*-
# @Time : 2022/4/3 19:15
# @Author : zhangyaqiang
# @File : spider.py
# @softwawre : PyCharm

from bs4 import BeautifulSoup     #网页解析，获取数据
import re       #正则表达式
import urllib.request,urllib.error      #制定URL
import xlwt     #进行excel操作
import sqlite3  #进行sqlite数据库操作

def main():
    #1.爬取网页
    #2.逐一解析数据
    #3.保存数据

    #爬取网页
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    # savepath = ".\\豆瓣电影Top250.xls"
    # #保存数据
    # saveData(datalist,savepath)
    dbpath = "movie.db"
    saveDataDB(datalist,dbpath)




#所有规则
findLink = re.compile(r'<a href="(.*?)">')                  #生成创建正则表达式对象(电影链接)
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)          #图片链接
findTitle = re.compile(r'<span class="title">(.*)</span>')  #片名
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>') #评分
findJudgeNumber = re.compile(r'<span>(\d*)人评价</span>')                              #评价数
findInq = re.compile(r'<span class="inq">(.*)</span>')                               #评价
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)                                    #详情


#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = askUrl(url)

        #逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            # print(item)#测试
            data = []   #保存一部电影的所有信息
            item = str(item)


            link = re.findall(findLink,item)[0]        #通过正则表达式h获取电影超链接
            data.append(link)

            imgSrc = re.findall(findImgSrc,item)[0]#通过正则表达式h获取电影超链接
            data.append(imgSrc)

            titles = re.findall(findTitle,item)
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","")#去掉无关符号
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')#外文名留空
            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudgeNumber,item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")#去掉句号
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?'," ",bd) #去掉br
            bd = re.sub('/'," ",bd) #替换掉/
            data.append(bd.strip()) #去掉前后空格

            datalist.append(data)   #将处理好的一部电影信息放入datalist


            # print(item)
            # print(srclink)
        #查找符合要求的字符串，形成列表
    # print(datalist)
    return datalist

def askUrl(url):
    head = {#模拟浏览器头部信息
        "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"
    }#告诉豆瓣我的信息
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


def saveData(datalist,savepath):
    print("save")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)  # 创建工作表

    col = ("电影详情链接","图片链接","影片中文名","影片外文名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i]) #列名

    book.save(savepath)

    for i in range(0,250):
        print("第%d条"%i)
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])

    book.save(savepath)

def saveDataDB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into movie250(
                info_link,pic_link,cname,ename,score,rated,instroduction,info)
                values(%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        instroduction text,
        info text
        )
    '''    #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()




if __name__ == '__main__':
#调用函数
    main()
    print("爬取完毕")
    # init_db("movietest.db")
    # print("建立数据库")

