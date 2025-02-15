# Import de la classe Flask du module flask
from flask import Flask, render_template, session, redirect
# On importe le module os = Operating System
import os
# On importe la liste questions du fichier questions.py
from questions import questions
# On importe la dictionnaire resultats du fichier resultats.py
from resultats import resultats 
# Création d'une instance de la classe Flask = notre app
app = Flask("Ma première App")
# On définit notre secret_key pour pouvoir créer des cookies de session
app.secret_key = os.urandom(24)



# On crée notre premier qui sera l'URL racine /, la fonction index sera appelée
# On renvoit ce que la fonction index renvoie.
@app.route("/")
def index():
    # On crée un cookie pour compter à quelle question on est
    session["nb_question"] = 0
    # On crée un cookie
    session["score"] = {"Pikachu" : 0, "Mew" : 0, "Salamèche": 0, "Carapuce": 0}
    return render_template("index.html")


# route pour la question
@app.route("/question")
def question():
    # On accède à la variable global questions
    global questions
    nb_question = session["nb_question"]
    
    # Si il reste des questions à afficher
    if nb_question < len(questions) :
        # On récupère l'énoncé de la question
        enonce = questions[nb_question]["enonce"]
        # On copie le dictionnaire qui stocke la question et les réponses possibles
        question_copy = questions[nb_question].copy()
        question_copy.pop("enonce")
        # On récupère les valeurs = les réponses
        reponses =  list(question_copy.values())
        # On récupère les clefs associées = pour les scores
        clefs =  list(question_copy.keys())
        # Cookie pour stocker l'ordre des réponses -> sert pour le score
        session["clefs"] = clefs
        # On affiche la page question avec les différentes réponses possibles
        return render_template("question.html", question = enonce, reponses = reponses)
    else :
        global resultats
        # On trie les scores de manière décroissante sous forme de liste
        score_trie = sorted(session["score"], key = session["score"].get, reverse = True)
        # On récupère la première valeur de la liste qui est le nom de celui qui a eu le plus de réponses
        nom_vainqueur = score_trie[0]
        # On récupère la description du vainqueurs
        description = resultats[nom_vainqueur]
        # On affiche les resultats en injectant nos variables stockant le nom & la description
        return render_template("resultats.html", vainqueur = nom_vainqueur, description = description)




# Route réponse pour passer à la question suivante et compter les scores
@app.route("/reponse/<numero>")
def reponse(numero):
    # On incrémente numero_question pour passer à l'utilisateur suivant
    session["nb_question"] += 1
    # On récupère le nom du personnage dont la réponse a été sélectionnée
    nom_personnage = session["clefs"][int(numero)]
    # On incrémente les scores du personnage dont la réponse a été sélectionnée
    session["score"][nom_personnage] += 1
    # On redirige vers le route question pour passer à la question suivante
    return redirect("/question")








# Execution de l'application
# host='0.0.0.0' -> le serveur Flask ecoute sur toutes les adresses IP
# port = 81 -> port d'écoute de l'app avec lequel on accède à l'application
app.run(host='0.0.0.0', port = 81)






