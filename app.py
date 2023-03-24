from flask import Flask,render_template
import datetime

app = Flask(__name__)


#路由解析：通过用户访问的路径，匹配相应的函数
# @app.route("/")
# def index():
# 	return render_template("index.html")


#向页面传递一个变量
@app.route("/")
def index():
	time = datetime.date.today()	#普通变量
	name = ["小张","小王","小赵"]		#列表变量
	return render_template("index.html",var = time,list = name)

#通过访问路径，获取用户的整型参数
@app.route("/user/<int:id>")
def welcome2(id):
	return "你好，%d的会员"%id


#路由路径不能重复，用户通过唯一路径访问特定的函数

if __name__ == '__main__':
    app.run(debug=True)
