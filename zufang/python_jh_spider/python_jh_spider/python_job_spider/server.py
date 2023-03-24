import jieba
import jieba.analyse
import numpy as np
from flask import Flask, request, jsonify
import pymysql
from flask_cors import *
import pandas as pd
from collections import Counter
import pickle

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, supports_credentials=True)

from flask.json import JSONEncoder as _JSONEncoder

class JSONEncoder(_JSONEncoder):
    def default(self, o):
        import decimal
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(JSONEncoder, self).default(o)
app.json_encoder = JSONEncoder

@app.route('/xueli',methods=['GET'])
def xueli():
    #打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    #创建一个游标对象cursor
    cursor = conn.cursor()
    #执行sql语句
    cursor.execute("SELECT DISTINCT(education) from demo")
    #获取所有记录列表
    result = cursor.fetchall()
    education = []
    education_data = []
    color_list = ['#459AF0', '#38C3B0', '#86CA5A', '#BFD44F', '	#90EE90']
    #获取到学历的五种情况：不限、大专、本科、硕士、博士
    for field in result:
        education.append(field[0])
    #获取到每种学历对应的个数
    for i in range(len(education)):
        cursor.execute("SELECT count(*) from demo where education = '" + education[i] + "'")
        count = cursor.fetchall()
        education_data.append({'value': count[0][0], 'itemStyle': {'color': color_list[i]}})
    cursor.execute("SELECT DISTINCT(workYear) from demo")
    result = cursor.fetchall()
    workYear = []
    workYear_data = []
    #获取到的几种工作经验
    for field in result:
        workYear.append(field[0])
    #获取到每种工作经验对应的个数
    for i in workYear:
        cursor.execute("SELECT count(*) from demo where workYear = '" + i + "'")
        count = cursor.fetchall()
        workYear_data.append({'value': count[0][0], 'name': i})
    cursor.close()
    return jsonify({"education":education, "education_data":education_data, "workYear_data":workYear_data})

@app.route('/xueli_first',methods=['GET'])
def xueli_first():
    #打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    #创建一个游标对象cursor
    cursor = conn.cursor()
    #执行sql语句
    cursor.execute("SELECT DISTINCT(education) from demo where city in ('北京', '上海', '广州', '深圳');")
    #获取所有记录列表
    result = cursor.fetchall()
    education = []
    education_data = []
    color_list = ['#459AF0', '#38C3B0', '#86CA5A', '#BFD44F', '	#90EE90']
    #获取到学历的五种情况：不限、大专、本科、硕士、博士
    for field in result:
        education.append(field[0])
    #获取到每种学历对应的个数
    for i in range(len(education)):
        cursor.execute("SELECT count(*) from demo where education = '" + education[i] + "' and city in ('北京', '上海', '广州', '深圳');")
        count = cursor.fetchall()
        education_data.append({'value': count[0][0], 'itemStyle': {'color': color_list[i]}})

    cursor.execute("SELECT DISTINCT(workYear) from demo where city in ('北京', '上海', '广州', '深圳');")
    result = cursor.fetchall()
    workYear = []
    workYear_data = []
    #获取到的几种工作经验
    for field in result:
        workYear.append(field[0])
    #获取到每种工作经验对应的个数
    for i in workYear:
        cursor.execute("SELECT count(*) from demo where workYear = '" + i + "' and city in ('北京', '上海', '广州', '深圳');")
        count = cursor.fetchall()
        workYear_data.append({'value': count[0][0], 'name': i})
    cursor.close()
    return jsonify({"education":education, "education_data":education_data, "workYear_data":workYear_data})

