var canvas = document.getElementById('canvas'); // Récupération de l'élément caneva de notre page par son id (élément dans lequel on dessine)   
var ctx = canvas.getContext('2d', {alpha: false}); // Sélection du contexte du caneva (pour modifier ses données)
ctx.fillStyle = 'white'; // Sélecion de la couleur de remplissage (blanc)
ctx.fillRect(0, 0, canvas.width, canvas.height); // Dessin d'un rectangle de dimension largeur X hauteur commençant aux coordonnées (0;0)
ctx.font = "20px Arial"; // Sélection de la police d'écriture
var taille=canvas.width/nbValeurs; // Définition de la taille d'une bande de l'histogramme par défaut

var listeActions = []; // Initialisation du tableau qui récupère les actions à effectuer
var listeIndices = []; // Initialisation du tableau qui récupère les indices des éléments sur lesquels effectuer les actions
var listeValeurs = []; // Initialisation du tableau qui récupère les valeurs du tableau associées aux indices

var defaultColor = "red"; // Définition de la couleur des bandes par défaut
var minColor = "blue"; // Définition de la couleur des bandes lors de la sélection du minimum
var defaultTextColor = "black"; // Définition de la couleur du texte par défaut
var sortedColor = "orange"; // Définition de la couleur des bandes des éléments déjà triés
var currentPosColor = "green"; // Définition de la couleur des bandes des éléments parcourus
var timer; // Initialisation de la variable globale timer permettant de déclencher une animation à la fréquence de délai

function drawLineWithArrows(x0,y0,x1,y1,aWidth,aLength,arrowStart,arrowEnd){ // Fonction pemerttant le dessin d'une flèche 
	var dx=x1-x0;
	var dy=y1-y0;
	var angle=Math.atan2(dy,dx);
	var length=Math.sqrt(dx*dx+dy*dy);
	ctx.translate(x0,y0);
	ctx.rotate(angle);
	ctx.beginPath();
	ctx.moveTo(0,0);
	ctx.lineTo(length,0);
	if(arrowStart){
		ctx.moveTo(aLength,-aWidth);
		ctx.lineTo(0,0);
		ctx.lineTo(aLength,aWidth);
	}
	if(arrowEnd){
		ctx.moveTo(length-aLength,-aWidth);
		ctx.lineTo(length,0);
		ctx.lineTo(length-aLength,aWidth);
	}
	ctx.stroke();
	ctx.setTransform(1,0,0,1,0,0);
}
function drawLine(x0,y0,x1,y1){ //Fonction permettant le dessin d'une ligne entre deux points
	ctx.beginPath();
	ctx.moveTo(x0,y0);
	ctx.lineTo(x1, y1);
	ctx.stroke();
}

