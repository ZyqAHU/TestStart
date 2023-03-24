# -*- codeing = utf-8 -*-
# @Time : 2022/4/5 20:02
# @Author : ahu_zyq
# @File : testSqlite.py
# @softwawre : PyCharm

import sqlite3

#创建数据表
# conn = sqlite3.connect("test.db")   #打开获创建数据库文件
#
# print("成功打开数据库")
#
# c = conn.cursor()
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''
#
# c.execute(sql)  #执行sql语句
# conn.commit()   #提交数据库操作
# conn.close()    #关闭数据库连接
#
#
# print("Opened database successfully")

#插入数据
# conn = sqlite3.connect("test.db")   #打开获创建数据库文件
#
# print("成功打开数据库")
#
# c = conn.cursor()
# sql1 = '''
#   insert into company (id,name,age,address,salary)
#     values (1,'张三',30,"成都",10000);
# '''
#
# c.execute(sql1)  #执行sql语句
# conn.commit()   #提交数据库操作
# conn.close()    #关闭数据库连接
#
#
# print("插入数据完毕")


#查询数据
conn = sqlite3.connect("test.db")   #打开获创建数据库文件

print("成功打开数据库")

c = conn.cursor()
sql = "select id,name,age,address,salary from company"


cursor = c.execute(sql)  #执行sql语句
for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("age = ",row[2])
    print("address = ",row[3])
    print("address = ",row[4])



conn.close()    #关闭数据库连接


print("查询完毕")