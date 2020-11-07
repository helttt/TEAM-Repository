from flask import Flask, request, render_template, redirect, session, jsonify
import uuid
import queue
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'asdfasdf'
bootstrap = Bootstrap(app)
# 定义一个字典，用于存放用户的queue  键为uuid
USER_QUEUE = {

}


# 在用户访问之前判断是否登录，注意这里的before_request没有括号
@app.before_request
def check_login():
    # 如果用户访问login则直接让访问
    if request.path == '/login':
        return None
    user = session.get('user_info')
    if not user:
        return redirect('/login')


@app.route('/login', methods=['GET', "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        uid = str(uuid.uuid4())  # 生成一个uuid
        USER_QUEUE[uid] = queue.Queue()
        # 把用户登录信息放入到session 中去
        session['user_info'] = {'uid': uid, 'name': user}
        return redirect('/index')


# 假装这是数据库，里边有数据
GENTILEMAN = {
    '1': {'name': '向龙', 'count': 0},
    '2': {'name': '霄汉', 'count': 0},
}


@app.route('/index')
def index():
    # 从数据库中取出数据，返回给前端
    return render_template('index.html', gg=GENTILEMAN)


@app.route('/get_new_count')
def get_new_count():
    """
    获取用户session中的uid
    根据uid获取当前登录用的队列
    :return:
    """
    # 定义一个字典，里边放着从queue中取出的数据，status为False的时候代表里边没有值，让前端继续过来 长轮询
    ret = {'status': True, 'data': None}
    uid = session['user_info']['uid']

    q = USER_QUEUE[uid]  # 在字典中取出用户的queue
    try:
        # 视图从queue中取出数据，最多等10秒  长轮询之 夯住操作，一直在等queue中是否能取出数据，取出去之后直接返回，或是10秒之后没有的话返回数据，
        data = q.get(timeout=10)
        ret['data'] = data
        # 如果queue中被取空的话，报错
    except queue.Empty as e:
        ret['status'] = False

    return jsonify(ret)


@app.route('/vote', methods=['POST'])
def vote():
    """
    接收用户请求，对帅哥进行投票
    :return:
    """
    gid = request.form.get('gid')
    old = GENTILEMAN[gid]['count']
    new = old + 1
    GENTILEMAN[gid]['count'] = new

    data = {'gid': gid, 'count': new}
    for q in USER_QUEUE.values():
        q.put(data)

    return 'OK'


if __name__ == '__main__':
    app.run(threaded=True)