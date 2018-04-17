# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import send_from_directory, \
    Flask,url_for,request,render_template

import os

import time



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + '/media/'
# 设置文件上传的路径 os.getcwd() 返回当前进程的工作目录
# 项目原文件目录需要有一个media文件夹，用来存放上传文件，如不设置，则和源文件同一目录



html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>Photo Upload</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=upload>
    </form>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # 提供对已上传文件的访问服务
    # 下载也可以使用此url
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/file/<filename>')
def upload_file(filename):
    file_url = url_for('uploaded_file', filename=filename)
    print file_url
    print filename
    return html+'<br><a href='+file_url+' '+'download='+filename+'>加链接处</a>'

# @app.route('/list')
# def file_list():
#     file_list = os.listdir(r'E:\project\flask_demo\filedown_up\media')
#     return render_template('download.html',file_list=file_list)

@app.route('/list')
def file_list():
    file_size = []
    file_creatime = []
    file_name = os.listdir(r'E:\project\flask_demo\filedown_up\media')
    record = []
    for name in file_name:
        name = name.encode('gb2312')
        path = os.path.join("E:\project\\flask_demo\\filedown_up\\media",name)
        # print path
        # file_size.append(get_FileSize(path))
        # file_creatime.append(get_FileCreateTime(path))
        record.append(name)
        record.append(get_FileSize(path))
        record.append(get_FileCreateTime(path))

    return render_template('file_list.html',records=record)




def get_FileSize(filePath):
    filePath = unicode(filePath, 'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)

def get_FileCreateTime(filePath):
    filePath = unicode(filePath,'utf8')
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)

def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)


if __name__ == '__main__':
    app.debug = True
    app.run()