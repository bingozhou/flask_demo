import os
import time,datetime


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

# file_list = os.listdir(r'E:\project\flask_demo\filedown_up\media')
#
# print file_list

print get_FileSize(r'E:\project\flask_demo\filedown_up\media\ZeroTier One.msi')

print get_FileCreateTime(r'E:\project\flask_demo\filedown_up\media\ZeroTier One.msi')


name = '01.jpg'
path = os.path.join("E:\project\\flask_demo\\filedown_up\media", name)
print path


a = [1,3,5]
b = [2,4,8]
c = [3,7,13]

d = zip(a,b)

e = zip(d,c)

print e