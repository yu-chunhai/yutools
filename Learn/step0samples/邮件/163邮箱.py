# coding=utf-8
# @作者:yuLearn
#@Time:2018/2/7-18:55
#@文件名称:yu-chunhai-163邮箱
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = 't18905255025@163.com'
receiver = 't18905255025@163.com'
# 标题
subject = 'pythonemailtest20180121'
smtpserver = 'smtp.163.com'
username = 't18905255025@163.com'
password = 'yuchunhai1989'
# 附件内容
msg = MIMEText('yuchunhai','text','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()