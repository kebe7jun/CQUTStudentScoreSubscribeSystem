#coding=utf-8
'''
Created on 2015.5.22
@author: KEBE
'''
import re
class StudentScore:
    def __init__(self, html):
        self.scoreList = []
        scoreRe = re.findall(r'<td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td></td>', html)
        scoreRe.sort(key=lambda x:(x[2],x[0],x[1]))     #按照课程号、学期进行排序
        for item in scoreRe:
            scoreObject = {
                           'year':item[0],
                           'semester':item[1],
                           'cno':item[2],
                           'name':item[3],
                           'credit':item[6],
                           'score':item[8]
                           }
            self.scoreList.append(scoreObject)
    def compile(self, newScore):
        addedList = []
        if(len(self) >= len(newScore)):
            return addedList
        newList = newScore.getData()
        for i in range(len(self)):
            if(newList[i]['cno'] != self.scoreList[i]['cno']):
                addedList.append(newList[i])
                del newList[i]
                i-=1
        return addedList
    def __str__(self):
        for item in self.scoreList:
            print item
    def __len__(self):      #返回长度
        return len(self.scoreList)
    def getData(self):      #返回数据
        return self.scoreList
    def test(self):     #测试时用的函数
        del self.scoreList[len(self.scoreList)-2]
                
                