@app.route('/xueli_nfirst',methods=['GET'])
def xueli_nfirst():
    #打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    #创建一个游标对象cursor
    cursor = conn.cursor()
    #执行sql语句
    cursor.execute("SELECT DISTINCT(education) from demo where city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
    #获取所有记录列表
    result = cursor.fetchall()
    education = []
    education_data = []
    color_list = ['#459AF0', '#38C3B0', '#86CA5A', '#BFD44F', '	#90EE90']
    #获取到学历的五种情况：不限、大专、本科、硕士、博士
    for field in result:
        education.append(field[0])
    #获取到每种学历对应的个数
    for i in range(len(education)):
        cursor.execute("SELECT count(*) from demo where education = '" + education[i] + "' and city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
        count = cursor.fetchall()
        education_data.append({'value': count[0][0], 'itemStyle': {'color': color_list[i]}})

    cursor.execute("SELECT DISTINCT(workYear) from demo where city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
    result = cursor.fetchall()
    workYear = []
    workYear_data = []
    #获取到的几种工作经验
    for field in result:
        workYear.append(field[0])
    #获取到每种工作经验对应的个数
    for i in workYear:
        cursor.execute("SELECT count(*) from demo where workYear = '" + i + "' and city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
        count = cursor.fetchall()
        workYear_data.append({'value': count[0][0], 'name': i})
    cursor.close()
    return jsonify({"education":education, "education_data":education_data, "workYear_data":workYear_data})

@app.route('/xueli_second',methods=['GET'])
def xueli_second():
    #打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    #创建一个游标对象cursor
    cursor = conn.cursor()
    #执行sql语句
    cursor.execute("SELECT DISTINCT(education) from demo where city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
    #获取所有记录列表
    result = cursor.fetchall()
    education = []
    education_data = []
    color_list = ['#459AF0', '#38C3B0', '#86CA5A', '#BFD44F', '	#90EE90']
    #获取到学历的五种情况：不限、大专、本科、硕士、博士
    for field in result:
        education.append(field[0])
    #获取到每种学历对应的个数
    for i in range(len(education)):
        cursor.execute("SELECT count(*) from demo where education = '" + education[i] + "' and city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
        count = cursor.fetchall()
        education_data.append({'value': count[0][0], 'itemStyle': {'color': color_list[i]}})

    cursor.execute("SELECT DISTINCT(workYear) from demo where city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
    result = cursor.fetchall()
    workYear = []
    workYear_data = []
    #获取到的几种工作经验
    for field in result:
        workYear.append(field[0])
    #获取到每种工作经验对应的个数
    for i in workYear:
        cursor.execute("SELECT count(*) from demo where workYear = '" + i + "' and city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
        count = cursor.fetchall()
        workYear_data.append({'value': count[0][0], 'name': i})
    cursor.close()
    return jsonify({"education":education, "education_data":education_data, "workYear_data":workYear_data})

@app.route('/fuli',methods=['GET'])
def fuli():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select positionAdvantage from `demo`")
    data_dict = []
    result = cursor.fetchall()
    for field in result:
        data_dict.append(field['positionAdvantage'])
    content = ''.join(data_dict)
    positionAdvantage = []
    jieba.analyse.set_stop_words('./stopwords.txt')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for v, n in tags:
        mydict = {}
        mydict["name"] = v
        mydict["value"] = str(int(n * 10000))
        positionAdvantage.append(mydict)
    cursor.execute("select companyLabelList from `demo`")
    data_dict = []
    result = cursor.fetchall()
    for field in result:
        data_dict.append(field['companyLabelList'])
    content = ''.join(data_dict)
    companyLabelList = []
    jieba.analyse.set_stop_words('./stopwords.txt')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for v, n in tags:
        mydict = {}
        mydict["name"] = v
        mydict["value"] = str(int(n * 10000))
        companyLabelList.append(mydict)
    cursor.close()
    return jsonify({"zwfl": positionAdvantage, "gsfl": companyLabelList})

@app.route('/fuli_first',methods=['GET'])
def fuli_first():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select positionAdvantage from `demo` where city in ('北京', '上海', '广州', '深圳');")
    data_dict = []
    result = cursor.fetchall()
    for field in result:
        data_dict.append(field['positionAdvantage'])
    content = ''.join(data_dict)
    positionAdvantage = []
    jieba.analyse.set_stop_words('./stopwords.txt')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for v, n in tags:
        mydict = {}
        mydict["name"] = v
        mydict["value"] = str(int(n * 10000))
        positionAdvantage.append(mydict)

    cursor.execute("select companyLabelList from `demo` where city in ('北京', '上海', '广州', '深圳');")
    data_dict = []
    result = cursor.fetchall()
    for field in result:
        data_dict.append(field['companyLabelList'])
    content = ''.join(data_dict)
    companyLabelList = []
    jieba.analyse.set_stop_words('./stopwords.txt')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for v, n in tags:
        mydict = {}
        mydict["name"] = v
        mydict["value"] = str(int(n * 10000))
        companyLabelList.append(mydict)
    cursor.close()
    return jsonify({"zwfl": positionAdvantage, "gsfl": companyLabelList})

@app.route('/fuli_nfirst',methods=['GET'])
def fuli_nfirst():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select positionAdvantage from `demo` where city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
    data_dict = []
    result = cursor.fetchall()
    for field in result:
        data_dict.append(field['positionAdvantage'])
    content = ''.join(data_dict)
    positionAdvantage = []
    jieba.analyse.set_stop_words('./stopwords.txt')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for v, n in tags:
        mydict = {}
        mydict["name"] = v
        mydict["value"] = str(int(n * 10000))
        positionAdvantage.append(mydict)

    cursor.execute("select companyLabelList from `demo` where city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
    data_dict = []
    result = cursor.fetchall()
    for field in result:
        data_dict.append(field['companyLabelList'])
    content = ''.join(data_dict)
    companyLabelList = []
    jieba.analyse.set_stop_words('./stopwords.txt')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for v, n in tags:
        mydict = {}
        mydict["name"] = v
        mydict["value"] = str(int(n * 10000))
        companyLabelList.append(mydict)
    cursor.close()
    return jsonify({"zwfl": positionAdvantage, "gsfl": companyLabelList})

@app.route('/fuli_second',methods=['GET'])
def fuli_second():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select positionAdvantage from `demo` where city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
    data_dict = []
    result = cursor.fetchall()
    for field in result:
        data_dict.append(field['positionAdvantage'])
    content = ''.join(data_dict)
    positionAdvantage = []
    jieba.analyse.set_stop_words('./stopwords.txt')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for v, n in tags:
        mydict = {}
        mydict["name"] = v
        mydict["value"] = str(int(n * 10000))
        positionAdvantage.append(mydict)

    cursor.execute("select companyLabelList from `demo` where city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
    data_dict = []
    result = cursor.fetchall()
    for field in result:
        data_dict.append(field['companyLabelList'])
    content = ''.join(data_dict)
    companyLabelList = []
    jieba.analyse.set_stop_words('./stopwords.txt')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for v, n in tags:
        mydict = {}
        mydict["name"] = v
        mydict["value"] = str(int(n * 10000))
        companyLabelList.append(mydict)
    cursor.close()
    return jsonify({"zwfl": positionAdvantage, "gsfl": companyLabelList})

@app.route('/qiye',methods=['GET'])
def qiye():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(city) from demo")
    result = cursor.fetchall()
    city = []
    city_result = []
    companySize = []
    companySizeResult = []
    selected = {}
    # 获取到的城市
    for field in result:
        city.append(field[0])
    if (len(request.args) == 0):
        # 没有查询条件
        # 获取到城市对应的个数
        for i in city:
            cursor.execute("SELECT count(*) from demo where city = '" + i + "'")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            city_result.append(dict)
        # 初始化最开始显示几个城市
        for i in city[10:]:
            selected[i] = False
        # 获取到几种公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            # 每种公司规模对应的个数
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "'")
            count = cursor.fetchall()
            companySizeResult.append(count[0][0])
    else:
        positionName = str(request.args['positionName']).lower()
        # 查询条件：某种职业
        # 每个城市某种职业的个数
        for i in city:
            cursor.execute("SELECT count(*) from demo where city = '" + i + "' and positionName like '%"+positionName+"%'")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            city_result.append(dict)
        for i in city[10:]:
            selected[i] = False
        cursor.execute("SELECT DISTINCT(companySize) from demo")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and positionName like '%"+positionName+"%'")
            count = cursor.fetchall()
            companySizeResult.append(count[0][0])
    result = {"city": city, "city_result": city_result, "selected": selected, "companySize": companySize, "companySizeResult": companySizeResult}
    cursor.close()
    return jsonify(result)

@app.route('/qiye_first',methods=['GET'])
def qiye_first():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    #cursor.execute("SELECT DISTINCT(city) from demo")
    #result = cursor.fetchall()
    city = ['北京', '上海', '广州', '深圳']
    city_result = []
    companySize = []
    companySizeResult = []
    selected = {}
    # 获取到的城市
    #for field in result:
        #city.append(field[0])
    if (len(request.args) == 0):
        # 没有查询条件
        # 获取到城市对应的个数
        for i in city:
            cursor.execute("SELECT count(*) from demo where city = '" + i + "'")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            city_result.append(dict)
        # 初始化最开始显示几个城市
        for i in city[4:]:
            selected[i] = False
        # 获取到几种公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city in ('北京', '上海', '广州', '深圳');")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            # 每种公司规模对应的个数
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and city in ('北京', '上海', '广州', '深圳');")
            count = cursor.fetchall()
            companySizeResult.append(count[0][0])
    else:
        positionName = str(request.args['positionName']).lower()
        # 查询条件：某种职业
        # 每个城市某种职业的个数
        for i in city:
            cursor.execute("SELECT count(*) from demo where city = '" + i + "' and positionName like '%"+positionName+"%'")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            city_result.append(dict)
        for i in city[4:]:
            selected[i] = False
        cursor.execute("SELECT DISTINCT(companySize) from demo where city in ('北京', '上海', '广州', '深圳');")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and positionName like '%"+positionName+"%' and city in ('北京', '上海', '广州', '深圳');")
            count = cursor.fetchall()
            companySizeResult.append(count[0][0])

    result = {"city": city, "city_result": city_result, "selected": selected, "companySize": companySize, "companySizeResult": companySizeResult}
    cursor.close()
    return jsonify(result)

@app.route('/qiye_nfirst',methods=['GET'])
def qiye_nfirst():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    #cursor.execute("SELECT DISTINCT(city) from demo")
    #result = cursor.fetchall()
    city = ['成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山']
    city_result = []
    companySize = []
    companySizeResult = []
    selected = {}
    # 获取到的城市
    #for field in result:
        #city.append(field[0])
    if (len(request.args) == 0):
        # 没有查询条件
        # 获取到城市对应的个数
        for i in city:
            cursor.execute("SELECT count(*) from demo where city = '" + i + "'")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            city_result.append(dict)
        # 初始化最开始显示几个城市
        for i in city[15:]:
            selected[i] = False
        # 获取到几种公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            # 每种公司规模对应的个数
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
            count = cursor.fetchall()
            companySizeResult.append(count[0][0])
    else:
        positionName = str(request.args['positionName']).lower()
        # 查询条件：某种职业
        # 每个城市某种职业的个数
        for i in city:
            cursor.execute("SELECT count(*) from demo where city = '" + i + "' and positionName like '%"+positionName+"%'")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            city_result.append(dict)
        for i in city[15:]:
            selected[i] = False
        cursor.execute("SELECT DISTINCT(companySize) from demo where city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and positionName like '%"+positionName+"%' and city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
            count = cursor.fetchall()
            companySizeResult.append(count[0][0])

    result = {"city": city, "city_result": city_result, "selected": selected, "companySize": companySize, "companySizeResult": companySizeResult}
    cursor.close()
    return jsonify(result)

@app.route('/qiye_second',methods=['GET'])
def qiye_second():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    #cursor.execute("SELECT DISTINCT(city) from demo")
    #result = cursor.fetchall()
    city = ['宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊']
    city_result = []
    companySize = []
    companySizeResult = []
    selected = {}
    # 获取到的城市
    #for field in result:
        #city.append(field[0])
    if (len(request.args) == 0):
        # 没有查询条件
        # 获取到城市对应的个数
        for i in city:
            cursor.execute("SELECT count(*) from demo where city = '" + i + "'")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            city_result.append(dict)
        # 初始化最开始显示几个城市
        for i in city[30:]:
            selected[i] = False
        # 获取到几种公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            # 每种公司规模对应的个数
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
            count = cursor.fetchall()
            companySizeResult.append(count[0][0])
    else:
        positionName = str(request.args['positionName']).lower()
        # 查询条件：某种职业
        # 每个城市某种职业的个数
        for i in city:
            cursor.execute("SELECT count(*) from demo where city = '" + i + "' and positionName like '%"+positionName+"%'")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            city_result.append(dict)
        for i in city[30:]:
            selected[i] = False
        cursor.execute("SELECT DISTINCT(companySize) from demo where city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and positionName like '%"+positionName+"%' and city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
            count = cursor.fetchall()
            companySizeResult.append(count[0][0])

    result = {"city": city, "city_result": city_result, "selected": selected, "companySize": companySize, "companySizeResult": companySizeResult}
    cursor.close()
    return jsonify(result)

@app.route('/xinzi',methods=['GET'])
def xinzi():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    positionName = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
    #柱状图返回列表
    zzt_list = []
    zzt_list.append(['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
    if (len(request.args) == 0 or str(request.args['education'])=='不限'):
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%K%' and positionName like '%"+i+"%';")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%"+i+"%';")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%"+i+"%';")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%';")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%';")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    else:
        education = str(request.args['education'])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%K%' and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    result = {"zzt": zzt_list}
    cursor.close()
    return jsonify(result)

@app.route('/xinzi_first',methods=['GET'])
def xinzi_first():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    #citys = ['北京', '上海', '广州', '深圳']
    positionName = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
    #柱状图返回列表
    zzt_list = []
    zzt_list.append(['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
    if (len(request.args) == 0 or str(request.args['education'])=='不限'):
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%K%' and positionName like '%"+i+"%' and city in ('北京', '上海', '广州', '深圳');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%"+i+"%' and city in ('北京', '上海', '广州', '深圳');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%"+i+"%' and city in ('北京', '上海', '广州', '深圳');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and city in ('北京', '上海', '广州', '深圳');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and city in ('北京', '上海', '广州', '深圳');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    else:
        education = str(request.args['education'])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('北京', '上海', '广州', '深圳') and SUBSTR(salary,1,2) like '%K%' and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('北京', '上海', '广州', '深圳') and SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('北京', '上海', '广州', '深圳') and SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('北京', '上海', '广州', '深圳') and SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('北京', '上海', '广州', '深圳') and SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    result = {"zzt": zzt_list}
    cursor.close()
    return jsonify(result)

@app.route('/xinzi_nfirst',methods=['GET'])
def xinzi_nfirst():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    #citys = ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山')
    positionName = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
    #柱状图返回列表
    zzt_list = []
    zzt_list.append(['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
    if (len(request.args) == 0 or str(request.args['education'])=='不限'):
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%K%' and positionName like '%"+i+"%' and city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%"+i+"%' and city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%"+i+"%' and city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    else:
        education = str(request.args['education'])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山') and SUBSTR(salary,1,2) like '%K%' and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山') and SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山') and SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山') and SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山') and SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    result = {"zzt": zzt_list}
    cursor.close()
    return jsonify(result)

@app.route('/xinzi_second',methods=['GET'])
def xinzi_second():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    #citys = ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊')
    positionName = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
    #柱状图返回列表
    zzt_list = []
    zzt_list.append(['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
    if (len(request.args) == 0 or str(request.args['education'])=='不限'):
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%K%' and positionName like '%"+i+"%' and city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%"+i+"%' and city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%"+i+"%' and city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    else:
        education = str(request.args['education'])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊') and SUBSTR(salary,1,2) like '%K%' and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊') and SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊') and SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊') and SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute(
                "SELECT COUNT(*) FROM demo WHERE city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊') and SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and education = '"+education+"'")
            count = cursor.fetchall()
            temp_list += count[0]
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    result = {"zzt": zzt_list}
    cursor.close()
    return jsonify(result)

@app.route('/rongzi',methods=['GET'])
def rongzi():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(financeStage) from demo")
    result = cursor.fetchall()
    finance = []
    finance_data = []
    # 获取到融资的几种情况
    for field in result:
        finance.append(field[0])
    # 获取到每种融资对应的个数
    for i in range(len(finance)):
        cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "'")
        count = cursor.fetchall()
        finance_data.append({'value': count[0][0], 'name': finance[i]})
    cursor.close()
    return jsonify({"finance": finance, "finance_data": finance_data})

@app.route('/rongzi_first',methods=['GET'])
def rongzi_first():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(financeStage) from demo where city in ('北京', '上海', '广州', '深圳');")
    result = cursor.fetchall()
    finance = []
    finance_data = []
    # 获取到融资的几种情况
    for field in result:
        finance.append(field[0])
    # 获取到每种融资对应的个数
    for i in range(len(finance)):
        cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and city in ('北京', '上海', '广州', '深圳');")
        count = cursor.fetchall()
        finance_data.append({'value': count[0][0], 'name': finance[i]})
    cursor.close()
    return jsonify({"finance": finance, "finance_data": finance_data})

@app.route('/rongzi_nfirst',methods=['GET'])
def rongzi_nfirst():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(financeStage) from demo where city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
    result = cursor.fetchall()
    finance = []
    finance_data = []
    # 获取到融资的几种情况
    for field in result:
        finance.append(field[0])
    # 获取到每种融资对应的个数
    for i in range(len(finance)):
        cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
        count = cursor.fetchall()
        finance_data.append({'value': count[0][0], 'name': finance[i]})
    cursor.close()
    return jsonify({"finance": finance, "finance_data": finance_data})

@app.route('/rongzi_second',methods=['GET'])
def rongzi_second():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(financeStage) from demo where city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
    result = cursor.fetchall()
    finance = []
    finance_data = []
    # 获取到融资的几种情况
    for field in result:
        finance.append(field[0])
    # 获取到每种融资对应的个数
    for i in range(len(finance)):
        cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
        count = cursor.fetchall()
        finance_data.append({'value': count[0][0], 'name': finance[i]})
    cursor.close()
    return jsonify({"finance": finance, "finance_data": finance_data})

@app.route('/poststyle',methods=['GET'])
def poststyle():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(firstType) from demo")
    result = cursor.fetchall()
    firstType = []
    firstType_data = []
    # 获取到职位类型的几种情况
    for field in result:
        firstType.append(field[0])
    # 获取到每种职位类型对应的个数
    for i in range(len(firstType)):
        cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "'")
        count = cursor.fetchall()
        firstType_data.append({'value': count[0][0], 'name': firstType[i]})
    cursor.execute("SELECT DISTINCT(secondType) from demo")
    second = cursor.fetchall()
    secondType = []
    secondType_data = []
    # 获取到职位类型的几种情况
    for field in second:
        secondType.append(field[0])
    # 获取到每种职位类型对应的个数
    for i in range(len(secondType)):
        cursor.execute("SELECT count(*) from demo where secondType = '" + secondType[i] + "'")
        count = cursor.fetchall()
        secondType_data.append({'value': count[0][0], 'name': secondType[i]})
    cursor.close()
    return jsonify({"firstType": firstType, "firstType_data": firstType_data, "secondType": secondType, "secondType_data": secondType_data})

@app.route('/poststyle_first',methods=['GET'])
def poststyle_first():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(firstType) from demo where city in ('北京', '上海', '广州', '深圳');")
    result = cursor.fetchall()
    firstType = []
    firstType_data = []
    # 获取到职位类型的几种情况
    for field in result:
        firstType.append(field[0])
    # 获取到每种职位类型对应的个数
    for i in range(len(firstType)):
        cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and city in ('北京', '上海', '广州', '深圳');")
        count = cursor.fetchall()
        firstType_data.append({'value': count[0][0], 'name': firstType[i]})

    cursor.execute("SELECT DISTINCT(secondType) from demo where city in ('北京', '上海', '广州', '深圳');")
    second = cursor.fetchall()
    secondType = []
    secondType_data = []
    # 获取到职位类型的几种情况
    for field in second:
        secondType.append(field[0])
    # 获取到每种职位类型对应的个数
    for i in range(len(secondType)):
        cursor.execute("SELECT count(*) from demo where secondType = '" + secondType[i] + "' and city in ('北京', '上海', '广州', '深圳');")
        count = cursor.fetchall()
        secondType_data.append({'value': count[0][0], 'name': secondType[i]})
    cursor.close()
    return jsonify({"firstType": firstType, "firstType_data": firstType_data, "secondType": secondType, "secondType_data": secondType_data})

@app.route('/poststyle_nfirst',methods=['GET'])
def poststyle_nfirst():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(firstType) from demo where city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
    result = cursor.fetchall()
    firstType = []
    firstType_data = []
    # 获取到职位类型的几种情况
    for field in result:
        firstType.append(field[0])
    # 获取到每种职位类型对应的个数
    for i in range(len(firstType)):
        cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
        count = cursor.fetchall()
        firstType_data.append({'value': count[0][0], 'name': firstType[i]})

    cursor.execute("SELECT DISTINCT(secondType) from demo where city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
    second = cursor.fetchall()
    secondType = []
    secondType_data = []
    # 获取到职位类型的几种情况
    for field in second:
        secondType.append(field[0])
    # 获取到每种职位类型对应的个数
    for i in range(len(secondType)):
        cursor.execute("SELECT count(*) from demo where secondType = '" + secondType[i] + "' and city in ('成都', '重庆', '杭州', '武汉', '西安', '天津', '苏州', '南京', '郑州', '长沙', '东莞' ,'沈阳', '青岛', '合肥', '佛山');")
        count = cursor.fetchall()
        secondType_data.append({'value': count[0][0], 'name': secondType[i]})
    cursor.close()
    return jsonify({"firstType": firstType, "firstType_data": firstType_data, "secondType": secondType, "secondType_data": secondType_data})

@app.route('/poststyle_second',methods=['GET'])
def poststyle_second():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(firstType) from demo where city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
    result = cursor.fetchall()
    firstType = []
    firstType_data = []
    # 获取到职位类型的几种情况
    for field in result:
        firstType.append(field[0])
    # 获取到每种职位类型对应的个数
    for i in range(len(firstType)):
        cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
        count = cursor.fetchall()
        firstType_data.append({'value': count[0][0], 'name': firstType[i]})

    cursor.execute("SELECT DISTINCT(secondType) from demo where city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
    second = cursor.fetchall()
    secondType = []
    secondType_data = []
    # 获取到职位类型的几种情况
    for field in second:
        secondType.append(field[0])
    # 获取到每种职位类型对应的个数
    for i in range(len(secondType)):
        cursor.execute("SELECT count(*) from demo where secondType = '" + secondType[i] + "' and city in ('宁波', '昆明', '福州', '无锡', '济南', '厦门', '大连', '哈尔滨', '温州', '石家庄', '泉州' ,'南宁', '长春', '南昌', '贵阳', '金华', '常州', '惠州', '嘉兴', '南通', '徐州', '太原', '珠海', '中山', '保定', '兰州', '台州', '绍兴', '烟台', '廊坊');")
        count = cursor.fetchall()
        secondType_data.append({'value': count[0][0], 'name': secondType[i]})
    cursor.close()
    return jsonify({"firstType": firstType, "firstType_data": firstType_data, "secondType": secondType, "secondType_data": secondType_data})



@app.route('/data',methods=['GET'])
def data():
    limit = int(request.args['limit'])
    page = int(request.args['page'])
    page = (page-1)*limit
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',charset='utf8mb4')
    cursor = conn.cursor()
    if (len(request.args) == 2):
        cursor.execute("select count(*) from demo")
        count = cursor.fetchall()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select * from demo limit "+str(page)+","+str(limit))
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field)
    else:
        education = str(request.args['education'])
        positionName = str(request.args['positionName']).lower()
        if(education=='不限'):
            cursor.execute("select count(*) from demo where positionName like '%"+positionName+"%'")
            count = cursor.fetchall()
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute("select * from demo where positionName like '%"+positionName+"%' limit " + str(page) + "," + str(limit))
            data_dict = []
            result = cursor.fetchall()
            for field in result:
                data_dict.append(field)
        else:
            cursor.execute("select count(*) from demo where positionName like '%"+positionName+"%' and education = '"+education+"'")
            count = cursor.fetchall()
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute("select * from demo where positionName like '%"+positionName+"%' and education = '"+education+"' limit " + str(page) + "," + str(limit))
            data_dict = []
            result = cursor.fetchall()
            for field in result:
                data_dict.append(field)
    table_result = {"code": 0, "msg": None, "count": count[0], "data": data_dict}
    cursor.close()
    conn.close()
    return jsonify(table_result)

@app.route('/zufang_data',methods=['GET'])
def zufang_data():
    limit = int(request.args['limit'])
    page = int(request.args['page'])
    page = (page-1)*limit
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')

    cursor = conn.cursor()
    if (len(request.args) == 2):
        cursor.execute("select count(*) from house;")
        count = cursor.fetchall()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select * from house limit "+str(page)+","+str(limit))
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field)
    else:
        city = str(request.args['city'])
        cursor.execute("select count(*) from house where city = '"+city+"';")
        count = cursor.fetchall()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select * from house where city = '"+city+"' limit " + str(page) + "," + str(limit))
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field)
    table_result = {"code": 0, "msg": None, "count": count[0], "data": data_dict}
    cursor.close()
    conn.close()
    return jsonify(table_result)

@app.route('/map',methods=['GET'])
def map():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(city) from demo")
    result = cursor.fetchall()
    city = []
    city_result = []
    # 获取到的城市
    for field in result:
        city.append(field[0])
    # 获取到城市对应的个数
    for i in city:
        cursor.execute("SELECT count(*) from demo where city = '" + i + "'")
        count = cursor.fetchall()
        dict = {'value': count[0][0], 'name': i}
        city_result.append(dict)

    result = {"city": city, "city_result": city_result}
    cursor.close()
    return jsonify(result)
#注册用户
@app.route('/addUser',methods=['POST'])
def addUser():
    #服务器端获取json
    get_json = request.get_json()
    name = get_json['name']
    password = get_json['password']
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("select count(*) from `user` where `username` = '" + name + "'")
    count = cursor.fetchall()
    #该昵称已存在
    if (count[0][0]!= 0):
        table_result = {"code": 500, "msg": "该昵称已存在！"}
        cursor.close()
    else:
        add = conn.cursor()
        sql = "insert into `user`(username,password) values('"+name+"','"+password+"');"
        add.execute(sql)
        conn.commit()
        table_result = {"code": 200, "msg": "注册成功"}
        add.close()
    conn.close()
    return jsonify(table_result)
#用户登录
@app.route('/loginByPassword',methods=['POST'])
def loginByPassword():
    get_json = request.get_json()
    name = get_json['name']
    password = get_json['password']
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("select count(*) from `user` where `username` = '" + name +"' and password = '" + password+"';")
    count = cursor.fetchall()
    if(count[0][0] != 0):
        table_result = {"code": 200, "msg": name}
        cursor.close()
    else:
        name_cursor = conn.cursor()
        name_cursor.execute("select count(*) from `user` where `username` = '" + name +"';")
        name_count = name_cursor.fetchall()
        #print(name_count)
        if(name_count[0][0] != 0):
            table_result = {"code":500, "msg": "密码错误！"}
        else:
            table_result = {"code":500, "msg":"该用户不存在，请先注册！"}
        name_cursor.close()
    conn.close()
    print(name)
    return jsonify(table_result)
#密码修改
@app.route('/updatePass',methods=['POST'])
def updatePass():
    get_json = request.get_json()
    name = get_json['name']
    oldPsw = get_json['oldPsw']
    newPsw = get_json['newPsw']
    rePsw = get_json['rePsw']
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("select count(*) from `user` where `username` = '" + name + "' and password = '" + oldPsw+"';")
    count = cursor.fetchall()
    print(count[0][0])
    #确定昵称密码对应
    if (count[0][0] == 0):
        table_result = {"code": 500, "msg": "原始密码错误！"}
        cursor.close()
    else:
        updatepass = conn.cursor()
        sql = "update `user` set password = '"+newPsw+"' where username = '"+ name +"';"
        updatepass.execute(sql)
        conn.commit()
        table_result = {"code": 200, "msg": "密码修改成功！", "username": name, "new_password": newPsw}
        updatepass.close()
    conn.close()
    return jsonify(table_result)
#个人信息修改
@app.route('/updateUserInfo',methods=['POST'])
def updateUserInfo():
    get_json = request.get_json()
    name = get_json['name']
    print(name)
    email = get_json['email']
    content = get_json['content']
    address = get_json['address']
    phone = get_json['phone']
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("update `user` set email = '"+email+"',content = '"+content+"',address = '"+address+"',phone = '"+phone+"' where username = '"+ name +"';")
    conn.commit()
    table_result = {"code": 200, "msg": "更新成功！","youxiang": email, "tel": phone}
    cursor.close()
    conn.close()
    print(table_result)
    return jsonify(table_result)
#密保手机修改
@app.route('/updateUserPhone',methods=['POST'])
def updateUserPhone():
    get_json = request.get_json()
    name = get_json['name']
    tel = get_json['tel']
    youxiang = get_json['youxiang']
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("update `user` set email = '"+youxiang+"',phone = '"+tel+"' where username = '"+ name +"';")
    conn.commit()
    table_result = {"code": 200, "msg": "修改成功！","youxiang": youxiang, "tel": tel}
    cursor.close()
    conn.close()
    print(table_result)
    return jsonify(table_result)
#密保邮箱修改
@app.route('/updateUserEmail',methods=['POST'])
def updateUserEmail():
    get_json = request.get_json()
    name = get_json['name']
    print(name)
    email = get_json['email']
    content = get_json['content']
    address = get_json['address']
    phone = get_json['phone']
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("update `user` set email = '"+email+"',content = '"+content+"',address = '"+address+"',phone = '"+phone+"' where username = '"+ name +"';")
    conn.commit()
    table_result = {"code": 200, "msg": "更新成功！","youxiang": email, "tel": phone}
    cursor.close()
    conn.close()
    print(table_result)
    return jsonify(table_result)
#个人信息查询
@app.route('/selectUserInfo',methods=['GET'])
def selectUserInfo():
    name = str(request.args['name'])
    print(name)
    email = []
    content = []
    address = []
    phone = []
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    #邮箱
    cursor.execute("select email from user where username = '"+ name +"';")
    result = cursor.fetchall()
    for field in result:
        email.append(field[0])
    #个人简介
    cursor.execute("select content from user where username = '" + name + "';")
    result = cursor.fetchall()
    for field in result:
        content.append(field[0])
    #地址
    cursor.execute("select address from user where username = '" + name + "';")
    result = cursor.fetchall()
    for field in result:
        address.append(field[0])
    #联系方式
    cursor.execute("select phone from user where username = '" + name + "';")
    result = cursor.fetchall()
    for field in result:
        phone.append(field[0])
    table_result = {"code": 200, "msg": "查询成功！","name": name, "email": email, "content": content, "address": address, "phone": phone, "tel": phone, "youxiang": email}
    cursor.close()
    conn.close()
    print(table_result)
    return jsonify(table_result)
@app.route('/predict',methods=['GET'])
def predict():
    y_data = ['0—10K', '10—20K', '20—30K', '30—40K', '40K以上']
    positionName = str(request.args['positionName']).lower()
    model = str(request.args['model'])
    with open(positionName+'_'+model+'.model', 'rb') as fr:
        selected_model = pickle.load(fr)
    companySize = int(request.args['companySize'])
    workYear = int(request.args['workYear'])
    education = int(request.args['education'])
    city = int(request.args['city'])
    x = [companySize, workYear, education, city]
    x = np.array(x)
    y = selected_model.predict(x.reshape(1, -1))
    return jsonify(y_data[y[0]])

@app.route('/beijing',methods=['GET'])
def beijing():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()

    district = []
    district_result = []
    companySize = []
    companySizeResult = []
    education = []
    educationResult = []
    workYear = []
    workYear_data = []
    firstType = []
    firstType_data = []
    finance = []
    finance_data = []
    leida_max_dict = []

    # 获取到的行政区
    cursor.execute("SELECT DISTINCT(district) from demo where city='北京';")
    result = cursor.fetchall()
    for field in result:
        district.append(field[0])
    if (len(request.args) == 0):
        # 没有查询条件
        # 获取到行政区对应的个数
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)

        # 获取到几种公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '北京';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            # 每种公司规模对应的个数
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and city = '北京';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)

        # 获取到几种学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '北京';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            # 每种学历要求对应的个数
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and city = '北京';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)


        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '北京';")
        workyear = cursor.fetchall()
        # 获取到的几种工作经验
        for field in workyear:
            workYear.append(field[0])
        # 获取到每种工作经验对应的个数
        for i in workYear:
            cursor.execute("SELECT count(*) from demo where workYear = '" + i + "' and city = '北京';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': i})

        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '北京';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 300})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and city = '北京';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])

        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '北京';")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)

        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '北京';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            for i in field.keys():
                firstType.append(field[i])

        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and city = '北京';")
            count = cursor.fetchall()
            for field in count:
                for j in field.keys():
                    value = field[j]

            firstType_data.append({'value': value, 'name': firstType[i]})

        #薪资待遇
        positionName = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(
            ['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + i + "%' and city = '北京';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(
            ['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + i + "%' and city = '北京';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + i + "%' and city = '北京';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and city = '北京';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and city = '北京';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])


    else:
        positionName = str(request.args['positionName']).lower()
        print(positionName)
        # 查询条件：某种职业
        # 行政区
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "' and positionName like '%"+positionName+"%';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)
        # 公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '北京';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and positionName like '%"+positionName+"%' and city = '北京';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)
        # 学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '北京';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '北京';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)
        #工作经验
        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '北京';")
        workyear = cursor.fetchall()
        for field in workyear:
            workYear.append(field[0])
            cursor.execute("SELECT count(*) from demo where workYear = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '北京';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': field[0]})
        # 融资阶段
        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '北京';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 300})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and positionName like '%" + positionName + "%' and city = '北京';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])
        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '北京';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            firstType.append(field[0])
        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and positionName like '%" + positionName + "%' and city = '北京';")
            count = cursor.fetchall()
            firstType_data.append({'value': count[0][0], 'name': firstType[i]})
        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '北京' and positionName like '%" + positionName + "%' ;")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)
        # 薪资待遇
        positionName_sample = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(['product', 'Java', 'Python', 'PHP', 'Web', 'BI', 'Android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        # <10k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + positionName + "%' and city = '北京';")
        count = cursor.fetchall()
        #print(count)
        for i in count[0].keys():
            value = count[0][i]
        print(value)
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # print(temp_list)
        # temp_list.append(value)
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 10-20k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + positionName + "%' and city = '北京';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 20-30k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + positionName + "%' and city = '北京';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 30-40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + positionName + "%' and city = '北京';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # >40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + positionName + "%' and city = '北京';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['>40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    print(zzt_list)
    result = {"district": district, "district_result": district_result, "companySize": companySize, "companySizeResult": companySizeResult, "education": education, "educationResult": educationResult, "workYear_data":workYear_data, "firstType": firstType, "firstType_data": firstType_data, "leida_max_dict":leida_max_dict, "cyt": positionAdvantage, "finance": finance, "finance_data": finance_data, "zzt": zzt_list}
    cursor.close()
    return jsonify(result)

@app.route('/shanghai',methods=['GET'])
def shanghai():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()

    district = []
    district_result = []
    companySize = []
    companySizeResult = []
    education = []
    educationResult = []
    workYear = []
    workYear_data = []
    firstType = []
    firstType_data = []
    finance = []
    finance_data = []
    leida_max_dict = []

    # 获取到的行政区
    cursor.execute("SELECT DISTINCT(district) from demo where city='上海';")
    result = cursor.fetchall()
    for field in result:
        district.append(field[0])
    if (len(request.args) == 0):
        # 没有查询条件
        # 获取到行政区对应的个数
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)

        # 获取到几种公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '上海';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            # 每种公司规模对应的个数
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and city = '上海';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)

        # 获取到几种学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '上海';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            # 每种学历要求对应的个数
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and city = '上海';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)


        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '上海';")
        workyear = cursor.fetchall()
        # 获取到的几种工作经验
        for field in workyear:
            workYear.append(field[0])
        # 获取到每种工作经验对应的个数
        for i in workYear:
            cursor.execute("SELECT count(*) from demo where workYear = '" + i + "' and city = '上海';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': i})

        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '上海';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 250})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and city = '上海';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])

        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '上海';")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)

        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '上海';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            for i in field.keys():
                firstType.append(field[i])

        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and city = '上海';")
            count = cursor.fetchall()
            for field in count:
                for j in field.keys():
                    value = field[j]

            firstType_data.append({'value': value, 'name': firstType[i]})

        #薪资待遇
        positionName = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(
            ['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + i + "%' and city = '上海';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(
            ['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + i + "%' and city = '上海';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + i + "%' and city = '上海';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and city = '上海';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and city = '上海';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])


    else:
        positionName = str(request.args['positionName']).lower()
        print(positionName)
        # 查询条件：某种职业
        # 行政区
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "' and positionName like '%"+positionName+"%';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)
        # 公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '上海';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and positionName like '%"+positionName+"%' and city = '上海';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)
        # 学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '上海';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '上海';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)
        #工作经验
        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '上海';")
        workyear = cursor.fetchall()
        for field in workyear:
            workYear.append(field[0])
            cursor.execute("SELECT count(*) from demo where workYear = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '上海';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': field[0]})
        # 融资阶段
        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '上海';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 250})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and positionName like '%" + positionName + "%' and city = '上海';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])
        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '上海';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            firstType.append(field[0])
        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and positionName like '%" + positionName + "%' and city = '上海';")
            count = cursor.fetchall()
            firstType_data.append({'value': count[0][0], 'name': firstType[i]})
        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '上海' and positionName like '%" + positionName + "%' ;")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)
        # 薪资待遇
        positionName_sample = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        # <10k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + positionName + "%' and city = '上海';")
        count = cursor.fetchall()
        #print(count)
        for i in count[0].keys():
            value = count[0][i]
        #print(value)
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # print(temp_list)
        # temp_list.append(value)
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 10-20k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + positionName + "%' and city = '上海';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 20-30k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + positionName + "%' and city = '上海';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 30-40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + positionName + "%' and city = '上海';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # >40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + positionName + "%' and city = '上海';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['>40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    print(zzt_list)
    result = {"district": district, "district_result": district_result, "companySize": companySize, "companySizeResult": companySizeResult, "education": education, "educationResult": educationResult, "workYear_data":workYear_data, "firstType": firstType, "firstType_data": firstType_data, "leida_max_dict":leida_max_dict, "cyt": positionAdvantage, "finance": finance, "finance_data": finance_data, "zzt": zzt_list}
    cursor.close()
    return jsonify(result)

@app.route('/guangzhou',methods=['GET'])
def guangzhou():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()

    district = []
    district_result = []
    companySize = []
    companySizeResult = []
    education = []
    educationResult = []
    workYear = []
    workYear_data = []
    firstType = []
    firstType_data = []
    finance = []
    finance_data = []
    leida_max_dict = []

    # 获取到的行政区
    cursor.execute("SELECT DISTINCT(district) from demo where city='广州';")
    result = cursor.fetchall()
    for field in result:
        district.append(field[0])
    if (len(request.args) == 0):
        # 没有查询条件
        # 获取到行政区对应的个数
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)

        # 获取到几种公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '广州';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            # 每种公司规模对应的个数
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and city = '广州';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)

        # 获取到几种学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '广州';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            # 每种学历要求对应的个数
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and city = '广州';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)


        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '广州';")
        workyear = cursor.fetchall()
        # 获取到的几种工作经验
        for field in workyear:
            workYear.append(field[0])
        # 获取到每种工作经验对应的个数
        for i in workYear:
            cursor.execute("SELECT count(*) from demo where workYear = '" + i + "' and city = '广州';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': i})

        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '广州';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 150})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and city = '广州';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])

        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '广州';")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)

        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '广州';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            for i in field.keys():
                firstType.append(field[i])

        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and city = '广州';")
            count = cursor.fetchall()
            for field in count:
                for j in field.keys():
                    value = field[j]

            firstType_data.append({'value': value, 'name': firstType[i]})

        #薪资待遇
        positionName = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(
            ['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + i + "%' and city = '广州';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(
            ['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + i + "%' and city = '广州';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + i + "%' and city = '广州';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and city = '广州';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and city = '广州';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])


    else:
        positionName = str(request.args['positionName']).lower()
        # 查询条件：某种职业
        # 行政区
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "' and positionName like '%"+positionName+"%';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)
        # 公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '广州';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and positionName like '%"+positionName+"%' and city = '广州';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)
        # 学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '广州';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '广州';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)
        #工作经验
        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '广州';")
        workyear = cursor.fetchall()
        for field in workyear:
            workYear.append(field[0])
            cursor.execute("SELECT count(*) from demo where workYear = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '广州';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': field[0]})
        # 融资阶段
        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '广州';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 150})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and positionName like '%" + positionName + "%' and city = '广州';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])
        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '广州';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            firstType.append(field[0])
        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and positionName like '%" + positionName + "%' and city = '广州';")
            count = cursor.fetchall()
            firstType_data.append({'value': count[0][0], 'name': firstType[i]})
        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '广州' and positionName like '%" + positionName + "%' ;")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)
        # 薪资待遇
        positionName_sample = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        # <10k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + positionName + "%' and city = '广州';")
        count = cursor.fetchall()
        #print(count)
        for i in count[0].keys():
            value = count[0][i]
        #print(value)
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # print(temp_list)
        # temp_list.append(value)
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 10-20k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + positionName + "%' and city = '广州';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 20-30k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + positionName + "%' and city = '广州';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 30-40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + positionName + "%' and city = '广州';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # >40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + positionName + "%' and city = '广州';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['>40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    print(zzt_list)
    result = {"district": district, "district_result": district_result, "companySize": companySize, "companySizeResult": companySizeResult, "education": education, "educationResult": educationResult, "workYear_data":workYear_data, "firstType": firstType, "firstType_data": firstType_data, "leida_max_dict":leida_max_dict, "cyt": positionAdvantage, "finance": finance, "finance_data": finance_data, "zzt": zzt_list}
    cursor.close()
    return jsonify(result)

@app.route('/hangzhou',methods=['GET'])
def hangzhou():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()

    district = []
    district_result = []
    companySize = []
    companySizeResult = []
    education = []
    educationResult = []
    workYear = []
    workYear_data = []
    firstType = []
    firstType_data = []
    finance = []
    finance_data = []
    leida_max_dict = []

    # 获取到的行政区
    cursor.execute("SELECT DISTINCT(district) from demo where city='杭州';")
    result = cursor.fetchall()
    for field in result:
        district.append(field[0])
    if (len(request.args) == 0):
        # 没有查询条件
        # 获取到行政区对应的个数
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)

        # 获取到几种公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '杭州';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            # 每种公司规模对应的个数
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and city = '杭州';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)

        # 获取到几种学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '杭州';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            # 每种学历要求对应的个数
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and city = '杭州';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)


        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '杭州';")
        workyear = cursor.fetchall()
        # 获取到的几种工作经验
        for field in workyear:
            workYear.append(field[0])
        # 获取到每种工作经验对应的个数
        for i in workYear:
            cursor.execute("SELECT count(*) from demo where workYear = '" + i + "' and city = '杭州';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': i})

        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '杭州';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 100})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and city = '杭州';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])

        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '杭州';")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)

        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '杭州';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            for i in field.keys():
                firstType.append(field[i])

        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and city = '杭州';")
            count = cursor.fetchall()
            for field in count:
                for j in field.keys():
                    value = field[j]

            firstType_data.append({'value': value, 'name': firstType[i]})

        #薪资待遇
        positionName = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(
            ['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + i + "%' and city = '杭州';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(
            ['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + i + "%' and city = '杭州';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + i + "%' and city = '杭州';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and city = '杭州';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and city = '杭州';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])


    else:
        positionName = str(request.args['positionName']).lower()
        # 查询条件：某种职业
        # 行政区
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "' and positionName like '%"+positionName+"%';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)
        # 公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '杭州';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and positionName like '%"+positionName+"%' and city = '杭州';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)
        # 学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '杭州';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '杭州';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)
        #工作经验
        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '杭州';")
        workyear = cursor.fetchall()
        for field in workyear:
            workYear.append(field[0])
            cursor.execute("SELECT count(*) from demo where workYear = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '杭州';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': field[0]})
        # 融资阶段
        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '杭州';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 100})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and positionName like '%" + positionName + "%' and city = '杭州';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])
        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '杭州';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            firstType.append(field[0])
        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and positionName like '%" + positionName + "%' and city = '杭州';")
            count = cursor.fetchall()
            firstType_data.append({'value': count[0][0], 'name': firstType[i]})
        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '杭州' and positionName like '%" + positionName + "%' ;")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)
        # 薪资待遇
        positionName_sample = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        # <10k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + positionName + "%' and city = '杭州';")
        count = cursor.fetchall()
        #print(count)
        for i in count[0].keys():
            value = count[0][i]
        #print(value)
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # print(temp_list)
        # temp_list.append(value)
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 10-20k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + positionName + "%' and city = '杭州';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 20-30k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + positionName + "%' and city = '杭州';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 30-40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + positionName + "%' and city = '杭州';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # >40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + positionName + "%' and city = '杭州';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['>40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    print(zzt_list)
    result = {"district": district, "district_result": district_result, "companySize": companySize, "companySizeResult": companySizeResult, "education": education, "educationResult": educationResult, "workYear_data":workYear_data, "firstType": firstType, "firstType_data": firstType_data, "leida_max_dict":leida_max_dict, "cyt": positionAdvantage, "finance": finance, "finance_data": finance_data, "zzt": zzt_list}
    cursor.close()
    return jsonify(result)

@app.route('/shenzhen',methods=['GET'])
def shenzhen():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()

    district = []
    district_result = []
    companySize = []
    companySizeResult = []
    education = []
    educationResult = []
    workYear = []
    workYear_data = []
    firstType = []
    firstType_data = []
    finance = []
    finance_data = []
    leida_max_dict = []

    # 获取到的行政区
    cursor.execute("SELECT DISTINCT(district) from demo where city='深圳';")
    result = cursor.fetchall()
    for field in result:
        district.append(field[0])
    if (len(request.args) == 0):
        # 没有查询条件
        # 获取到行政区对应的个数
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)

        # 获取到几种公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '深圳';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            # 每种公司规模对应的个数
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and city = '深圳';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)

        # 获取到几种学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '深圳';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            # 每种学历要求对应的个数
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and city = '深圳';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)


        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '深圳';")
        workyear = cursor.fetchall()
        # 获取到的几种工作经验
        for field in workyear:
            workYear.append(field[0])
        # 获取到每种工作经验对应的个数
        for i in workYear:
            cursor.execute("SELECT count(*) from demo where workYear = '" + i + "' and city = '深圳';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': i})

        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '深圳';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 300})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and city = '深圳';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])

        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '深圳';")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)

        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '深圳';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            for i in field.keys():
                firstType.append(field[i])

        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and city = '深圳';")
            count = cursor.fetchall()
            for field in count:
                for j in field.keys():
                    value = field[j]

            firstType_data.append({'value': value, 'name': firstType[i]})

        #薪资待遇
        positionName = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(
            ['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + i + "%' and city = '深圳';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(
            ['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + i + "%' and city = '深圳';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + i + "%' and city = '深圳';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and city = '深圳';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and city = '深圳';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])


    else:
        positionName = str(request.args['positionName']).lower()
        # 查询条件：某种职业
        # 行政区
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "' and positionName like '%"+positionName+"%';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)
        # 公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '深圳';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and positionName like '%"+positionName+"%' and city = '深圳';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)
        # 学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '深圳';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '深圳';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)
        #工作经验
        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '深圳';")
        workyear = cursor.fetchall()
        for field in workyear:
            workYear.append(field[0])
            cursor.execute("SELECT count(*) from demo where workYear = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '深圳';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': field[0]})
        # 融资阶段
        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '深圳';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 300})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and positionName like '%" + positionName + "%' and city = '深圳';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])
        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '深圳';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            firstType.append(field[0])
        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and positionName like '%" + positionName + "%' and city = '深圳';")
            count = cursor.fetchall()
            firstType_data.append({'value': count[0][0], 'name': firstType[i]})
        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '深圳' and positionName like '%" + positionName + "%' ;")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)
        # 薪资待遇
        positionName_sample = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        # <10k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + positionName + "%' and city = '深圳';")
        count = cursor.fetchall()
        #print(count)
        for i in count[0].keys():
            value = count[0][i]
        #print(value)
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # print(temp_list)
        # temp_list.append(value)
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 10-20k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + positionName + "%' and city = '深圳';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 20-30k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + positionName + "%' and city = '深圳';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 30-40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + positionName + "%' and city = '深圳';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # >40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + positionName + "%' and city = '深圳';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['>40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    print(zzt_list)
    result = {"district": district, "district_result": district_result, "companySize": companySize, "companySizeResult": companySizeResult, "education": education, "educationResult": educationResult, "workYear_data":workYear_data, "firstType": firstType, "firstType_data": firstType_data, "leida_max_dict":leida_max_dict, "cyt": positionAdvantage, "finance": finance, "finance_data": finance_data, "zzt": zzt_list}
    cursor.close()
    return jsonify(result)

@app.route('/nanjing',methods=['GET'])
def nanjing():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()

    district = []
    district_result = []
    companySize = []
    companySizeResult = []
    education = []
    educationResult = []
    workYear = []
    workYear_data = []
    firstType = []
    firstType_data = []
    finance = []
    finance_data = []
    leida_max_dict = []

    # 获取到的行政区
    cursor.execute("SELECT DISTINCT(district) from demo where city='南京';")
    result = cursor.fetchall()
    for field in result:
        district.append(field[0])
    if (len(request.args) == 0):
        # 没有查询条件
        # 获取到行政区对应的个数
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)

        # 获取到几种公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '南京';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            # 每种公司规模对应的个数
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and city = '南京';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)

        # 获取到几种学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '南京';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            # 每种学历要求对应的个数
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and city = '南京';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)


        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '南京';")
        workyear = cursor.fetchall()
        # 获取到的几种工作经验
        for field in workyear:
            workYear.append(field[0])
        # 获取到每种工作经验对应的个数
        for i in workYear:
            cursor.execute("SELECT count(*) from demo where workYear = '" + i + "' and city = '南京';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': i})

        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '南京';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 10})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and city = '南京';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])

        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '南京';")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)

        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '南京';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            for i in field.keys():
                firstType.append(field[i])

        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and city = '南京';")
            count = cursor.fetchall()
            for field in count:
                for j in field.keys():
                    value = field[j]

            firstType_data.append({'value': value, 'name': firstType[i]})

        #薪资待遇
        positionName = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(
            ['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + i + "%' and city = '南京';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(
            ['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + i + "%' and city = '南京';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + i + "%' and city = '南京';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and city = '南京';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and city = '南京';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])


    else:
        positionName = str(request.args['positionName']).lower()
        # 查询条件：某种职业
        # 行政区
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "' and positionName like '%"+positionName+"%';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)
        # 公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '南京';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and positionName like '%"+positionName+"%' and city = '南京';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)
        # 学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '南京';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '南京';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)
        #工作经验
        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '南京';")
        workyear = cursor.fetchall()
        for field in workyear:
            workYear.append(field[0])
            cursor.execute("SELECT count(*) from demo where workYear = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '南京';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': field[0]})
        # 融资阶段
        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '南京';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 10})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and positionName like '%" + positionName + "%' and city = '南京';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])
        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '南京';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            firstType.append(field[0])
        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and positionName like '%" + positionName + "%' and city = '南京';")
            count = cursor.fetchall()
            firstType_data.append({'value': count[0][0], 'name': firstType[i]})
        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '南京' and positionName like '%" + positionName + "%' ;")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)
        # 薪资待遇
        positionName_sample = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        # <10k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + positionName + "%' and city = '南京';")
        count = cursor.fetchall()
        #print(count)
        for i in count[0].keys():
            value = count[0][i]
        #print(value)
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # print(temp_list)
        # temp_list.append(value)
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 10-20k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + positionName + "%' and city = '南京';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 20-30k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + positionName + "%' and city = '南京';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 30-40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + positionName + "%' and city = '南京';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # >40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + positionName + "%' and city = '南京';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['>40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    print(zzt_list)
    result = {"district": district, "district_result": district_result, "companySize": companySize, "companySizeResult": companySizeResult, "education": education, "educationResult": educationResult, "workYear_data":workYear_data, "firstType": firstType, "firstType_data": firstType_data, "leida_max_dict":leida_max_dict, "cyt": positionAdvantage, "finance": finance, "finance_data": finance_data, "zzt": zzt_list}
    cursor.close()
    return jsonify(result)

@app.route('/xian',methods=['GET'])
def xian():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()

    district = []
    district_result = []
    companySize = []
    companySizeResult = []
    education = []
    educationResult = []
    workYear = []
    workYear_data = []
    firstType = []
    firstType_data = []
    finance = []
    finance_data = []
    leida_max_dict = []

    # 获取到的行政区
    cursor.execute("SELECT DISTINCT(district) from demo where city='西安';")
    result = cursor.fetchall()
    for field in result:
        district.append(field[0])
    if (len(request.args) == 0):
        # 没有查询条件
        # 获取到行政区对应的个数
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)

        # 获取到几种公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '西安';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            # 每种公司规模对应的个数
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and city = '西安';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)

        # 获取到几种学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '西安';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            # 每种学历要求对应的个数
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and city = '西安';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)


        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '西安';")
        workyear = cursor.fetchall()
        # 获取到的几种工作经验
        for field in workyear:
            workYear.append(field[0])
        # 获取到每种工作经验对应的个数
        for i in workYear:
            cursor.execute("SELECT count(*) from demo where workYear = '" + i + "' and city = '西安';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': i})

        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '西安';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 20})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and city = '西安';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])

        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '西安';")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)

        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '西安';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            for i in field.keys():
                firstType.append(field[i])

        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and city = '西安';")
            count = cursor.fetchall()
            for field in count:
                for j in field.keys():
                    value = field[j]

            firstType_data.append({'value': value, 'name': firstType[i]})

        #薪资待遇
        positionName = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(
            ['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + i + "%' and city = '西安';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(
            ['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + i + "%' and city = '西安';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + i + "%' and city = '西安';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and city = '西安';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and city = '西安';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])


    else:
        positionName = str(request.args['positionName']).lower()
        # 查询条件：某种职业
        # 行政区
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "' and positionName like '%"+positionName+"%';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)
        # 公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '西安';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and positionName like '%"+positionName+"%' and city = '西安';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)
        # 学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '西安';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '西安';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)
        #工作经验
        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '西安';")
        workyear = cursor.fetchall()
        for field in workyear:
            workYear.append(field[0])
            cursor.execute("SELECT count(*) from demo where workYear = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '西安';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': field[0]})
        # 融资阶段
        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '西安';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 20})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and positionName like '%" + positionName + "%' and city = '西安';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])
        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '西安';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            firstType.append(field[0])
        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and positionName like '%" + positionName + "%' and city = '西安';")
            count = cursor.fetchall()
            firstType_data.append({'value': count[0][0], 'name': firstType[i]})
        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '西安' and positionName like '%" + positionName + "%' ;")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)
        # 薪资待遇
        positionName_sample = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        # <10k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + positionName + "%' and city = '西安';")
        count = cursor.fetchall()
        #print(count)
        for i in count[0].keys():
            value = count[0][i]
        #print(value)
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # print(temp_list)
        # temp_list.append(value)
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 10-20k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + positionName + "%' and city = '西安';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 20-30k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + positionName + "%' and city = '西安';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 30-40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + positionName + "%' and city = '西安';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # >40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + positionName + "%' and city = '西安';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['>40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    print(zzt_list)
    result = {"district": district, "district_result": district_result, "companySize": companySize, "companySizeResult": companySizeResult, "education": education, "educationResult": educationResult, "workYear_data":workYear_data, "firstType": firstType, "firstType_data": firstType_data, "leida_max_dict":leida_max_dict, "cyt": positionAdvantage, "finance": finance, "finance_data": finance_data, "zzt": zzt_list}
    cursor.close()
    return jsonify(result)

@app.route('/chengdu',methods=['GET'])
def chengdu():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()

    district = []
    district_result = []
    companySize = []
    companySizeResult = []
    education = []
    educationResult = []
    workYear = []
    workYear_data = []
    firstType = []
    firstType_data = []
    finance = []
    finance_data = []
    leida_max_dict = []

    # 获取到的行政区
    cursor.execute("SELECT DISTINCT(district) from demo where city='成都';")
    result = cursor.fetchall()
    for field in result:
        district.append(field[0])
    if (len(request.args) == 0):
        # 没有查询条件
        # 获取到行政区对应的个数
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)

        # 获取到几种公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '成都';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            # 每种公司规模对应的个数
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and city = '成都';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)

        # 获取到几种学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '成都';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            # 每种学历要求对应的个数
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and city = '成都';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)


        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '成都';")
        workyear = cursor.fetchall()
        # 获取到的几种工作经验
        for field in workyear:
            workYear.append(field[0])
        # 获取到每种工作经验对应的个数
        for i in workYear:
            cursor.execute("SELECT count(*) from demo where workYear = '" + i + "' and city = '成都';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': i})

        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '成都';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 120})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and city = '成都';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])

        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '成都';")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)

        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '成都';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            for i in field.keys():
                firstType.append(field[i])

        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and city = '成都';")
            count = cursor.fetchall()
            for field in count:
                for j in field.keys():
                    value = field[j]

            firstType_data.append({'value': value, 'name': firstType[i]})

        #薪资待遇
        positionName = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(
            ['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + i + "%' and city = '成都';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(
            ['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + i + "%' and city = '成都';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + i + "%' and city = '成都';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and city = '成都';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and city = '成都';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])


    else:
        positionName = str(request.args['positionName']).lower()
        # 查询条件：某种职业
        # 行政区
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "' and positionName like '%"+positionName+"%';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)
        # 公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '成都';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and positionName like '%"+positionName+"%' and city = '成都';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)
        # 学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '成都';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '成都';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)
        #工作经验
        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '成都';")
        workyear = cursor.fetchall()
        for field in workyear:
            workYear.append(field[0])
            cursor.execute("SELECT count(*) from demo where workYear = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '成都';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': field[0]})
        # 融资阶段
        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '成都';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 120})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and positionName like '%" + positionName + "%' and city = '成都';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])
        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '成都';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            firstType.append(field[0])
        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and positionName like '%" + positionName + "%' and city = '成都';")
            count = cursor.fetchall()
            firstType_data.append({'value': count[0][0], 'name': firstType[i]})
        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '成都' and positionName like '%" + positionName + "%' ;")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)
        # 薪资待遇
        positionName_sample = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        # <10k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + positionName + "%' and city = '成都';")
        count = cursor.fetchall()
        #print(count)
        for i in count[0].keys():
            value = count[0][i]
        #print(value)
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # print(temp_list)
        # temp_list.append(value)
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 10-20k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + positionName + "%' and city = '成都';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 20-30k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + positionName + "%' and city = '成都';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 30-40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + positionName + "%' and city = '成都';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # >40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + positionName + "%' and city = '成都';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['>40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    print(zzt_list)
    result = {"district": district, "district_result": district_result, "companySize": companySize, "companySizeResult": companySizeResult, "education": education, "educationResult": educationResult, "workYear_data":workYear_data, "firstType": firstType, "firstType_data": firstType_data, "leida_max_dict":leida_max_dict, "cyt": positionAdvantage, "finance": finance, "finance_data": finance_data, "zzt": zzt_list}
    cursor.close()
    return jsonify(result)

@app.route('/wuhan',methods=['GET'])
def wuhan():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()

    district = []
    district_result = []
    companySize = []
    companySizeResult = []
    education = []
    educationResult = []
    workYear = []
    workYear_data = []
    firstType = []
    firstType_data = []
    finance = []
    finance_data = []
    leida_max_dict = []

    # 获取到的行政区
    cursor.execute("SELECT DISTINCT(district) from demo where city='武汉';")
    result = cursor.fetchall()
    for field in result:
        district.append(field[0])
    if (len(request.args) == 0):
        # 没有查询条件
        # 获取到行政区对应的个数
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)

        # 获取到几种公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '武汉';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            # 每种公司规模对应的个数
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and city = '武汉';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)

        # 获取到几种学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '武汉';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            # 每种学历要求对应的个数
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and city = '武汉';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)


        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '武汉';")
        workyear = cursor.fetchall()
        # 获取到的几种工作经验
        for field in workyear:
            workYear.append(field[0])
        # 获取到每种工作经验对应的个数
        for i in workYear:
            cursor.execute("SELECT count(*) from demo where workYear = '" + i + "' and city = '武汉';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': i})

        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '武汉';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 40})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and city = '武汉';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])

        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '武汉';")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)

        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '武汉';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            for i in field.keys():
                firstType.append(field[i])

        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and city = '武汉';")
            count = cursor.fetchall()
            for field in count:
                for j in field.keys():
                    value = field[j]

            firstType_data.append({'value': value, 'name': firstType[i]})

        #薪资待遇
        positionName = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']
        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(
            ['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + i + "%' and city = '武汉';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(
            ['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + i + "%' and city = '武汉';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + i + "%' and city = '武汉';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + i + "%' and city = '武汉';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        temp_list = []
        for i in positionName:
            cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + i + "%' and city = '武汉';")
            count = cursor.fetchall()
            for i in count[0].keys():
                value = count[0][i]
            temp_list.append(value)
        zzt_list.append(['40以上', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])


    else:
        positionName = str(request.args['positionName']).lower()
        # 查询条件：某种职业
        # 行政区
        for i in district:
            cursor.execute("SELECT count(*) from demo where district = '" + i + "' and positionName like '%"+positionName+"%';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': i}
            district_result.append(dict)
        # 公司规模
        cursor.execute("SELECT DISTINCT(companySize) from demo where city = '武汉';")
        company = cursor.fetchall()
        for field in company:
            companySize.append(field[0])
            cursor.execute("SELECT count(*) from demo where companySize = '" + field[0] + "' and positionName like '%"+positionName+"%' and city = '武汉';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            companySizeResult.append(dict)
        # 学历要求
        cursor.execute("SELECT DISTINCT(education) from demo where city = '武汉';")
        eduresult = cursor.fetchall()
        for field in eduresult:
            education.append(field[0])
            cursor.execute("SELECT count(*) from demo where education = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '武汉';")
            count = cursor.fetchall()
            dict = {'value': count[0][0], 'name': field[0]}
            educationResult.append(dict)
        #工作经验
        cursor.execute("SELECT DISTINCT(workYear) from demo where city = '武汉';")
        workyear = cursor.fetchall()
        for field in workyear:
            workYear.append(field[0])
            cursor.execute("SELECT count(*) from demo where workYear = '" + field[0] + "' and positionName like '%" + positionName + "%' and city = '武汉';")
            count = cursor.fetchall()
            workYear_data.append({'value': count[0][0], 'name': field[0]})
        # 融资阶段
        cursor.execute("SELECT DISTINCT(financeStage) from demo where city = '武汉';")
        result = cursor.fetchall()
        # 获取到融资的几种情况
        for field in result:
            finance.append(field[0])
            leida_max_dict.append({'name': field[0], 'max': 40})
        # 获取到每种融资对应的个数
        for i in range(len(finance)):
            cursor.execute("SELECT count(*) from demo where financeStage = '" + finance[i] + "' and positionName like '%" + positionName + "%' and city = '武汉';")
            count = cursor.fetchall()
            finance_data.append(count[0][0])
        # 职位类型
        cursor.execute("SELECT DISTINCT(firstType) from demo where city = '武汉';")
        result = cursor.fetchall()
        # 获取到职位类型的几种情况
        for field in result:
            firstType.append(field[0])
        # 获取到每种职位类型对应的个数
        for i in range(len(firstType)):
            cursor.execute("SELECT count(*) from demo where firstType = '" + firstType[i] + "' and positionName like '%" + positionName + "%' and city = '武汉';")
            count = cursor.fetchall()
            firstType_data.append({'value': count[0][0], 'name': firstType[i]})
        # 职位福利
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select positionAdvantage from `demo` where city = '武汉' and positionName like '%" + positionName + "%' ;")
        data_dict = []
        result = cursor.fetchall()
        for field in result:
            data_dict.append(field['positionAdvantage'])
        content = ''.join(data_dict)
        positionAdvantage = []
        jieba.analyse.set_stop_words('./stopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        for v, n in tags:
            mydict = {}
            mydict["name"] = v
            mydict["value"] = str(int(n * 10000))
            positionAdvantage.append(mydict)
        # 薪资待遇
        positionName_sample = ['java', 'python', 'php', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库']        # 柱状图返回列表
        zzt_list = []
        zzt_list.append(['product', 'Java', 'Python', 'PHP', 'web', 'bi', 'android', 'ios', '算法', '大数据', '测试', '运维', '数据库'])
        # <10k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) like '%k%' and positionName like '%" + positionName + "%' and city = '武汉';")
        count = cursor.fetchall()
        #print(count)
        for i in count[0].keys():
            value = count[0][i]
        #print(value)
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # print(temp_list)
        # temp_list.append(value)
        zzt_list.append(['0—10K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 10-20k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 10 AND 20 and positionName like '%" + positionName + "%' and city = '武汉';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        # temp_list.append(value)
        zzt_list.append(['10—20K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 20-30k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 20 AND 30 and positionName like '%" + positionName + "%' and city = '武汉';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['20—30K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # 30-40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) BETWEEN 30 AND 40 and positionName like '%" + positionName + "%' and city = '武汉';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['30—40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
        # >40k
        temp_list = []
        cursor.execute("SELECT COUNT(*) FROM demo WHERE SUBSTR(salary,1,2) > 40 and positionName like '%" + positionName + "%' and city = '武汉';")
        count = cursor.fetchall()
        for i in count[0].keys():
            value = count[0][i]
        for num in range(len(positionName_sample)):
            if positionName == positionName_sample[num]:
                temp_list.append(value)
            else:
                temp_list.append(0)
        #temp_list.append(value)
        zzt_list.append(['>40K', temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5],temp_list[6], temp_list[7], temp_list[8], temp_list[9], temp_list[10], temp_list[11]])
    print(zzt_list)
    result = {"district": district, "district_result": district_result, "companySize": companySize, "companySizeResult": companySizeResult, "education": education, "educationResult": educationResult, "workYear_data":workYear_data, "firstType": firstType, "firstType_data": firstType_data, "leida_max_dict":leida_max_dict, "cyt": positionAdvantage, "finance": finance, "finance_data": finance_data, "zzt": zzt_list}
    cursor.close()
    return jsonify(result)

@app.route('/area',methods=['GET'])
def area():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡', '181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    #<=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20;")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    #21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40;")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60;")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80;")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100;")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120;")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140;")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160;")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180;")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200;")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    cursor.close()
    print(area_data)
    return jsonify({"area_kind": area_kind, "area_data": area_data})

@app.route('/area_first',methods=['GET'])
def area_first():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡', '181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    #<=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    #21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    cursor.close()
    print(area_data)
    return jsonify({"area_kind": area_kind, "area_data": area_data})

@app.route('/area_nfirst',methods=['GET'])
def area_nfirst():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡', '181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    #<=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    #21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    cursor.close()
    print(area_data)
    return jsonify({"area_kind": area_kind, "area_data": area_data})

@app.route('/area_second',methods=['GET'])
def area_second():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡', '181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    #<=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    #21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    area_data.append(count[0][0])
    cursor.close()
    print(area_data)
    return jsonify({"area_kind": area_kind, "area_data": area_data})

@app.route('/floor',methods=['GET'])
def floor():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(floor) from house;")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "'")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    cursor.close()
    return jsonify({"floor_kind": floor_kind, "floor_data": floor_data})

@app.route('/floor_first',methods=['GET'])
def floor_first():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(floor) from house where city in ('北京','上海','深圳');")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city in ('北京','上海','深圳');")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    cursor.close()
    return jsonify({"floor_kind": floor_kind, "floor_data": floor_data})

@app.route('/floor_nfirst',methods=['GET'])
def floor_nfirst():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(floor) from house where city in ('杭州','南京','武汉','西安','成都','重庆');")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city in ('杭州','南京','武汉','西安','成都','重庆');")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    cursor.close()
    return jsonify({"floor_kind": floor_kind, "floor_data": floor_data})

@app.route('/floor_second',methods=['GET'])
def floor_second():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(floor) from house where city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    cursor.close()
    return jsonify({"floor_kind": floor_kind, "floor_data": floor_data})

@app.route('/orient',methods=['GET'])
def orient():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(orient) from house;")
    result = cursor.fetchall()
    orient_kind = []
    orient_data = []
    # 获取到朝向的几种情况
    for field in result:
        orient_kind.append(field[0])
    # 获取到每种朝向类型对应的个数
    for i in range(len(orient_kind)):
        cursor.execute("SELECT count(*) from house where orient = '" + orient_kind[i] + "'")
        count = cursor.fetchall()
        orient_data.append({'value': count[0][0], 'name': orient_kind[i]})
    cursor.close()
    print(orient_data)
    return jsonify({"orient_kind": orient_kind, "orient_data": orient_data})

@app.route('/orient_first',methods=['GET'])
def orient_first():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(orient) from house where city in ('北京','上海','深圳');")
    result = cursor.fetchall()
    orient_kind = []
    orient_data = []
    # 获取到朝向的几种情况
    for field in result:
        orient_kind.append(field[0])
    # 获取到每种朝向类型对应的个数
    for i in range(len(orient_kind)):
        cursor.execute("SELECT count(*) from house where orient = '" + orient_kind[i] + "' and city in ('北京','上海','深圳');")
        count = cursor.fetchall()
        orient_data.append({'value': count[0][0], 'name': orient_kind[i]})
    cursor.close()
    print(orient_data)
    return jsonify({"orient_kind": orient_kind, "orient_data": orient_data})

@app.route('/orient_nfirst',methods=['GET'])
def orient_nfirst():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(orient) from house where city in ('杭州','南京','武汉','西安','成都','重庆');")
    result = cursor.fetchall()
    orient_kind = []
    orient_data = []
    # 获取到朝向的几种情况
    for field in result:
        orient_kind.append(field[0])
    # 获取到每种朝向类型对应的个数
    for i in range(len(orient_kind)):
        cursor.execute("SELECT count(*) from house where orient = '" + orient_kind[i] + "' and city in ('杭州','南京','武汉','西安','成都','重庆');")
        count = cursor.fetchall()
        orient_data.append({'value': count[0][0], 'name': orient_kind[i]})
    cursor.close()
    print(orient_data)
    return jsonify({"orient_kind": orient_kind, "orient_data": orient_data})

@app.route('/orient_second',methods=['GET'])
def orient_second():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(orient) from house where city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    result = cursor.fetchall()
    orient_kind = []
    orient_data = []
    # 获取到朝向的几种情况
    for field in result:
        orient_kind.append(field[0])
    # 获取到每种朝向类型对应的个数
    for i in range(len(orient_kind)):
        cursor.execute("SELECT count(*) from house where orient = '" + orient_kind[i] + "' and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
        count = cursor.fetchall()
        orient_data.append({'value': count[0][0], 'name': orient_kind[i]})
    cursor.close()
    print(orient_data)
    return jsonify({"orient_kind": orient_kind, "orient_data": orient_data})

@app.route('/price',methods=['GET'])
def price():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000', '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000;")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000;")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000;")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000;")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000;")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000;")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000;")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000;")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000;")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000;")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000;")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    cursor.close()
    print(price_data)
    return jsonify({"price_kind": price_kind, "price_data": price_data})

@app.route('/price_first',methods=['GET'])
def price_first():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000', '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种类别类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    cursor.close()
    print(price_data)
    return jsonify({"price_kind": price_kind, "price_data": price_data})

@app.route('/price_nfirst',methods=['GET'])
def price_nfirst():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000', '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种类别类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    cursor.close()
    print(price_data)
    return jsonify({"price_kind": price_kind, "price_data": price_data})

@app.route('/price_second',methods=['GET'])
def price_second():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000', '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种类别类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    cursor.close()
    print(price_data)
    return jsonify({"price_kind": price_kind, "price_data": price_data})

@app.route('/relation',methods=['GET'])
def relation():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    relation_data = []
    cursor.execute("select count(*) from house;")
    count = cursor.fetchall()
    #print(count[0][0])
    cursor.execute("SELECT area,price from house;")
    result = cursor.fetchall()
    for i in range(count[0][0]):
        relation_data.append(list(result[i]))
    #print(relation_data)
    cursor.close()
    return jsonify({"relation_data": relation_data})

@app.route('/relation_first',methods=['GET'])
def relation_first():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    relation_data = []
    cursor.execute("select count(*) from house where city in ('北京','上海','深圳');")
    count = cursor.fetchall()
    #print(count[0][0])

    cursor.execute("SELECT area,price from house where city in ('北京','上海','深圳');")
    result = cursor.fetchall()
    for i in range(count[0][0]):
        relation_data.append(list(result[i]))
    #print(relation_data)
    cursor.close()
    return jsonify({"relation_data": relation_data})

@app.route('/relation_nfirst',methods=['GET'])
def relation_nfirst():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    relation_data = []
    cursor.execute("select count(*) from house where city in ('杭州','南京','武汉','西安','成都','重庆');")
    count = cursor.fetchall()
    #print(count[0][0])

    cursor.execute("SELECT area,price from house where city in ('杭州','南京','武汉','西安','成都','重庆');")
    result = cursor.fetchall()
    for i in range(count[0][0]):
        relation_data.append(list(result[i]))
    #print(relation_data)
    cursor.close()
    return jsonify({"relation_data": relation_data})

@app.route('/relation_second',methods=['GET'])
def relation_second():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    cursor = conn.cursor()
    relation_data = []
    cursor.execute("select count(*) from house where city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    count = cursor.fetchall()
    #print(count[0][0])

    cursor.execute("SELECT area,price from house where city in ('兰州','大连','贵阳','石家庄','太原','徐州');")
    result = cursor.fetchall()
    for i in range(count[0][0]):
        relation_data.append(list(result[i]))
    #print(relation_data)
    cursor.close()
    return jsonify({"relation_data": relation_data})

@app.route('/bj',methods=['GET'])
def bj():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '北京';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '北京';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '北京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '北京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '北京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '北京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '北京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '北京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '北京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '北京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '北京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '北京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '北京';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '北京';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '北京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max': 500})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '北京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max': 500})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '北京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max': 500})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '北京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 500})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '北京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 500})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '北京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 500})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '北京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 500})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '北京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 500})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '北京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 500})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '北京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 500})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '北京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 500})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

