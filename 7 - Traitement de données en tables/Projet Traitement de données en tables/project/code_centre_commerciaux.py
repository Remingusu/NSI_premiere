import folium
from os import getcwd
from webbrowser import open as open_web


def fabricationCarte(fichier):
    carte1 = folium.Map(location=[47.471646, -0.551846], zoom_start=13)  # carte centrée sur le centre d'Angers
    carte2 = folium.Map(location=[47.471646, -0.551846], zoom_strat=13)
    with open(fichier, 'r') as file:
        for ligne in file:
            nom, departement, lat, long, type_mag = ligne.strip().split(";")
            if departement == 'Maine et Loire' and type_mag == 'Centre commercial':
                print("hi2")
                folium.Marker([float(lat), 0 - float(long)], popup="Centre commercial", icon=folium.Icon(color="blue")).add_to(carte1)
            if departement == 'Maine et loire' and type_mag == 'Supermarche':
                print("hi3")
                folium.Marker([float(lat), 0 - float(long)], popup="Supermarché", icon=folium.Icon(color="red")).add_to(carte2)
        carte1.save('centre_commerciaux.html')
        carte2.save('supermarkets.html')


fabricationCarte("magasin_angers.csv")


def page_html(file):
    with open(file, 'w', encoding='utf-8') as html_file:
        html_file.write(f"""
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="style.css">
    <title>Magasins sur Angers</title>
</head>
<body>
    <header>
        <div class="title">Magasins Angevins</div>
    </header>
    <main>
        <iframe src="centre_commerciaux.html" height="700" width="1000"></iframe><br>
        <iframe src="supermarkets.html" height="700" width="1000"></iframe>
    </main>
    <script>
        // Script for number of markets
    </script>
</body>
</html>
""")


page_html('index.html')
open_web(getcwd()+"/index.html")
