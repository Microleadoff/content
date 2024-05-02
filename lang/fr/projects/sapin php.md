## Énoncé

### Description courte

Le principe du projet est de générer un sapin de noël à partir d'un algorithme que vous devrez concevoir.

### Listing de fonctionnalités

Les fonctionnalités suivantes sont à réaliser dans l'ordre (n'essayez pas de tout faire en une seule fois si vous n'êtes pas parfaitement à l'aise avec l'algorithmique !).

1. Réaliser un algorithme qui soit capable de "dessiner" le sapin ci-dessous. Ne prenez pas en compte les "S", ni les boules de noël en dessous du sapin.
2. Créer une constante "FLOORS" au début de votre script. Celle-ci contiendra un nombre entier (Integer) ajustable, qui déterminera combien d'étages doit avoir le sapin. Votre algorithme doit maintenant dessiner autant d'étage que le nombre contenu dans cette constante.
3. Créer une constante "GARLAND" au début de votre script. Celle-ci sera de type "Boolean", et devra être définie à TRUE ou FALSE. Si la valeur est vraie, alors les "S" devront s'afficher sur votre sapin, sinon ils ne devront pas s'afficher. Votre algorithme doit être adapté pour prendre en compte ce nouveau paramètre.
4. Créer une constante "BALLS" au début de votre script. Celle-ci sera de type "Boolean", et devra être définir à TRUE ou FALSE. Si la valeur est vraie, alors les boules de noël en bas du sapin devront s'afficher, sinon elles ne s'affichent pas. Votre algorithme doit être adapté pour prendre en compte ce nouveau paramètre.
5. Créer une constante "REPLICA" au début de votre script. Celle-ci contiendra un nombre entier (Integer) ajustable, qui déterminera combien de sapins doivent être dessinés horizontalement, côte à côte (de gauche à droite). Tous les sapins ainsi dessinés doivent être positionnés sur la même ligne, quitte à faire apparaître une scrollbar sur votre navigateur.

### Éléments donnés

Voici le schéma de base du sapin, incluant toutes les options : 

![Représentation du sapin à réaliser](https://raw.githubusercontent.com/Microleadoff/content/master/lang/fr/projects/images_projets/image_dessin_sapin.png)

### Contraintes

N'utilisez que du PHP à l'exception des balises html **<pre></pre>** que vous pouvez utiliser de telle sorte à ce que les caractères d'espace soient de la même taille que les caractères d'étoile.

Ne dessinez rien directement dans votre code PHP : chaque ligne doit ENTIÈREMENT être générée algorithmiquement.

## Étapes de réalisation

1. créer une fonction qui affiche une ligne, avec un nombre d'espaces donné en paramètre, et un nombre d'étoiles donné aussi en paramètre.
2. créer une fonction qui permet de faire un étage, et qui prend en paramètre le nombre d'étoiles pour la première ligne de l'étage (attention, petite particularité pour le premier étage - à traiter ultérieurement !)
3. Faire une fonction qui permet de faire le sapin
4. Traiter les spécificités une par une.

## Astuces

- Ne faire que du procédural au début si vous galérez !
- Utilisez les fonctions "simples" pour faire les fonctions "complexes" (n'hésitez pas à appeler une fonction dans une autre)
- Toujours commencer par l'étape la plus simple !