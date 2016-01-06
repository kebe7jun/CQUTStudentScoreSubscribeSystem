#coding=gbk

import re
import os
import datetime
import LoginCQUT


# cookie = LoginCQUT.LoginCQUTCookie('11303070104','').login()
opener = LoginCQUT.LoginCQUTCookie('11303070104','password').login()

rep = opener.open('http://i.cqut.edu.cn/zfca?yhlx=student&login=122579031373493679&url=stuPage.jsp')    #进入学工系统
fc = open('classes.txt')
for cno in fc:
    cno = re.findall('([0-9]+)', cno)[0]
    if len(cno) < 9:
        continue
    os.mkdir('./'+cno)
    print cno+' class is getting... ----- '+datetime.datetime.now().__str__()
    for i in range(1,45):
        sno = cno+"{0:0>2}".format(i)
        rep = opener.open('http://xgxt.i.cqut.edu.cn/xgxt/xsxx_xsgl.do?method=showPhoto&xh='+sno)    #获取照片
        f = open(cno+'/'+sno+'.jpg','wb')
        f.write(rep.read())
        f.close()
        