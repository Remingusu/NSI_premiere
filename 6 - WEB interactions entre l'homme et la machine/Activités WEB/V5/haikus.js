// G�n�ration d'un ha�ku

var tableau1=["fishing boats","ash wednesday","snowy morn","shortest day","haze","low sun","advent","tarn","snowflakes","Crystal Night","rain","winter stars","hungry","rain","sharia","the sound of geese","autumn sun","fly fishing","december","end of path","morning frost","evening walk","dachau","Deep autumn","visiting the graves","over the hedge","a bubble","rain","my hand","three petals fall","instant message","Out of the well","nude beach","garden wedding","rainy New York","drunk on the beach","faintly purple","the last light of day","wisteria ","through lace ","rain","winter beach","winter","long illness","lunch al fresco","the attention","remembering a song","father's pills","end of summer","waking up","long night","train window","old love letter","his scent gone","overnight snow","forest trail","learning to eat","winter night ","thumbing through","dandelion field","trailing behind","summer break","summer's end","early morning dew","spring fever","tourist season","unknotting","glowing embers","office window","beach stroll","all day rain","late night stroll","dusting off","autumn rain","mountain cave","after its first flight","winter roses","storm","candle snuffer","the patter and hiss ","lull","afternoon malaise","first day of school","downpour","dusk","airport window","midnight moon","in the no-name vine","fresh snow","night shift","freeze warning","freeze warning","freeze warning","freeze warning","freeze warning","dust","porn shop","scrabble dictionary","rusting nail","labor day","that fart"];
var tableau2=["colors of","trying to remember","pouring another cup","flames dance","half the horse hidden","the lady in red","the passing stranger","a bubble in","new asphalt","gusts of rain","the sound of a horse galloping","suddenly a whiff","half of the moon","another leaf","the sound of one hand","drowned by the sound of the train","my shadow over","the sound of the wind","a long shadow","snowflakes melting","she leaves","smell of tar between","a blue sky above","The apple colder","stronger the October wind","a dragonfly","bursts on surface","the white lilac","on her hip","from the purple coneflower","moon reveals more","By the bucket","a stranger covers me","under the cherry blossoms","from the tenth storey window","the moon in my sake cup","against the moon","purple rhododendrons","blooming before","the tracery of frost","falls from the trees","three grey lines","white peonies","pink dogwood blooming","leaving out a chair","his dog gets","from my childhood","the palette of","our memories","with freckles & curls","on my window-a spider","the fingerprints","the crinkled edges","from every room","his side of the bed","running to the end","around bruises","extending my word ","an old rolodex","my voice dissipates","the other hikers","the sun scatters","in a jar of shells","squeezing the last drop","tree roots cracking","the zen garden","the phone cord","I start my story","comings and goings","dipping our feet","lowering the blinds","through parted curtains","the piano keys","puddles fill up","from out of darkness","the young gerfalcon's talons","I am tired of reading","the monologue","our eyes adjust","of gentle raining","reading into the braille","slant light","the house fills with the space","the dead animal smell","the last whistle of something","the cloud of my breath","afraid","bluebirds","the new neighbors","a quick break","light from the arc welder","the need to pee","just enough change","from the end of the bar","a couple of homeless guys","distant thunder","each cock","lighting one candle","the coffinmaker","i dust of","prayer fans"];
var tableau3=["the rainbow","my dream","of black coffee","in the oven","behind the house","on high heels","farts","the ice","in the holes","outside","through leaves","of perfume","hidden","down","clapping","this morning","tombstones","in the reel","joins another","on the pond","first","pines","the chimneys","In the tree","at my grandparents","east","full moon","low","full moon","almost summer","of herself each night","I hunt A moon","with his shadow","the bride's blush deepens","black umbrellas bloom","disappears","pines in the light","dissolve in the dark","the end of rain","on glass","on the blue iris","of sand, sea and sky","in falling snow","without me","for the sun","homeless man","plum blossoms","autumn leaves","in zip files","summer break","climbing the moon","from past journeys","of poppy petals","winter jasmine","untouched","of my thoughts","winter apples","on scrabble","winter light","in the wind","taste of dust","my freckles","the smell of salt air","from my teabag","the concrete","fills up with noise","mother's day","from the end","of butterflies","in the stars","in her dollhouse","lives of others","autumn wind","with moonlight","the morning light","tighter on my glove","between the lines","of every tree","to the smoke wisp","cloudlight ","of your goose bumps","at the oranges bowl","between second hand ticks","shifts toward memory","as I turn on a reading light","as your plane reaches the clouds","to turn another page","at the red berries","with all the porch lights on","to look at the stars","brightens the night","once we hit traffic","for coffee","she looks back","feeding seagulls","moves on","stares at her","from another","talks of price","my resume","all sermon long"];

function newFirstLine(){
	let aleaDec=Math.random(); // Cr�ation d'un nombre al�atoire d�cimal (entre 0 et 1)
	let aleaInt=Math.floor(aleaDec*100);	
	firstLine.innerHTML=tableau1[aleaInt];
}
function newSecondLine(){
	let aleaDec=Math.random(); // Cr�ation d'un nombre al�atoire d�cimal (entre 0 et 1)
	let aleaInt=Math.floor(aleaDec*100);
	secondLine.innerHTML=tableau2[aleaInt];
}
function newThirdLine(){
	let aleaDec=Math.random(); // Cr�ation d'un nombre al�atoire d�cimal (entre 0 et 1)
	let aleaInt=Math.floor(aleaDec*100);
	thirdLine.innerHTML=tableau3[aleaInt];
}

function genererHaiku(){
	newFirstLine();
	newSecondLine();
	newThirdLine();
}

function enterFirstLineStyle() {firstLine.classList.replace("haiku", "haikuOver");}
function enterSecondLineStyle() {secondLine.classList.replace("haiku", "haikuOver");}
function enterThirdLineStyle() {thirdLine.classList.replace("haiku", "haikuOver");}

function leaveFirstLineStyle () {firstLine.classList.replace("haikuOver", "haiku");}
function leaveSecondLineStyle () {secondLine.classList.replace("haikuOver", "haiku");}
function leaveThirdLineStyle () {thirdLine.classList.replace("haikuOver", "haiku");}

genererHaiku()

var bouton_first_line = document.getElementById("firstLine");
var bouton_second_line = document.getElementById("secondLine");
var bouton_third_line = document.getElementById("thirdLine");
var bouton = document.getElementById("boutonSuivant");

bouton_first_line.addEventListener("click", newFirstLine);
bouton_first_line.addEventListener("mouseenter", enterFirstLineStyle);
bouton_first_line.addEventListener("mouseleave", leaveFirstLineStyle);

bouton_second_line.addEventListener("click", newSecondLine);
bouton_second_line.addEventListener("mouseenter", enterSecondLineStyle);
bouton_second_line.addEventListener("mouseleave", leaveSecondLineStyle);

bouton_third_line.addEventListener("click", newThirdLine);
bouton_third_line.addEventListener("mouseenter", enterThirdLineStyle);
bouton_third_line.addEventListener("mouseleave", leaveThirdLineStyle);

bouton.addEventListener("click", genererHaiku)