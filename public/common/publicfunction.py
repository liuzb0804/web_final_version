#coding=utf-8
import time
from config import globalparam


#截图放到report下的img目录下
def get_img(dr, filename):
    path = globalparam.img_path + '\\' + filename
    # path = path.encode('raw_unicode_escape')
    # path = path.replace('\\','/')
    dr.take_screenshot(path)



# A = 'C:\\Users\\zk\\PycharmProjects\\web_final_version\\report\\img\\123.png'
# B = A.replace('\\','/')
# print B
# print type(B)
# C = u'C:\\Users\\zk\\PycharmProjects\\web_final_version\\report\\img\\123.png'
# D = C.replace('\\','/')
# print D
# print type(D)
# C = B.encode('raw_unicode_escape')
# print A
# print type(A)
# print B
# print type(B)
# print C
# print type(C)





# file_path = r'D:/python/Daemon_/report/screenpicture/'
# rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
# screen_name = file_path + rq + '.png'
# print screen_name