@app.route('/sh',methods=['GET'])
def sh():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '上海';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '上海';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '上海';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '上海';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '上海';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '上海';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '上海';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '上海';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '上海';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '上海';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '上海';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '上海';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '上海';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '上海';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '上海';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max': 700})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '上海';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max': 700})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '上海';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max': 700})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '上海';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 700})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '上海';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 700})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '上海';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 700})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '上海';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 700})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '上海';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 700})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '上海';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 700})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '上海';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 700})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '上海';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 700})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

@app.route('/sz',methods=['GET'])
def sz():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '深圳';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '深圳';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '深圳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '深圳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '深圳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '深圳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '深圳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '深圳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '深圳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '深圳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '深圳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '深圳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '深圳';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '深圳';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '深圳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max': 400})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '深圳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max': 400})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '深圳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max': 400})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '深圳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 400})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '深圳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 400})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '深圳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 400})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '深圳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 400})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '深圳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 400})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '深圳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 400})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '深圳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 400})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '深圳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 400})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

@app.route('/hz',methods=['GET'])
def hz():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '杭州';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '杭州';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '杭州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '杭州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '杭州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '杭州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '杭州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '杭州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '杭州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '杭州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '杭州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '杭州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '杭州';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '杭州';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '杭州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max': 600})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '杭州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max': 600})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '杭州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max': 600})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '杭州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 600})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '杭州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 600})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '杭州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 600})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '杭州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 600})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '杭州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 600})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '杭州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 600})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '杭州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 600})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '杭州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 600})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

