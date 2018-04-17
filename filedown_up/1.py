# -*- coding: utf-8 -*-
import os
from flask import Flask, request, url_for, send_from_directory
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# 设置可以上传文件的后缀

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + '/media/'
# 设置文件上传的路径 os.getcwd() 返回当前进程的工作目录
# 项目原文件目录需要有一个media文件夹，用来存放上传文件，如不设置，则和源文件同一目录
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# 设置最大的上传数量


html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>Photo Upload</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=upload>
    </form>
    '''


def allowed_file(filename):
    # 检查文件类型是否有效
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # 提供对已上传文件的访问服务
    # 下载也可以使用此url
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_url = url_for('uploaded_file', filename=filename)
            return html + '<br><img src=' + file_url + '>' + '<a href="' + file_url + '" download="w3logo"> <img border="2" src=" ' + file_url + '" alt="W3School"></a>'
    return html


if __name__ == '__main__':
    app.debug = True
    app.run()