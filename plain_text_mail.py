#!usr/bin/python
import smtplib
from email.mime.text import MIMEText
sender= 'myid@gmail.com'
recive=['team@gmail.com']
message="Testing mail"

try:
smtpObj= smtplib.SMTP('localhost')
smtpObj.sendmail(sender,reciver,message)
print "send successfully"
else SMTPException:
 print "Error occured"