@app.route('/wh',methods=['GET'])
def wh():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '武汉';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '武汉';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '武汉';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '武汉';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '武汉';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '武汉';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '武汉';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '武汉';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '武汉';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '武汉';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '武汉';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '武汉';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '武汉';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '武汉';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '武汉';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max': 1000})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '武汉';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max': 1000})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '武汉';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max': 1000})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '武汉';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 1000})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '武汉';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 1000})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '武汉';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 1000})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '武汉';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 1000})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '武汉';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 1000})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '武汉';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 1000})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '武汉';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 1000})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '武汉';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 1000})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

@app.route('/nj',methods=['GET'])
def nj():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '南京';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '南京';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '南京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '南京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '南京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '南京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '南京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '南京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '南京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '南京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '南京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '南京';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '南京';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '南京';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '南京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max': 1000})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '南京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max': 1000})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '南京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max': 1000})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '南京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 1000})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '南京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 1000})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '南京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 1000})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '南京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 1000})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '南京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 1000})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '南京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 1000})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '南京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 1000})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '南京';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 1000})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

@app.route('/xa',methods=['GET'])
def xa():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '西安';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '西安';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '西安';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '西安';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '西安';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '西安';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '西安';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '西安';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '西安';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '西安';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '西安';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '西安';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '西安';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '西安';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '西安';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max': 900})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '西安';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max': 900})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '西安';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max': 900})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '西安';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 900})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '西安';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 900})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '西安';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 900})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '西安';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 900})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '西安';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 900})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '西安';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 900})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '西安';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 900})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '西安';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 900})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

