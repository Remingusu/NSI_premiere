const img4 = document.getElementById('img4')

function agrandir4() {
    var img = img4;
    var width = img.clientWidth;
	var height = img.clientHeight;
    img.style.width = (width + 50) + "px";
	img.style.height = (height + 50) + "px";
    }

function diminuer4() {
    var img = img4;
    var width = img.clientWidth;
	var height = img.clientHeight;
    img.style.width = (width - 50) + "px";
	img.style.height = (height - 50) + "px";
    }