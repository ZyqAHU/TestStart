import requests
from pyquery import PyQuery as pq
from fake_useragent import UserAgent
import time
import pandas as pd
import random
import pymysql
from sqlalchemy import create_engine

UA = UserAgent()
headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': 'lianjia_uuid=6383a9ce-19b9-47af-82fb-e8ec386eb872; UM_distinctid=1777521dc541e1-09601796872657-53e3566-13c680-1777521dc5547a; _smt_uid=601dfc61.4fcfbc4b; _ga=GA1.2.894053512.1612577894; _jzqc=1; _jzqckmp=1; _gid=GA1.2.1480435812.1614959594; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1614049202,1614959743; csrfSecret=lqKM3_19PiKkYOfJSv6ldr_c; activity_ke_com=undefined; ljisid=6383a9ce-19b9-47af-82fb-e8ec386eb872; select_nation=1; crosSdkDT2019DeviceId=-kkiavn-2dq4ie-j9ekagryvmo7rd3-qjvjm0hxo; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1615004691; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221777521e37421a-0e1d8d530671de-53e3566-1296000-1777521e375321%22%2C%22%24device_id%22%3A%221777521e37421a-0e1d8d530671de-53e3566-1296000-1777521e375321%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_utm_source%22%3A%22guanwang%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wybeijing%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; lianjia_ssid=7a179929-0f9a-40a4-9537-d1ddc5164864; _jzqa=1.3310829580005876700.1612577889.1615003848.1615013370.6; _jzqy=1.1612577889.1615013370.2.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6.jzqsr=baidu; select_city=440300; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiZjdiNTI1Yjk4YjI3MGNhNjRjMGMzOWZkNDc4NjE4MWJkZjVjNTZiMWYxYTM4ZTJkNzMxN2I0Njc1MDEyY2FiOWMzNTIzZTE1ZjEyZTE3NjlkNTRkMTA2MWExZmIzMWM5YzQ3ZmQxM2M3NTM5YTQ1YzM5OWU0N2IyMmFjM2ZhZmExOGU3ZTc1YWU0NDQ4NTdjY2RiMjEwNTQyMDQzM2JiM2UxZDQwZWQwNzZjMWQ4OTRlMGRkNzdmYjExZDQwZTExNTg5NTFkODIxNWQzMzdmZTA4YmYyOTFhNWQ2OWQ1OWM4ZmFlNjc0OTQzYjA3NDBjNjNlNDYyNTZiOWNhZmM4ZDZlMDdhNzdlMTY1NmM0ZmM4ZGI4ZGNlZjg2OTE2MmU4M2MwYThhNTljMGNkODYxYjliNGYwNGM0NzJhNGM3MmVmZDUwMTJmNmEwZWMwZjBhMzBjNWE2OWFjNzEzMzM4M1wiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJhYWEyMjhiNVwifSIsInIiOiJodHRwczovL20ubGlhbmppYS5jb20vY2h1enUvc3ovenVmYW5nL3BnJTdCJTdELyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9',
    'Host': 'sz.lianjia.com',
    'Referer': 'https://sz.lianjia.com/zufang/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
}
num_page = 2

class Lianjia_Crawer:

    def __init__(self, txt_path):
        super(Lianjia_Crawer, self).__init__()
        self.file = str(txt_path)
        self.df = pd.DataFrame(columns = ['title', 'district', 'area', 'orient', 'floor', 'price', 'city'])

    def run(self):
        '''启动脚本'''
        connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format("root", "123456", "localhost", "3366", "lagou")
        engine = create_engine(connect_info)
        for i in range(100):
            url = "https://sz.lianjia.com/zufang/pg{}/".format(str(i))
            self.parse_url(url)
            time.sleep(random.randint(2, 5))
            print('正在爬取的 url 为 {}'.format(url))
        print('爬取完毕！！！！！！！！！！！！！！')
        self.df.to_csv(self.file, encoding='utf-8')
        print('租房信息已保存至本地')
        self.df.to_sql(name='house', con=engine, if_exists='append', index=False)
        print('租房信息已保存数据库')

    def parse_url(self, url):
        headers['User-Agent'] = UA.chrome
        res = requests.get(url, headers=headers)
        #声明pq对象
        doc = pq(res.text)
        for i in doc('.content__list--item .content__list--item--main'):
            try:
                pq_i = pq(i)
                # 房屋标题
                title = pq_i('.content__list--item--title a').text()
                # 具体信息
                houseinfo = pq_i('.content__list--item--des').text()
                # 行政区
                address = str(houseinfo).split('/')[0]
                district = str(address).split('-')[0]
                # 房屋面积
                full_area = str(houseinfo).split('/')[1]
                area = str(full_area)[:-1]
                # 朝向
                orient = str(houseinfo).split('/')[2]
                # 楼层
                floor = str(houseinfo).split('/')[-1]
                # 价格
                price = pq_i('.content__list--item-price').text()
                #城市
                city = '深圳'
                data_dict = {'title': title, 'district': district, 'area': area, 'orient': orient, 'floor': floor, 'price': price, 'city': city}
                self.df = self.df.append(data_dict, ignore_index=True)
                print([title, district, area, orient, floor, price, city])
            except Exception as e:
                print(e)
                print("索引提取失败，请重试！！！！！！！！！！！！！")

if __name__ =="__main__":
    txt_path = "zufang_shenzhen.csv"
    Crawer = Lianjia_Crawer(txt_path)
    Crawer.run() # 启动爬虫脚本