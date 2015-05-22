#coding=utf-8
'''
    @author: KEBE
'''
import smtplib  
from email.mime.text import MIMEText  
mailto_list=['kebe0412@hotmail.com'] 
mail_host="smtp.mxhichina.com"  #设置服务器
mail_user="cqutscore@kebe7jun.com"    #用户名
mail_pass="testpassword_1"   #口令 ,没事，只能在我服务器上登陆，放心的看吧。
mail_postfix="kebe7jun.com‍"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  
    me="hello"+"<"+mail_user+">"  
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')  
    msg['Subject'] = sub  
    msg['From'] = me
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False