function animation(){ // Fonction déroulant l'animation du tri
	if (listeActions.length > 0) {
		if (listeActions[0] == 1){ // Si l'action de la liste est 1 : Animation de la permutation (dessin des flèches pour indiquer quels éléments vont être permutés)
			listeActions.shift(); // Retire la dernière action de la liste d'actions
			ctx.fillStyle = defaultTextColor; // Choix de la couleur de texte par défaut 
			drawLineWithArrows(listeIndices[0]*taille+taille/2,575,listeIndices[0]*taille+taille/2,550,5,5,false,true); // Dessin de la flèche sur le premier élément à permuter 
			drawLine(listeIndices[0]*taille+taille/2,575,listeIndices[1]*taille+taille/2,575); // Dessin d'une ligne entre les deux flèches
			drawLineWithArrows(listeIndices[1]*taille+taille/2,575,listeIndices[1]*taille+taille/2,550,5,5,false,true);	// Dessin de la flèche sur le deuxième élément à permuter 		
		}
		else if (listeActions[0] == 2){ // Si l'action de la liste est 2 : Animation de la permutation (animation d'échange des deux éléments permutés)
			listeActions.shift(); // Retire la dernière action de la liste d'actions 
			ctx.fillStyle = 'white'; // Choix de la couleur blanche pour nettoyer les bandes avant de dessiner
			ctx.fillRect(listeIndices[0]*taille, 0, taille , 600); // Nettoie la bande avant de dessiner
			ctx.fillRect(listeIndices[1]*taille, 0, taille , 600); // Nettoie la bande avant de dessiner
			ctx.fillRect(0, 550, 1000 , 50); // Nettoie la bande avant de dessiner			
			// Déplacement du premier élément non trié
			ctx.fillStyle = defaultColor; // Choix de la couleur par défaut des éléments non triès
			ctx.fillRect(listeIndices[1]*taille, 500, taille , -(listeValeurs[0]/borneMax)*500); // Dessin d'un rectangle bande de largeur taille avec décalage en fonction de l'indice du tableau	
			ctx.fillStyle = defaultTextColor; // Sélection de la couleur de texte par défaut
			if (nbValeurs<=30) ctx.fillText(listeValeurs[0], listeIndices[1]*taille + taille/2 - 10, 525); // Ecriture d'un texte (la valeur du tableau à l'indice i) sous la bande correspondante	
			// Déplacement du deuxième élément trié
			ctx.fillStyle = sortedColor; // Choix de la couleur des éléments triès
			ctx.fillRect(listeIndices[0]*taille, 500, taille , -(listeValeurs[1]/borneMax)*500); // Dessin d'un rectangle bande de largeur taille avec décalage en fonction de l'indice du tableau
			if (nbValeurs<=30) ctx.fillText(listeValeurs[1], listeIndices[0]*taille + taille/2 - 10, 525); // Ecriture d'un texte (la valeur du tableau à l'indice i) sous la bande correspondante	
			listeIndices.shift();listeIndices.shift(); // Retire deux valeurs de la liste des indices (les deux indices permutés)
			listeValeurs.shift();listeValeurs.shift(); // Retire deux valeurs de la liste des valeurs (les deux valeurs permutées)
		}
		else if (listeActions[0] == 3){ // Si l'action de la liste est 3 : Animation de la sélection (Colore la bande actuellement parcourue)
			listeActions.shift(); // Retire la dernière action de la liste d'actions
			ctx.fillStyle = 'white'; // Choix de la couleur blanche pour nettoyer les bandes avant de dessiner
			ctx.fillRect(listeIndices[0]*taille, 0, taille , 500); // Nettoie la bande avant de dessiner
			ctx.fillStyle = currentPosColor; // Choix de la couleur de la position parcourue
			ctx.fillRect(listeIndices[0]*taille, 500, taille , -(listeValeurs[0]/borneMax)*500); // Dessin d'un rectangle bande de largeur taille avec décalage en fonction de l'indice du tableau	
			if (nbValeurs<=30) ctx.fillText(listeValeurs[0], listeIndices[0]*taille + taille/2 - 10, 525); // Ecriture d'un texte (la valeur du tableau à l'indice i) sous la bande correspondante	
			listeIndices.shift(); // Retire la dernière valeur de la liste d'indices
			listeValeurs.shift(); // Retire la dernière valeur de la liste de valeurs
		}
		else if (listeActions[0] == 4){ // Si l'action de la liste est 4 : Animation du parcours de la prochaine valeur (Déselectionne la valeur précédente et séléctionne la suivante)
			listeActions.shift(); // Retire la dernière action de la liste d'actions
			ctx.fillStyle = 'white'; // Choix de la couleur blanche pour nettoyer les bandes avant de dessiner
			ctx.fillRect((listeIndices[1])*taille, 0, taille , 500); // Nettoie la bande avant de dessiner
			ctx.fillRect(listeIndices[0]*taille, 0, taille , 500); // Nettoie la bande avant de dessiner			
			ctx.fillStyle = defaultColor; // Choix de la couleur par défaut des éléments non triès
			ctx.fillRect((listeIndices[1])*taille, 500, taille , -(listeValeurs[1]/borneMax)*500); // Dessin d'un rectangle bande de largeur taille avec décalage en fonction de l'indice du tableau	
			ctx.fillStyle = defaultTextColor; // Sélection de la couleur de remplissage (noir)
			if (nbValeurs<=30) ctx.fillText(listeValeurs[1], listeIndices[1]*taille + taille/2 - 10, 525); // Ecriture d'un texte (la valeur du tableau à l'indice i) sous la bande correspondante					
			ctx.fillStyle = currentPosColor; // Choix de la couleur de l'élément parcouru
			ctx.fillRect(listeIndices[0]*taille, 500, taille , -(listeValeurs[0]/borneMax)*500); // Dessin d'un rectangle bande de largeur taille avec décalage en fonction de l'indice du tableau	
			if (nbValeurs<=30) ctx.fillText(listeValeurs[0], listeIndices[0]*taille + taille/2 - 10, 525); // Ecriture d'un texte (la valeur du tableau à l'indice i) sous la bande correspondante
			listeIndices.shift();listeIndices.shift(); // Retire deux valeurs de la liste des indices (les deux indices permutés)
			listeValeurs.shift();listeValeurs.shift(); // Retire deux valeurs de la liste des valeurs (les deux valeurs permutées)	
		}
		else if (listeActions[0] == 5){ // Si l'action de la liste est 5 : Animation du changement de statut d'une valeur à triée (changement de couleur)
			listeActions.shift(); // Retire la dernière action de la liste d'actions
			ctx.fillStyle = 'white'; // Choix de la couleur blanche pour nettoyer les bandes avant de dessiner
			ctx.fillRect(listeIndices[0]*taille, 0, taille , 500); // Nettoie la bande avant de dessiner
			ctx.fillStyle = sortedColor; // Choix de la couleur de l'élément trié
			ctx.fillRect(listeIndices[0]*taille, 500, taille , -(listeValeurs[0]/borneMax)*500); // Dessin d'un rectangle bande de largeur taille avec décalage en fonction de l'indice du tableau	
			if (nbValeurs<=30) ctx.fillText(listeValeurs[0], listeIndices[0]*taille + taille/2 - 10, 525); // Ecriture d'un texte (la valeur du tableau à l'indice i) sous la bande correspondante	
			listeIndices.shift(); // Retire la dernière valeur de la liste d'indices
			listeValeurs.shift(); // Retire la dernière valeur de la liste de valeurs
		}
		else if (listeActions[0] == 6){ // Si l'action de la liste est 6 : Animation du changement de statut d'une valeur minimum (changement de couleur)
			listeActions.shift(); // Retire la dernière action de la liste d'actions
			ctx.fillStyle = 'white'; // Choix de la couleur blanche pour nettoyer les bandes avant de dessiner
			ctx.fillRect(listeIndices[0]*taille, 0, taille , 500); // Nettoie la bande avant de dessiner
			ctx.fillRect(listeIndices[1]*taille, 0, taille , 500); // Nettoie la bande avant de dessiner		
			ctx.fillStyle = defaultColor; // Choix de la couleur par défaut des éléments non triès
			ctx.fillRect(listeIndices[0]*taille, 500, taille , -(listeValeurs[0]/borneMax)*500); // Dessin d'un rectangle bande de largeur taille avec décalage en fonction de l'indice du tableau	
			ctx.fillStyle = defaultTextColor; // Choix de la couleur par défaut de texte par défaut
			if (nbValeurs<=30) ctx.fillText(listeValeurs[0], listeIndices[0]*taille + taille/2 - 10, 525); // Ecriture d'un texte (la valeur du tableau à l'indice i) sous la bande correspondante
			ctx.fillStyle = minColor; // Choix de la couleur par défaut de valeur minimum
			ctx.fillRect(listeIndices[1]*taille, 500, taille , -(listeValeurs[1]/borneMax)*500); // Dessin d'un rectangle bande de largeur taille avec décalage en fonction de l'indice du tableau	
			if (nbValeurs<=30) ctx.fillText(listeValeurs[1], listeIndices[1]*taille + taille/2 - 10, 525); // Ecriture d'un texte (la valeur du tableau à l'indice i) sous la bande correspondante					
			listeIndices.shift();listeIndices.shift(); // Retire deux valeurs de la liste des indices (les deux indices permutés)
			listeValeurs.shift();listeValeurs.shift(); // Retire deux valeurs de la liste des valeurs (les deux valeurs permutées)					
		}
		else if (listeActions[0] == 7){ // Si l'action de la liste est 6 : Animation d'insertion (echange de valeur entre la précédente et la suivante)
			listeActions.shift(); // Retire la dernière action de la liste d'actions
			ctx.fillStyle = 'white'; // Choix de la couleur blanche pour nettoyer les bandes avant de dessiner
			ctx.fillRect(listeIndices[0]*taille, 0, taille , 600); // Nettoie la bande avant de dessiner
			ctx.fillRect(listeIndices[1]*taille, 0, taille , 600); // Nettoie la bande avant de dessiner
			ctx.fillRect(0, 550, 1000 , 50); // Nettoie la bande avant de dessiner			
			ctx.fillStyle = currentPosColor;  // Choix de la couleur de l'élément parcouru
			ctx.fillRect(listeIndices[1]*taille, 500, taille , -(listeValeurs[0]/borneMax)*500); // Dessin d'un rectangle bande de largeur taille avec décalage en fonction de l'indice du tableau	
			if (nbValeurs<=30) ctx.fillText(listeValeurs[0], listeIndices[1]*taille + taille/2 - 10, 525); // Ecriture d'un texte (la valeur du tableau à l'indice i) sous la bande correspondante	
			ctx.fillStyle = sortedColor; // Choix de la couleur de l'élément trié
			ctx.fillRect(listeIndices[0]*taille, 500, taille , -(listeValeurs[1]/borneMax)*500); // Dessin d'un rectangle bande de largeur taille avec décalage en fonction de l'indice du tableau
			if (nbValeurs<=30) ctx.fillText(listeValeurs[1], listeIndices[0]*taille + taille/2 - 10, 525); // Ecriture d'un texte (la valeur du tableau à l'indice i) sous la bande correspondante	
			listeIndices.shift();listeIndices.shift(); // Retire deux valeurs de la liste des indices (les deux indices permutés)
			listeValeurs.shift();listeValeurs.shift(); // Retire deux valeurs de la liste des valeurs (les deux valeurs permutées)				
		}
	}
	else{
		clearInterval(timer); // S'il n'y a plus d'action on arrête l'animation
	}
}

