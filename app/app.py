from flask import Flask, request, render_template, redirect, session, jsonify,url_for
import uuid
import queue
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login',methods = ['GET',"POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('user')
        sql = sqlite3.connect("data.db")
        print(list(sql.execute('select sid from student')))
        #if user in list(sql.execute('select sid from student')):
        return redirect(url_for('vote'))

@app.route('/vote',methods=['GET','POST'])
def vote():
    if request.method == "GET":
        return render_template('student.html')


if __name__ == '__main__':
    app.run(threaded=True)