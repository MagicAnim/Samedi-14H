# Import de unidecode pour enlever les caractères spéciaux
from unidecode import unidecode

# On crée notre classe pendu pour toute la gestion du jeu
class Pendu:
    # On crée les attributs utiles pour le jeu
    vies = 0
    mot_a_deviner = ""
    mot_a_afficher = ""
    # On stocke l'ensemble des propositions de l'utilisateur dans une liste
    lettres_proposees = []

    ############################################################
    #              1ere Méthode : Initialisation               #
    ############################################################
    def initialisation(mot_a_deviner, vies):
        # On règle les soucis de caractères spéciaux
        mot_a_deviner = unidecode(mot_a_deviner).upper()
        # On crée un dictionnaire d'état du jeu pour avoir un suivi 
        data_etat_du_jeu = {
            "vies" : vies,
            "mot_a_deviner" : mot_a_deviner,
            "mot_a_afficher" : "-" * len(mot_a_deviner),
            "lettres_proposees" : [],
            "victoire" : False,
            "defaite" : False,
            "entree" : ""
        }
        return data_etat_du_jeu






