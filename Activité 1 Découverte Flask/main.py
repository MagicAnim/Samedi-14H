# Import de la classe Flask du module flask
from flask import Flask, render_template

# Création d'une instance de la classe Flask = notre app
app = Flask("Ma première App")




# On crée notre premier qui sera l'URL racine /, la fonction index sera appelée
# On renvoit ce que la fonction index renvoie.
@app.route("/")
def index():
    return render_template("index.html")


# route pour la seconde page
@app.route("/seconde_page")
def second_page():
    texte_erreur = "!!! WARNING2 !!!"
    return render_template("seconde_page.html", erreur = texte_erreur)




# Execution de l'application
# host='0.0.0.0' -> le serveur Flask ecoute sur toutes les adresses IP
# port = 81 -> port d'écoute de l'app avec lequel on accède à l
app.run(host='0.0.0.0', port = 81)






