## Énoncé

### Description courte

En réutilisant un code fourni, vous allez devoir mettre en place l'ensemble des règles du Clean Code relatif aux commentaires.

### Éléments donnés

Voici le code sur lequel vous devez travailler : 

```python
class Carte:

    def __init__(self, nom, chaine):
        self.nom = nom
        self.chaine = chaine
        self.plan = chaine.replace("X", " ")
        self.robot = ref(chaine)[0]
        self.succes = ref(chaine)[1]
        self.obstacles = ref(chaine)[2]
        self.largeur = len(chaine.split("\n")[0])
        self.hauteur = len(chaine.split("\n"))

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def grille(self, coord):
        x, y = coord
        succes = False
        grille = self.plan.split("\n")
        destination = grille[y][x]
        grille[y] = list(grille[y])
        grille[y][x] = "X"
        grille[y] = "".join(grille[y])
        grille = "\n".join(grille)
        return grille
```

### Contraintes

- Respectez les spécificités du langage python pour la réalisation de vos commentaires

### Critères de réussite

L'ensemble des commentaires sont en place et décrivent parfaitement ce à quoi ils sont rattachés. Ils permettent de simplifier la lecture du code et sa compréhension.

### Astuces

#### Astuce 1

- Vous pouvez vous aidez d'outils tels que ```flake8``` pour vérifier le respect des normes de python