@app.route('/cq',methods=['GET'])
def cq():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '重庆';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '重庆';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '重庆';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '重庆';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '重庆';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '重庆';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '重庆';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '重庆';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '重庆';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '重庆';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '重庆';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '重庆';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '重庆';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '重庆';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '重庆';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max': 1200})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '重庆';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max': 1200})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '重庆';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max': 1200})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '重庆';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 1200})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '重庆';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 1200})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '重庆';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 1200})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '重庆';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 1200})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '重庆';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 1200})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '重庆';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 1200})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '重庆';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 1200})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '重庆';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 1200})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

@app.route('/cd',methods=['GET'])
def cd():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '成都';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '成都';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '成都';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '成都';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '成都';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '成都';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '成都';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '成都';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '成都';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '成都';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '成都';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '成都';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '成都';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '成都';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '成都';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max':1100})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '成都';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max':1100})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '成都';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max':1100})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '成都';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 1100})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '成都';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 1100})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '成都';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 1100})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '成都';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 1100})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '成都';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 1100})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '成都';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 1100})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '成都';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 1100})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '成都';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 1100})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

@app.route('/lz',methods=['GET'])
def lz():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '兰州';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '兰州';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '兰州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '兰州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '兰州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '兰州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '兰州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '兰州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '兰州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '兰州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '兰州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '兰州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '兰州';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '兰州';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '兰州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max':1200})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '兰州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max':1200})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '兰州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max':1200})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '兰州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 1200})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '兰州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 1200})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '兰州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 1200})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '兰州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 1200})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '兰州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 1200})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '兰州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 1200})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '兰州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 1200})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '兰州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 1200})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

