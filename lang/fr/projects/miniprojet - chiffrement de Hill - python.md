## Énoncé

### Introduction

Le chiffrement de Hill est un système de chiffrement polygraphique qui utilise l'algèbre linéaire pour chiffrer un message. Il a été inventé par Lester S. Hill en 1929. Dans le chiffrement de Hill, le texte en clair est divisé en blocs de taille fixe, qui sont ensuite transformés en vecteurs. Ces vecteurs sont multipliés par une matrice clé pour produire des vecteurs chiffrés.

### Description courte

Votre mission est d'écrire deux fonctions en Python, ```chiffre_hill``` et ```dechiffre_hill```. La fonction ```chiffre_hill``` prend en entrée une chaîne de caractères (le texte en clair) et une clé sous forme de matrice 2x2, et retourne le texte chiffré. La fonction ```dechiffre_hill``` fait l'inverse, elle prend en entrée une chaîne de caractères (le texte chiffré) et une clé, et retourne le texte en clair.

### Exemple

```
>>> texte_clair = "HELLO"
>>> cle = [[6, 24], [1, 16]]
>>> texte_chiffre = chiffre_hill(texte_clair, cle)
>>> print(texte_chiffre)
"APZQG"
>>> texte_dechiffre = dechiffre_hill(texte_chiffre, cle)
>>> print(texte_dechiffre)
"HELLO"
```

### Contraintes

- Vous devez uniquement utiliser les fonctionnalités de base de python, c'est à dire les variables, les boucles et les conditions.
- Vous aurez besoin de la bibliothèque numpy pour effectuer les opérations matricielles.

### Astuces

- Notez que le chiffrement de Hill n'est pas sensible à la casse, vous pouvez donc convertir toutes les lettres en majuscules ou en minuscules pour simplifier le processus.
- L'inversion de la matrice clé est nécessaire pour le déchiffrement. Assurez-vous que votre clé est inversible modulo 26 (la taille de l'alphabet anglais), sinon elle ne pourra pas être utilisée pour le chiffrement de Hill.
- voici [un lien supplémentaire pour comprendre le chiffrement de Hill](https://fr.wikipedia.org/wiki/Chiffre_de_Hill)