function animationPermutation(tableau,i,j){ // Ajout des éléments d'action pour l'animation de permutation
	listeActions.push(1);
	listeActions.push(2);
	listeIndices.push(i);
	listeIndices.push(j);
	listeValeurs.push(tableau[i]);
	listeValeurs.push(tableau[j]);
}

function animationSelect(tableau,i){ // Ajout des éléments d'action pour l'animation de sélection
	listeActions.push(3);
	listeIndices.push(i);
	listeValeurs.push(tableau[i]);
}

function animationParcours(tableau,i){ // Ajout des éléments d'action pour l'animation de parcours
	listeActions.push(4);
	listeIndices.push(i);
	listeValeurs.push(tableau[i]);
	listeIndices.push(i-1);
	listeValeurs.push(tableau[i-1]);
}

function animationTriee(tableau,i){ // Ajout des éléments d'action pour l'animation d'élément trié
	listeActions.push(5);
	listeIndices.push(i);
	listeValeurs.push(tableau[i]);
}

function animationMin(tableau,i,j){ // Ajout des éléments d'action pour l'animation de sélection du minimum
	listeActions.push(6);
	listeIndices.push(i);
	listeValeurs.push(tableau[i]);
	listeIndices.push(j);
	listeValeurs.push(tableau[j]);
}