@app.route('/dl',methods=['GET'])
def dl():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '大连';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '大连';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '大连';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '大连';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '大连';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '大连';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '大连';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '大连';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '大连';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '大连';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '大连';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '大连';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '大连';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '大连';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '大连';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max':1000})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '大连';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max':1000})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '大连';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max':1000})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '大连';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 1000})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '大连';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 1000})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '大连';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 1000})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '大连';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 1000})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '大连';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 1000})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '大连';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 1000})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '大连';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 1000})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '大连';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 1000})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

@app.route('/gy',methods=['GET'])
def gy():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '贵阳';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '贵阳';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '贵阳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '贵阳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '贵阳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '贵阳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '贵阳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '贵阳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '贵阳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '贵阳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '贵阳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '贵阳';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '贵阳';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '贵阳';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '贵阳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max':1300})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '贵阳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max':1300})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '贵阳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max':1300})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '贵阳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 1300})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '贵阳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 1300})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '贵阳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 1300})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '贵阳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 1300})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '贵阳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 1300})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '贵阳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 1300})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '贵阳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 1300})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '贵阳';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 1300})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

@app.route('/sjz',methods=['GET'])
def sjz():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '石家庄';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '石家庄';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '石家庄';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '石家庄';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '石家庄';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '石家庄';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '石家庄';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '石家庄';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '石家庄';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '石家庄';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '石家庄';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '石家庄';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '石家庄';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '石家庄';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '石家庄';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max': 1700})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '石家庄';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max': 1700})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '石家庄';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max': 1700})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '石家庄';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 1700})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '石家庄';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 1700})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '石家庄';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 1700})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '石家庄';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 1700})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '石家庄';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 1700})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '石家庄';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 1700})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '石家庄';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 1700})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '石家庄';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 1700})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

