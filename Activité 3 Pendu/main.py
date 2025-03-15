# On importe la classe Flask du module flask
from flask import Flask, render_template, session, redirect
# On importe os
import os
# On import random pour les choix aléatoires
import random
# On importe notre classe pendu de notre fichier pendu.py
from pendu import Pendu

# On crée une instance de Flask stocké dans la variable app
app = Flask("My Pendu App Web avec Flask")

# On définit notre clef secrète pour la création des cookies
app.secret_key = os.urandom(24)

# On définit notre premier route pour l'initialisation
@app.route('/')
def initialisation():
    # Liste de mots
    liste_mots = ["arbre", "magic", "chat", "dns", "python", "virus", "série", "clavier", "soleil", "lune"]
    # On choisit aléatoirement un mot parmi la liste
    mot_a_deviner = random.choice(liste_mots)
    # On définit le nombre de vie
    vies = 6
    # On initialise le jeu
    session["etat_du_jeu"] = Pendu.initialisation(mot_a_deviner, vies)
    return redirect("/affichage_jeu")

# On définit notre second route pour l'affiche
@app.route('/affichage_jeu')
def affichage():
    # On affiche le jeu et on injecte le cookie etat_du_jeu en tant que variable
    return render_template("jeu_pendu.html", etat_du_jeu = session["etat_du_jeu"] )




# Démarre le serveur Flask
# Host: "0.0.0.0" -> Configure Flask pour accepter des connexions provenant de toutes les adresses IP
# port = 81 : Définit le port sur lequel l'application sera accessible
app.run(host = '0.0.0.0', port = 81)