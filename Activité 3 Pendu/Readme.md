# Activité 3 Jeu du Pendu avec Flask

## POO <=> Programmation Orientée Objet

### Classe <=> Création d'un type

Les classes sont composée de :

#### Attributs <=> propriétés de la classe = VARIABLES

#### Méthodes <=> actions de la classe = FONCTIONS
=> Une méthode est forcément une fonction pas l'inverse.

Exemple : Imaginons une classe voiture

- **Attributs** -> Couleur (string = chaîne de caractères), poids (int = entier ou float = nb décimale ), liste, dictionnaire, booléen

- **Methodes** -> allumer_phares(), rouler(), freiner()

- Classe -> le schéma, dessin de la voiture
- Instance -> Une variable qui est de classe voiture

On crée une variable Voiture1 de classe voiture

* voiture1.vitesse     -> attribut 
* voiture1.accelerer() -> méthode

```
class voiture:
    vitesse = 25 

    def accelerer():
        vitesse += 10
```

#### Vocabulaire

- Classe
- Instance
- Attributs
- Méthodes