@app.route('/ty',methods=['GET'])
def ty():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '太原';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '太原';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '太原';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '太原';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '太原';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '太原';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '太原';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '太原';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '太原';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '太原';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '太原';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '太原';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '太原';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '太原';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '太原';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max':1600})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '太原';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max':1600})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '太原';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max':1600})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '太原';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 1600})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '太原';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 1600})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '太原';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 1600})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '太原';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 1600})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '太原';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 1600})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '太原';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 1600})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '太原';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 1600})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '太原';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 1600})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

@app.route('/xz',methods=['GET'])
def xz():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3366, db='lagou',
                           charset='utf8mb4')
    # 创建一个游标对象cursor
    cursor = conn.cursor()
    # 行政区
    cursor.execute("SELECT DISTINCT(district) from house where city = '徐州';")
    result = cursor.fetchall()
    district = []
    district_data = []
    for field in result:
        district.append(field[0])
    for i in range(len(district)):
        cursor.execute("SELECT count(*) from house where district = '" + district[i] + "' and city = '徐州';")
        count = cursor.fetchall()
        district_data.append({'value': count[0][0], 'name': district[i]})
    #面积
    area_kind = ['<=20㎡', '21~40㎡', '41~60㎡', '61~80㎡', '81~100㎡', '101~120㎡', '121~140㎡', '141~160㎡', '161~180㎡','181~200㎡']
    area_data = []
    # 获取到每种面积类别对应的个数
    # <=20㎡
    cursor.execute("SELECT count(*) from house where area between 0 and 20 and city = '徐州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[0]})
    # 21~40㎡
    cursor.execute("SELECT count(*) from house where area between 21 and 40 and city = '徐州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[1]})
    # 41~60㎡
    cursor.execute("SELECT count(*) from house where area between 41 and 60 and city = '徐州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[2]})
    # 61~80㎡
    cursor.execute("SELECT count(*) from house where area between 61 and 80 and city = '徐州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[3]})
    # 81~100㎡
    cursor.execute("SELECT count(*) from house where area between 81 and 100 and city = '徐州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[4]})
    # 101~120㎡
    cursor.execute("SELECT count(*) from house where area between 101 and 120 and city = '徐州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[5]})
    # 121~140㎡
    cursor.execute("SELECT count(*) from house where area between 121 and 140 and city = '徐州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[6]})
    # 141~160㎡
    cursor.execute("SELECT count(*) from house where area between 141 and 160 and city = '徐州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[7]})
    # 161~180㎡
    cursor.execute("SELECT count(*) from house where area between 161 and 180 and city = '徐州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[8]})
    # 181~200㎡
    cursor.execute("SELECT count(*) from house where area between 181 and 200 and city = '徐州';")
    count = cursor.fetchall()
    area_data.append({'value': count[0][0], 'name':area_kind[9]})
    #楼层
    cursor.execute("SELECT DISTINCT(floor) from house where city = '徐州';")
    result = cursor.fetchall()
    floor_kind = []
    floor_data = []
    # 获取到楼层的几种情况
    for field in result:
        floor_kind.append(field[0])
    # 获取到每种楼层类型对应的个数
    for i in range(len(floor_kind)):
        cursor.execute("SELECT count(*) from house where floor = '" + floor_kind[i] + "' and city = '徐州';")
        count = cursor.fetchall()
        floor_data.append({'value': count[0][0], 'name': floor_kind[i]})
    #价格
    max_dict = []
    price_kind = ['<=1000', '1001~2000', '2001~3000', '3001~4000', '4001~5000', '5001~6000', '6001~7000', '7001~8000',
                  '8001~9000', '9001~10000', '>10000']
    price_data = []
    # 获取到每种价格类别对应的个数
    # <=1000
    cursor.execute("SELECT count(*) from house where price between 0 and 1000 and city = '徐州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[0], 'max':1600})
    # 1001~2000
    cursor.execute("SELECT count(*) from house where price between 1001 and 2000 and city = '徐州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[1], 'max':1600})
    # 2001~3000
    cursor.execute("SELECT count(*) from house where price between 2001 and 3000 and city = '徐州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[2], 'max':1600})
    # 3001~4000
    cursor.execute("SELECT count(*) from house where price between 3001 and 4000 and city = '徐州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[3], 'max': 1600})
    # 4001~5000
    cursor.execute("SELECT count(*) from house where price between 4001 and 5000 and city = '徐州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[4], 'max': 1600})
    # 5001~6000
    cursor.execute("SELECT count(*) from house where price between 5001 and 6000 and city = '徐州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[5], 'max': 1600})
    # 6001~7000
    cursor.execute("SELECT count(*) from house where price between 6001 and 7000 and city = '徐州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[6], 'max': 1600})
    # 7001~8000
    cursor.execute("SELECT count(*) from house where price between 7001 and 8000 and city = '徐州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[7], 'max': 1600})
    # 8001~9000
    cursor.execute("SELECT count(*) from house where price between 8001 and 9000 and city = '徐州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[8], 'max': 1600})
    # 9001~10000
    cursor.execute("SELECT count(*) from house where price between 9001 and 10000 and city = '徐州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[9], 'max': 1600})
    # >10000
    cursor.execute("SELECT count(*) from house where price >10000 and city = '徐州';")
    count = cursor.fetchall()
    price_data.append(count[0][0])
    max_dict.append({'name': price_kind[10], 'max': 1600})

    cursor.close()
    return jsonify({"district":district, "district_data":district_data, "area_data":area_data, "floor_kind":floor_kind, "floor_data":floor_data,
                    "price_data":price_data, "max_dict":max_dict})

if __name__ == "__main__":
   app.run(port=5000)