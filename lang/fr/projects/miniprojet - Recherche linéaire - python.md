## Énoncé

### Introduction

La recherche linéaire est une méthode simple pour trouver un élément particulier dans une liste. Elle fonctionne en parcourant chaque élément de la liste un par un jusqu'à ce qu'elle trouve l'élément recherché ou jusqu'à ce qu'elle ait parcouru tous les éléments. En python, vous pouvez implémenter cet algorithme en utilisant une boucle.

### Description courte

Votre mission est d'écrire une fonction en Python, nommée ```recherche_lineaire```, qui prend en entrée une liste d'éléments et un élément cible à rechercher dans cette liste. Votre fonction doit retourner l'index du premier occurence de cet élément dans la liste. Si l'élément n'est pas trouvé dans la liste, votre fonction doit retourner ```-1```.

### Exemple

```
>>> ma_liste = [4, 2, 9, 3, 5, 7, 8, 1]
>>> recherche_lineaire(ma_liste, 5)
4
>>> recherche_lineaire(ma_liste, 6)
-1
```

Dans le premier exemple, l'élément 5 est trouvé à l'index 4 de la liste. Dans le deuxième exemple, comme l'élément 6 n'est pas dans la liste, la fonction retourne ```-1```.

### Contraintes

Vous devez uniquement utiliser les fonctionnalités de base de python, c'est à dire les variables, les boucles et les conditions.
- Vous ne pouvez pas utiliser des fonctions prédéfinies de python comme ```index``` pour accomplir cette tâche.
- Vous pouvez utiliser la fonction ```len``` pour obtenir la longueur de la liste.