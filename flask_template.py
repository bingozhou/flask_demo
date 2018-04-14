# coding=utf8
from flask import Flask,render_template

# 处理中文编码问题
import sys

reload(sys)

sys.setdefaultencoding('utf8')



app = Flask(__name__)


# 模版传入

@app.route('/')
def hello_world():
    url_str = 'www.baidu.com'
    my_list = [1,3,5,7]
    my_dict = {
        'name':'小明',
        'age':'28'
    }
    my_int = 12
    return render_template('index.html',
                           url_str=url_str,
                           my_list=my_list,
                           my_dict=my_dict,
                           my_int=my_int)

if __name__ == '__main__':
    app.run(debug=True)
