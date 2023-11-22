## Énoncé

### Introduction

La recherche binaire (aussi appelée dichotomique) est une méthode de recherche efficace qui fonctionne sur des listes triées. Elle fonctionne en divisant constamment la liste en deux et en vérifiant si l'élément recherché est dans la première ou la deuxième moitié de la liste. Cela permet de réduire considérablement le nombre d'éléments à vérifier par rapport à la recherche linéaire. En Python, vous pouvez implémenter cet algorithme en utilisant une boucle ou de la récursion.

### Description courte

Votre mission est d'écrire une fonction en Python, nommée ```recherche_binaire```, qui prend en entrée une liste triée d'éléments et un élément cible à rechercher dans cette liste. Votre fonction doit retourner l'index de cet élément dans la liste. Si l'élément n'est pas trouvé dans la liste, votre fonction doit retourner ```-1```.

### Exemple

```
>>> ma_liste = [1, 2, 3, 4, 5, 7, 8, 9]
>>> recherche_binaire(ma_liste, 5)
4
>>> recherche_binaire(ma_liste, 6)
-1
```

Dans le premier exemple, l'élément 5 est trouvé à l'index 4 de la liste. Dans le deuxième exemple, comme l'élément 6 n'est pas dans la liste, la fonction retourne -1.

### Contraintes

Vous devez uniquement utiliser les fonctionnalités de base de python, c'est à dire les variables, les boucles et les conditions.
- Vous ne pouvez pas utiliser des fonctions prédéfinies de python comme ```index``` pour accomplir cette tâche.
- Vous pouvez utiliser la fonction ```len``` pour obtenir la longueur de la liste.

### Astuces

Souvenez-vous que la liste doit être triée pour que la recherche binaire fonctionne !