function animationInsert(tableau,i){ // Ajout des éléments d'action pour l'animation d'insertion
	listeActions.push(1);
	listeActions.push(7);
	listeIndices.push(i);
	listeValeurs.push(tableau[i]);
	listeIndices.push(i-1);
	listeValeurs.push(tableau[i-1]);
}

function dessinerHistogramme(tableau){ // Fonction de dessin de l'histogramme d'un tableau
	ctx.fillStyle = 'white'; // Sélecion de la couleur de remplissage (blanc)
	ctx.fillRect(0, 0, 1000, 600); // Dessin d'un rectangle de dimension 1000x600 commençant aux coordonnées (0;0)

	for (let i = 0; i < tableau.length; i++) { // Parcours du tableau
		ctx.fillStyle = defaultColor; // Définition de la couleur de remplissage par défaut
		ctx.fillRect(i*taille, 500, taille , -(tableau[i]/borneMax)*500); // Dessin d'un rectangle bande de largeur taille avec décalage en fonction de l'indice du tableau
		if (nbValeurs<=30){ // Si le nombre de valeurs est inférieur à 30 on affiche en plus sa valeur
			ctx.fillStyle = defaultTextColor; // Sélection de la couleur de remplissage (noir)
			ctx.fillText(tableau[i], i*taille + taille/2 - 10, 525); // Ecriture d'un texte (la valeur du tableau à l'indice i) sous la bande correspondante
		}
	}			
}

function resetAnimation(){ // Réinitialisation de l'animation
	clearInterval(timer); // Arrêt de l'animation
	listeActions = []; // Vidage des listes
	listeIndices = []; // Vidage des listes
	listeValeurs = []; // Vidage des listes
	let int_delai=parseInt(document.getElementById('delai').value); // Récupération du nouveau délai
	if (Number.isInteger(int_delai)) delai=int_delai; //Si la valeur du champs nbValeurs est un entier : stocker dans la variable borneMax
	defaultColor = document.getElementById('colorDefault').value; // Récupération de la nouvelle couleur par défaut
	minColor = document.getElementById('colorSelect').value; // Récupération de la nouvelle couleur de sélection
	sortedColor = document.getElementById('colorSorted').value; // Récupération de la nouvelle couleur de tri
	currentPosColor = document.getElementById('colorParcours').value; // Récupération de la nouvelle couleur de parcours	 
}
