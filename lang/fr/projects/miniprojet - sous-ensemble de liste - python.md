## Durée approximative

30 minutes

## Prérequis

- <a href="https://microlead.fr/echelles/python" title="Prérequis en Python" target="_blank">Python niveau 5</a>

## Énoncé

### Description courte

Écrire une fonction en Python qui prend en entrée une liste de nombres entiers et un nombre entier ```k```, et qui retourne une liste contenant tous les sous-ensembles de la liste initiale ayant une somme égale à ```k```.

Exemple d'utilisation :

```
>>> ma_liste = [2, 3, 4, 5, 6]
>>> trouver_sous_ensembles(ma_liste, 9)
[[2, 3, 4], [5, 4], [3, 6]]
>>> ma_liste = [1, 2, 3]
>>> trouver_sous_ensembles(ma_liste, 5)
[[2, 3]]
```

### Contraintes

- N'utilisez que les fonctionnalités de base de python (variables, boucles et conditions).
- vous pouvez exceptionnellement utiliser les fonctions ```len```, ```append``` et ```sum```