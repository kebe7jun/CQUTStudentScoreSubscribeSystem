#!/usr/bin/env python
#coding=gbk

import re
import os
import datetime
import time
import LoginCQUT

fc = open('classes.txt')
tt = time.time()
opener = LoginCQUT.LoginCQUTCookie('11303070104','password').login()
rep = opener.open('http://i.cqut.edu.cn/zfca?yhlx=student&login=0122579031373493743&url=login')    #½øÈëÑ§¹¤ÏµÍ³
# print rep.read().decode('gb2312').encode('utf-8')
for cno in fc:
    if time.time() - tt > 25*60:
        opener = LoginCQUT.LoginCQUTCookie('11303070104','password').login()
        rep = opener.open('http://i.cqut.edu.cn/zfca?yhlx=student&login=0122579031373493743&url=login')
        tt = time.time()
        print 'Relogin  ----- '+datetime.datetime.now().__str__()
    cno = re.findall('([0-9]+)', cno)[0]
    if len(cno) < 9:
        continue
    os.mkdir('./'+cno)
    print cno+' class is getting... ----- '+datetime.datetime.now().__str__()
    for i in range(1,45):
        sno = cno+"{0:0>2}".format(i)
        try:
            rep = opener.open('http://ykt.cqut.edu.cn:8088/zncard/personAccountJasperreport.do?startTime=2010-03-29&endTime=2016-03-29&cardNo='+sno+'&queryType=0&displayType=report')    #»ñÈ¡ÕÕÆ¬
        except:
            print 'error'
        f = open(cno+'/'+sno+'.html','w')
        f.write(rep.read())
        f.close()
    