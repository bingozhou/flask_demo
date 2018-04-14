# coding=utf8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# 请求方式限定  POST 或者 GET,默认是GET

@app.route('/new',methods=['GET','POST'])
def hello_new():
    return 'Hello get or post'

# 路由动态传参数,并限制参数的类型为int,默认为float类型

@app.route('/order/<int:order_id>')
def get_order_id(order_id):
    return 'order id is %s' % order_id



if __name__ == '__main__':
    app.run(debug=True)
