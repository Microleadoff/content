## Durée approximative

30 minutes

## Prérequis

- <a href="https://microlead.fr/echelles/python" title="Prérequis en Python" target="_blank">Python niveau 5</a>

## Énoncé

### Description courte

Écrire une fonction en Python qui prend en entrée une liste d'entiers et un entier à rechercher, et qui retourne l'index de l'entier dans la liste s'il est présent, ou -1 s'il n'est pas présent en utilisant l'algorithme de recherche dichotomique.

**Note** : La recherche dichotomique, également appelée recherche binaire, est un algorithme de recherche efficace pour trouver la position d'un élément dans une liste **triée**. Au lieu de parcourir la liste élément par élément, la recherche dichotomique divise la liste en deux à chaque itération et vérifie dans quelle moitié de la liste se trouve l'élément cherché.

Exemple d'utilisation :

```
>>> recherche_dichotomique([1, 2, 3, 4, 5, 6, 7, 8, 9], 6)
5
>>> recherche_dichotomique([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
-1
```

### Contraintes

- N'utilisez que les fonctionnalités de base de python (variables, boucles et conditions).
- vous pouvez exceptionnellement utiliser les fonctions ```len``` et ```range```