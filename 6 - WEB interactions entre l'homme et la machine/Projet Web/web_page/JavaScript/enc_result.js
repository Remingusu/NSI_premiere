const queryString = window.location.search;
console.log(queryString);
const urlParams = new URLSearchParams(queryString);
var contenu = "";
contenu +=  "<div class='all_box'>" + 
                "<div class='email_result'>" +
                    "<p>" + "Un e-mail serra envoyer à l'adresse si-dessous, lorsque les encouragements seront transmis. " + "</p>" + 
                    "<I>" + urlParams.get("email") + "</I>" + 
                "</div>" +
                "<div class='driver_result'>" + 
                    "<p>" + "Vos encouragements seront transmis à " + "</p><b>" + urlParams.get("driver") + "</b>" +
                "</div>" +
                "<div class='text_result'>" +
                    "<h3>" + "Texte:" + "</h3>" + 
                    "<p style='color: " + urlParams.get("color") + ";'>" + urlParams.get("message") + "<p>" +
                "</div>" +
            "</div>"
var resultat = document.getElementById('result');
resultat.innerHTML += contenu;