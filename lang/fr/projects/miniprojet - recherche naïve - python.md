## Énoncé

### Description courte

Écrire une fonction en Python qui prend en entrée une liste d'entiers et un entier à rechercher, et qui retourne l'index de l'entier dans la liste s'il est présent, ou -1 s'il n'est pas présent en utilisant l'algorithme de recherche naïve.

**Note** : La recherche naïve est un algorithme de recherche simple qui consiste à parcourir tous les éléments d'une liste pour trouver un élément donné.

Exemple d'utilisation :

```
>>> recherche_naive([4, 1, 6, 2, 7, 3, 9, 5, 8], 6)
2
>>> recherche_naive([4, 1, 6, 2, 7, 3, 9, 5, 8], 10)
-1
```

### Contraintes

- N'utilisez que les fonctionnalités de base de python (variables, boucles et conditions).
- vous pouvez exceptionnellement utiliser les fonctions ```len``` et ```range```