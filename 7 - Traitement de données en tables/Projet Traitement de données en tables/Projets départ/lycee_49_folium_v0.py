# affichage HTML de l'emplacement des lycées sur Angers

from folium import Map, Marker, Icon
from csv import reader
from webbrowser import open as web_open
import os


def fabricationCarte(fichier):
    liste_ecole = []
    carte_lpu = Map(location=[47.471646, -0.551846], zoom_start=13)  # carte centrée sur le centre d'Angers
    carte_lpr = Map(location=[47.471646, -0.551846], zoom_start=13)  # carte centrée sur le centre d'Angers
    with open(fichier, 'r', encoding='utf-8') as file:
        csv_read = reader(file, delimiter=";")
        for ligne in csv_read:
            if ligne[3] == 'Angers' and "LYCEE" in ligne[0]:
                liste_ecole.append(ligne)
    for ligne in liste_ecole:
        if ligne[2] == "Public":
            Marker([float(ligne[4]), float(ligne[5])], popup=f"<b>Lycée {ligne[1]}</b>"
                                                             f"<p>{ligne[2]}</p>"
                                                             f"<p>{ligne[6]}</p>"
                                                             f"<p>{ligne[3]}</p>",
                   icon=Icon(color="green")).add_to(carte_lpu)
        elif ligne[2] == "Privé":
            Marker([float(ligne[4]), float(ligne[5])], icon=Icon(color="red")).add_to(carte_lpr)
    carte_lpu.save('lycees_public.html')
    carte_lpr.save('lycees_prive.html')


fabricationCarte("France-scolaire.csv")


def page_html(fichier):
    with open(fichier, 'w', encoding='utf-8') as file:
        file.write(f"""
        <!DOCTYPE html>
        <head>
            <title>Lycée angevins</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <html>
            <body>
                <h1>ANGERS : lycées</h1>
                <p>Carte :</p>
                <iframe src="lycees_public.html" height="700" width="1000"></iframe>
                <iframe src="lycees_prive.html" height="700" width="1000"></iframe>
                <button class="button_style" type="button"></button>
            </body>
        </html>
        """)


page_html('lycee_0.html')
web_open(os.getcwd()+"/lycee_0.html")
