var button1 = document.getElementById('btn-1');
var button2 = document.getElementById('btn-2');
var Carte = document.getElementById('map');

button1.addEventListener("click",generercarte1);

button2.addEventListener("click",generercarte2);

function generercarte1(){
	Carte.setAttribute('src','centre_commerciaux.html');
}

function generercarte2(){
	Carte.setAttribute('src','supermarkets.html');
}
