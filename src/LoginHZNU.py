#coding=utf-8
import urllib2
import urllib
import cookielib
import re

class LoginHZNUCookie:
    #一些变量
    loginPageUrl = 'http://jwgl1.hznu.edu.cn/'
    loginUrl = 'http://jwgl1.hznu.edu.cn/default2.aspx'
    checkCodeUrl = 'http://jwgl1.hznu.edu.cn/CheckCode.aspx'
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
        lt = re.findall(r'__VIEWSTATE" value="(.*)"', html)  #提取lt的value
        f = open("code.jpg", 'wb')
        f.write(opener.open(self.checkCodeUrl).read())
        f.close()
        code = raw_input("请输入验证码:")
        postdata = urllib.urlencode({
                                    'txtSecretCode':code,
                                    'txtUserName':self.username,
                                    'TextBox2':self.password,
                                    'Button1':'',
                                    '__VIEWSTATE':lt[0],
                                    'lbLanguage':'',
                                    'hidPdrs':'',
                                    'hidsc':''
                                     })
        # print postdata
        postdata+='&RadioButtonList1=%BD%CC%CA%A6'
        rep = opener.open(self.loginUrl,postdata)    #模拟登陆
        print rep.read().decode("GBK")
        return opener

opener = LoginHZNUCookie('xxx', 'xxx').login()
