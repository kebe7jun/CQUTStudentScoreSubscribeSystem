#coding=utf-8
'''
Created on 2015.5.19

@author: 刘齐均

'''
import urllib2
import urllib
import cookielib
import re

class LoginCQUTCookie:
    #一些变量
    loginPageUrl = 'http://i.cqut.edu.cn/zfca/login?service=http%3A%2F%2Fi.cqut.edu.cn%2Fportal.do'
    loginUrl = 'http://i.cqut.edu.cn/zfca/login?service=http%3A%2F%2Fi.cqut.edu.cn%2Fportal.do'
    def __init__(self, username, password):
        self.username = username
        self.password = password
    '''
    @return: cookie
    
    '''
    def login(self):
        saveCookie = cookielib.MozillaCookieJar()#使用Cookie
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(saveCookie))
        #开始获取请求地址
        rep = opener.open(self.loginPageUrl)
        html = rep.read()
        lt = re.findall(r'lt" value="(.*)"', html)  #提取lt的value
        postdata = urllib.urlencode({
                                    'useValidateCode':'0',
                                    'isremenberme':'0',
                                    'ip':'',
                                    'username':self.username,
                                    'password':self.password,
                                    'losetime':'30',
                                    'lt':lt[0],
                                    '_eventId':'submit',
                                    'submit1':''
                                     })
        rep = opener.open(self.loginUrl,postdata)    #模拟登陆
        return opener