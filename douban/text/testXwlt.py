# -*- codeing = utf-8 -*-
# @Time : 2022/4/4 17:36
# @Author : ahu_zyq
# @File : testXwlt.py
# @softwawre : PyCharm

import xlwt
'''
workbook = xlwt.Workbook(encoding="utf-8")  #创建workbook对象
worksheet = workbook.add_sheet('sheet1')    #创建工作表

# worksheet.write(0,0,'hello')                #写入数据，（行，列，参数内容）
workbook.save('student.xls')                #保存数据表
'''
workbook = xlwt.Workbook(encoding="utf-8")  #创建workbook对象
worksheet = workbook.add_sheet('sheet1')    #创建工作表