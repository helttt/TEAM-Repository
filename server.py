from flask import Flask, redirect, url_for, request
from flask.templating import render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/result', methods=['GET'])
def result():
    sql = sqlite3.connect("data.db")
    string = ""
    for i in range(1, 12):
        data = len(list(sql.execute('select * from vote where gid=?', (i,))))
        string += '第' + str(i) + '组: ' + str(data) + '\r\n'
    sql.close()
    return string


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        sql = sqlite3.connect("data.db")
        for i in range(1, 12):
            group = request.form.get("g"+str(i))
            if group != None:
                print(group)
                insert = 'insert into vote values(?, ?)'
                insertData = ('00000000', i)
                sql.execute(insert, insertData)
        sql.commit()
        sql.close()
        return redirect(url_for('result'))
    # else:
    #     group = request.args.get('g1')
    #     print(group)
        # return redirect(url_for('success', name=group))
    # return False


if __name__ == '__main__':
    app.run(debug=True)
