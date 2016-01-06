#coding=utf-8
'''

@author: KEBE
'''
import re

test = 'kebe0412@hotmail.com'
def isEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
    return False