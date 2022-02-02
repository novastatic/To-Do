# Name des Programms: To-Do Liste - API Spezifikation
# Autorin: Antonia Lenz
# Erstellungsdatum: 2. Februar 2022

from flask import Flask
#import requests

# initialisiere Flask-Server
app = Flask(__name__)

# definiere Route für Hauptseite
@app.route('/')
def index():
    # gebe Antwort an aufrufenden Client zurück
    return '<h1>Hallo und willkommen auf der Hauptseite</h1><ul><li><a href="http://10.250.19.8:5000/get">GET</a></li><li><a href="http://10.250.19.8:5000/post">POST</a></li></ul>'   

# definiere Route für anzeigen aller Einträge der Liste
@app.route('/todo-list/{list_id}', methods=["GET"])
def get():
    # Inhalt der Get-Seite
    return '<h1>Hallo und willkommen auf der GETseite</h1><a href="http://10.250.19.8:5000">Hauptseite</a><br><a href="http://10.250.19.8:5000/post">POST</a><form action="#" method="get"> <p>Name: </p> <p><input type="text" name="name" id=""></p> <p><input type="submit" value="submit"></p> </form>'

# definiere Route für löschen der Liste
@app.route('/todo-list/{list_id}', methods=["DELETE"])
def delete():
    # Inhalt der Get-Seite
    return '<h1>Hallo und willkommen auf der GETseite</h1>'

# definiere Route für das Hinzufügen einer neuen Liste
@app.route('/todo-list/', methods=["POST"])
def post():
    # Inhalt der Post Seite
    return '<h1>Hallo und willkommen auf der POSTseite</h1><a href="http://10.250.19.8:5000">Hauptseite</a><br><a href="http://10.250.19.8:5000/get">GET</a><form action="#" method="post"> <p>Name: </p> <p><input type="text" name="name" id=""></p> <p><input type="submit" value="submit"></p> </form>'

# definiere Route für das Hinzufügen eines neuen Listeneintrags
@app.route('/todo-list/{list_id}/entry', methods=["POST"])
def post():
    # Inhalt der Get-Seite
    return '<h1>Hallo und willkommen auf der GETseite</h1>'

# definiere Route für das Aktualisieren eines bestehenden Eintrags
@app.route('/todo-list/{list_id}/entry/{entry_id}', methods=["PUT"])
def put():
    # Inhalt der Get-Seite
    return '<h1>Hallo und willkommen auf der GETseite</h1>'
    
# definiere Route für das Löschen eines einzelnen Eintrags
@app.route('/todo-list/{list_id}/entry/{entry_id}', methods=["DELETE"])
def delete():
    # Inhalt der Get-Seite
    return '<h1>Hallo und willkommen auf der GETseite</h1>'

# definiere Route für das Anzeigen aller Benutzer
@app.route('/user', methods=["GET"])
def get():
    # Inhalt der Get-Seite
    return '<h1>Hallo und willkommen auf der GETseite</h1>'

# definiere Route für das Hinzufügen eines Benutzers
@app.route('/user', methods=["POST"])
def post():
    # Inhalt der Get-Seite
    return '<h1>Hallo und willkommen auf der GETseite</h1>'

# definiere Route für das Löschen eines Benutzers
@app.route('/user/{user_id}', methods=["DELETE"])
def delete():
    # Inhalt der Get-Seite
    return '<h1>Hallo und willkommen auf der GETseite</h1>'

if __name__ == '__main__':

    # starte Flask-Server
    app.run(host='0.0.0.0', port=5000)