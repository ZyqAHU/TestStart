from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/history')
def movie():
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("history.html",movies = datalist)




    return render_template("history.html")

@app.route('/men')
def score():
    score = []
    judgenum = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        judgenum.append(item[1])
    cur.close()
    con.close()
    return render_template("men.html",score = score,num = judgenum)

@app.route('/database')
def word():
    return render_template("database.html")

@app.route('/wordcloud')
def team():
    return render_template("wordcloud.html")


if __name__ == '__main__':
    app.run(debug=True)
