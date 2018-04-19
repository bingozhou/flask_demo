flask前后台交互数据的几个思路
通过url进行参数传递：
@app.route('/hello/<name>')   # <name>为传递的参数
def hello(name=None):
    return render_template('src/hello.html',name=name)
hello.html的内容：

<!doctype html>
<title>Hello from Flask</title>
{% if name %}
<h1>Hello {{ name }}!</h1>
{% else %}
<h1>Hello World!</h1>
{% endif %}
其 中，name作为传入的变量。render_template()方法可以用来直接渲染模板，免去繁琐的html生成工作。 render_template方法只需传入需要渲染的模板名和传递个模板引擎（flask采用的是Jinja2）的参数。模板名需要放置在项目根目录下 的templates目录。

HTTP方法：
flask中一个route默认只应答http的get方法。可以通过methods参数指定具体能够应答的http方法。

@app.route('/test', methods=['POST','GET'])    # 可以应答POST和GET方法
def test():
    print(request.method)                      # request对象封装了http的request请求
    print(request.form['username'])            # form为前端的表单，request.form属于dict类型
    return 'response back'                     # 返回字符串类型的结果
如果要返回json字符串，可以使用如下方法：

jsonStr={'result':'hello world'}
return jsonify(jsonStr)                        # 或者json.dumps(jsonStr)
jsonStr 是dict类型，然后通过jsonify方法直接将dict类型转换为json串。当然也可以使用json.dumps（jsonStr）将dict转换 为json字符串。jsonify是flask自带的json处理类，返回的为flask结果，处理json串还携带了content- type="application/json"。json.dumps是单纯的转换为json串。另外json.dumps能够处理的类型比 jsonify多，比如list类型。

静态文件：
静态文件（比如css等）需要存放于根目录下的static目录下。可以通过url_for方法产生静态文件的url。 比如：

url_for('static', filename='style.css')
cookies&session：
读取cookie参数：

from flask import request
@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
设置cookie参数：

from flask import make_response
@app.route('/')
def index():
    resp = make_response(render_template(...))    # Converts the return value from a view function to a real response object that is an instance of response_class.
    resp.set_cookie('username', 'the username')
    return resp
session的一个例子：

from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)
@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])    # session是dict类型
    return 'You are not logged in'
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']            # 设置session中的username变量
        return redirect(url_for('index'))
    return '''''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)                                 # 移除session中的username变量
    return redirect(url_for('index'))
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
密钥的获取方式：

>>> import os
>>> os.urandom(24)

通过ajax读写后台数据


通过json读写数据