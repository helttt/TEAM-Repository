from flask import Flask, redirect, url_for, request
from flask.templating import render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['GET'])
def result():
    sql = sqlite3.connect("data.db")
    data = {}
    for i in range(1, 12):
        data[i] = len(
            list(sql.execute('select * from vote where gid=?', (i,))))
    sql.close()
    return render_template("result.html", data=data)

@app.route('/data', methods=['POST'])
def data():
    sql = sqlite3.connect("data.db")
    string = ""
    data2 = list(sql.execute('select * from vote order by sid'))
    for i in data2:
        string += i[0] + ' 投给第' + str(i[1]) + '组\r\n'
    sql.close()
    return render_template('data.html', string=string)

@app.route('/index', methods=['POST'])
def index():
    sql = sqlite3.connect("data.db")
    for i in range(1, 12):
        group = request.form.get("g"+str(i))
        if group != None:
            print(group)
            insert = 'insert into vote values(?, ?)'
            sid = request.form.get("sid")
            insertData = (sid, i)
            sql.execute(insert, insertData)
    sql.commit()
    sql.close()
    return redirect(url_for('result'))


if __name__ == '__main__':
    app.run(debug=True)
