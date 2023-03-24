import requests
import math
import time
import pandas as pd
import pymysql
from sqlalchemy import create_engine

def get_json(url, num):
    """
    从指定的url中通过requests请求携带请求头和请求体获取网页中的信息,
    :return:
    """
    url1 = 'https://www.lagou.com/jobs/list_python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie':'user_trace_token=20210218203227-35e936a1-f40f-410d-8400-b87f9fb4be0f; _ga=GA1.2.331665492.1613651550; LGUID=20210218203230-39948353-de3f-4545-aa01-43d147708c69; LG_HAS_LOGIN=1; hasDeliver=0; privacyPolicyPopup=false; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; RECOMMEND_TIP=true; index_location_city=%E5%85%A8%E5%9B%BD; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1613651550,1613652253,1613806244,1614497914; _putrc=52ABCFBE36E5D0BD123F89F2B170EADC; gate_login_token=ea312e017beac7fe72547a32956420b07d6d5b1816bc766035dd0f325ba92b91; JSESSIONID=ABAAAECAAEBABII8D8278DB16CB050FD656DD1816247B43; login=true; unick=%E7%94%A8%E6%88%B72933; WEBTJ-ID=20210228%E4%B8%8B%E5%8D%883:38:37153837-177e7932b7f618-05a12d1b3d5e8c-53e356a-1296000-177e7932b8071; sensorsdata2015session=%7B%7D; _gid=GA1.2.1359196614.1614497918; __lg_stoken__=bb184dd5d959320e9e61d943e802ac98a8538d44699751621e807e93fe0ffea4c1a57e923c71c93a13c90e5abda7a51873c2e488a4b9d76e67e0533fe9e14020734016c0dcf2; X_MIDDLE_TOKEN=90b85c3630b92280c3ad7a96c881482e; LGSID=20210228161834-659d6267-94a3-4a5c-9857-aaea0d5ae2ed; TG-TRACK-CODE=index_navigation; SEARCH_ID=092c1fd19be24d7cafb501684c482047; X_HTTP_TOKEN=fdb10b04b25b767756070541617f658231fd72d78b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2220600756%22%2C%22first_id%22%3A%22177b521c02a552-08c4a0f886d188-73e356b-1296000-177b521c02b467%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Linux%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2288.0.4324.190%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22%24device_id%22%3A%22177b521c02a552-08c4a0f886d188-73e356b-1296000-177b521c02b467%22%7D; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1614507066; LGRID=20210228181106-f2d71d85-74fe-4b43-b87e-d78a33c872ad'
    }
    data = {
        'first': 'true',
        'pn': num,
        'kd': 'BI工程师'}
    #得到Cookies信息
    s = requests.Session()
    print('建立session：', s, '\n\n')
    s.get(url=url1, headers=headers, timeout=3)
    cookie = s.cookies
    print('获取cookie：', cookie, '\n\n')
    #添加请求参数以及headers、Cookies等信息进行url请求
    res = requests.post(url, headers=headers, data=data, cookies=cookie, timeout=3)
    res.raise_for_status()
    res.encoding = 'utf-8'
    page_data = res.json()
    print('请求响应结果：', page_data, '\n\n')
    return page_data


def get_page_num(count):
    """
    计算要抓取的页数，通过在拉勾网输入关键字信息，可以发现最多显示30页信息,每页最多显示15个职位信息
    :return:
    """
    page_num = math.ceil(count / 15)
    if page_num > 29:
        return 29
    else:
        return page_num


def get_page_info(jobs_list):
    """
    获取职位
    :param jobs_list:
    :return:
    """
    page_info_list = []
    for i in jobs_list:  # 循环每一页所有职位信息
        job_info = []
        job_info.append(i['companyFullName'])
        job_info.append(i['companyShortName'])
        job_info.append(i['companySize'])
        job_info.append(i['financeStage'])
        job_info.append(i['district'])
        job_info.append(i['positionName'])
        job_info.append(i['workYear'])
        job_info.append(i['education'])
        job_info.append(i['salary'])
        job_info.append(i['positionAdvantage'])
        job_info.append(i['industryField'])
        job_info.append(i['firstType'])
        job_info.append(",".join(i['companyLabelList']))
        job_info.append(i['secondType'])
        job_info.append(i['city'])
        page_info_list.append(job_info)
    return page_info_list

def unique(old_list):
    newList = []
    for x in old_list:
        if x not in newList :
            newList.append(x)
    return newList

def main():
    connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format("root", "123456", "localhost", "3366",
                                                                        "lagou")
    engine = create_engine(connect_info)
    url = ' https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    first_page = get_json(url, 1)
    total_page_count = first_page['content']['positionResult']['totalCount']
    num = get_page_num(total_page_count)
    total_info = []
    time.sleep(10)
    for num in range(1, num + 1):
        # 获取每一页的职位相关的信息
        page_data = get_json(url, num)  # 获取响应json
        jobs_list = page_data['content']['positionResult']['result']  # 获取每页的所有python相关的职位信息
        page_info = get_page_info(jobs_list)
        total_info += page_info
        print('已经爬取到第{}页，职位总数为{}'.format(num, len(total_info)))
        time.sleep(20)
    #将总数据转化为data frame再输出,然后在写入到csv格式的文件中以及本地数据库中
    df = pd.DataFrame(data=unique(total_info),
                      columns=['companyFullName', 'companyShortName', 'companySize', 'financeStage',
                               'district', 'positionName', 'workYear', 'education',
                               'salary', 'positionAdvantage', 'industryField',
                               'firstType', 'companyLabelList', 'secondType', 'city'])
    df.to_csv('bi.csv', index=True)
    print('职位信息已保存本地')
    df.to_sql(name='demo', con=engine, if_exists='append', index=False)
    print('职位信息已保存数据库')

if __name__ == '__main__':
    main()