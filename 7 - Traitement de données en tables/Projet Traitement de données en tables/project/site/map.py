import folium
from os import getcwd
from webbrowser import open as open_web


def fabricationCarte(fichier):
    cc = 0
    sm = 0
    carte1 = folium.Map(location=[47.471646, -0.551846], zoom_start=13)  # carte centrée sur le centre d'Angers
    carte2 = folium.Map(location=[47.471646, -0.551846], zoom_start=14)
    with open(fichier, 'r') as file:
        for ligne in file:
            nom, departement, lat, long, type_mag = ligne.strip().split(";")
            if departement == 'Maine et Loire' and type_mag == 'Centre commercial':
                cc += 1
                folium.Marker([float(lat), 0 - float(long)], popup=nom + "- Centre commercial", icon=folium.Icon(color="blue")).add_to(carte1)
            if departement == 'Maine et Loire' and type_mag == 'Supermarché':
                sm += 1
                folium.Marker([float(lat), 0 - float(long)], popup=nom + "- Supermarché", icon=folium.Icon(color="red")).add_to(carte2)
        carte1.save('centre_commerciaux.html')
        carte2.save('supermarkets.html')
    return cc, sm


cc, sm = fabricationCarte("magasin_angers.csv")


def page_html(file, cc, sm):
    with open(file, 'w', encoding='utf-8') as html_file:
        html_file.write("""
<!DOCTYPE html>
<head>
    <link rel="stylesheet" href="style.css">
    <title>Magasins sur Angers</title>
</head>
<html>
<body>
    <header>
        <div class="title">Magasins Angevins</div>
    </header>
    <main>
        <p id="text">Nombre de Centres commerciaux: """ + str(cc) + """<br>Nombre de Supermarchés: """ + str(sm) + """</p>
        <iframe id="map" src="centre_commerciaux.html" frameborder="0" height="700" width="1000"></iframe><br>
        <button id="btn-1">Centres Commerciaux</button>
        <button id="btn-2">Supermarchés</button>
    </main>
    <script src="id.js"></script>
</body>
</html>
""")


page_html('index.html', cc, sm)
open_web(getcwd()+"/index.html")
