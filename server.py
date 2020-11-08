from flask import Flask, redirect, url_for, request
from flask.templating import render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/student', methods=['POST'])
def student():
    sid = request.form.get("id")
    sql = sqlite3.connect("data.db")
    if (sid,) not in list(sql.execute('select sid from student')):
        sql.close()
        return render_template('login.html', error=2)
    elif (sid,) in list(sql.execute('select sid from vote')):
        sql.close()
        return redirect(url_for('result'))
    else:
        gid = list(sql.execute('select gid from student where sid=?', (sid,)))
        gid = gid[0][0]
        sql.close()
        return render_template('index.html', sid=sid, gid=gid)

@app.route('/result', methods=['GET'])
def result():
    sql = sqlite3.connect("data.db")
    data = {}
    for i in range(1, 12):
        data[i] = len(
            list(sql.execute('select * from vote where gid=?', (i,))))
    sql.close()
    return render_template("result.html", data=data)

@app.route('/teacher', methods=['POST'])
def teacher():
    sql = sqlite3.connect("data.db")
    data = {}
    for i in range(1, 12):
        data[i] = len(
            list(sql.execute('select * from vote where gid=?', (i,))))
    for i in range(1, 12):
        vote = list(sql.execute('select student.sid, sname, vote.gid from student, vote where student.sid = vote.sid and vote.gid = ?', (i,)))
        string = str()
        for j in vote:
            if string != "":
                string += '、'
            # string += j[0]
            string += j[1]
        if string == "":
            string = "无"
        data[i+11] = string
    sql.close()
    print(data)
    return render_template('teacher.html', data=data)

@app.route('/vote', methods=['POST'])
def vote():
    sql = sqlite3.connect("data.db")
    sid = request.form.get("sid")
    if (sid,) not in list(sql.execute('select sid from vote')):
        for i in range(1, 12):
            group = request.form.get("g"+str(i))
            if group != None:
                insert = 'insert into vote values(?, ?)'
                insertData = (sid, i)
                sql.execute(insert, insertData)
        sql.commit()
        sql.close()
        return redirect(url_for('result'))
    else:
        sql.close()
        return redirect(url_for('result'))


if __name__ == '__main__':
    app.run(debug=True)
