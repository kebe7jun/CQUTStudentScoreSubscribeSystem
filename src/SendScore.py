#coding=utf-8
'''

@author: KEBE
'''
import urllib2
import urllib
import cookielib

import SendEmail


class SendSocre:
    messageUrl = 'http://yunpian.com/v1/sms/send.json'
    def __init__(self, list):
        self.datalist = list
    def sendMessage(self, phone):
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
        for item in self.datalist:
            content = '【KEBE7JUN成绩提醒】欢迎使用KEBE7JUN成绩订阅系统，您的'+item['name'].replace('【','[').replace('】',']')+'成绩出来啦，成绩为'+item['score']+'！有'+item['credit']+'个学分哦~'
            postdata = urllib.urlencode({
                                          'apikey':'74710a2e3c9a3402d0f7ac6d9e845d2e',
                                          'mobile':phone,
                                          'text':content
                                                    })
            print content
            rep = opener.open(self.messageUrl, postdata)
            print rep.read()
            # time.sleep(60)
    def sendEmail(self, email):
        toMailList = []
        toMailList.append(email)
        for item in self.datalist:
            content = '【KEBE7JUN成绩提醒】欢迎使用KEBE7JdUN成绩订阅系统，您的'+item['name'].replace('【','[').replace('】',']')+'成绩出来啦，成绩为'+item['score']+'！有'+item['credit']+'个学分哦~'
            SendEmail.send_mail(toMailList, '出新成绩啦！', content)
