#!/usr/bin/python
#coding=utf-8
'''
@author: KEBE 
'''
import urllib
import os
import sys
import re

import LoginCQUT
import StudentScore
import SendScore
import Tools

STUDENT_NO = ''
STUDENT_PWD = ''
STUDENT_PHONE = ''
STUDENT_EMAIL = ''
SCORE_FILE_NAME = ''

def getScorePage():     #获取信息
    opener = LoginCQUT.LoginCQUTCookie(STUDENT_NO, STUDENT_PWD).login()
    rep = opener.open('http://i.cqut.edu.cn/zfca?yhlx=student&login=0122579031373493728&url=xscj_gc.aspx')
    scoreUrl = rep.geturl()
    h = rep.read()
        #原来以为这个值不变，但是后来发现这个值会变，所以要提取
    VIEWSTATE = re.findall(r'__VIEWSTATE" value="(.*)"', h)  #提取lt的value
    postdata = urllib.urlencode({
                                 '__VIEWSTATE':VIEWSTATE[0],
                                 'ddlXN':'',
                                 'ddlXQ':'',
                                 'Button1':'按学期查询'.decode('utf-8').encode('gb2312')
                                 }) 
    rep = opener.open(scoreUrl, postdata)
    return rep.read().decode('gb2312').encode('utf-8')

def main():
    html = getScorePage()
    if os.path.exists(SCORE_FILE_NAME): #如果已经获取过文件
        f = open(SCORE_FILE_NAME)
        scoreHtml = f.read()
        f.close()
        score = StudentScore.StudentScore(scoreHtml)
#         print len(score)
        if(len(score) == 0):    #文件错误
            f = open(SCORE_FILE_NAME,'w')
            f.write(html)
            f.close()
        else:
            # score.test()
            newScore = StudentScore.StudentScore(html)
            # print len(score)
            # print len(newScore)
            list = score.compile(newScore)
            if(len(list) > 0):      #有新信息
                print '正在给'+STUDENT_PHONE+'发送成绩信息。。。'
                if STUDENT_PHONE == '':
                    print '正在发送邮件给'+STUDENT_EMAIL
                    SendScore.SendSocre(list).sendEmail(STUDENT_EMAIL)
                else:
                    print '正在发送短信给'+STUDENT_PHONE
                    SendScore.SendSocre(list).sendMessage(STUDENT_PHONE)
                f = open(SCORE_FILE_NAME,'w')
                f.write(html)
                f.close()
            else:
                print '成绩未更新。。。'
    else:
        print STUDENT_NO+'--第一次使用系统，正在初始化。。。'
        f = open(SCORE_FILE_NAME,'w')
        f.write(html)
        f.close()

if __name__ == '__main__':
    STUDENT_NO = sys.argv[1]
    STUDENT_PWD = sys.argv[2]
    if Tools.isEmail(sys.argv[3]):
        STUDENT_EMAIL = sys.argv[3]
    else:
        STUDENT_PHONE = sys.argv[3]
    SCORE_FILE_NAME = sys.path[0]+'/'+STUDENT_NO+"-score.html"  #设置存储路径
    main()