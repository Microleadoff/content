## Durée approximative

30 minutes

## Prérequis

- <a href="https://microlead.fr/echelles/python" title="Prérequis en Python" target="_blank">Python niveau 5</a>

## Énoncé

### Description courte

Écrire une fonction Python qui calcule le PGCD (Plus Grand Commun Diviseur) de deux nombres entiers positifs donnés en utilisant l'algorithme d'Euclide. L'algorithme d'Euclide est défini comme suit : si "a" et "b" sont deux nombres entiers positifs, on divise "a" par "b" et on note le reste "r". Si "r" est égal à zéro, alors le PGCD de "a" et "b" est égal à "b". Sinon, le PGCD de "a" et "b" est égal au PGCD de "b" et "r".

### Exemple

Si a est égal à 24 et b est égal à 36, nous pouvons appliquer l'algorithme d'Euclide de la manière suivante :

```
24 = 1 * 36 + 12
36 = 3 * 12 + 0
```

Le reste est nul, donc le PGCD de 24 et 36 est égal à 12.

### Contraintes

- N'utilisez que les fonctionnalités de base de python (variables, boucles et conditions).