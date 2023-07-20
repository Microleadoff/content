## Énoncé

### Introduction

Le chiffrement par substitution est une méthode de chiffrement où chaque lettre d'un texte donné est remplacée par une lettre différente, avec un décalage fixe dans l'alphabet. Par exemple, avec un décalage de 1, A serait remplacé par B, B deviendrait C, et ainsi de suite.

### Description courte

Votre mission est d'écrire deux fonctions en Python, ```chiffre_substitution``` et ```dechiffre_substitution```. La fonction ```chiffre_substitution``` prend en entrée une chaîne de caractères (le texte en clair) et une clé sous forme de nombre entier (le décalage), et retourne le texte chiffré. La fonction ```dechiffre_substitution``` fait l'inverse, elle prend en entrée une chaîne de caractères (le texte chiffré) et une clé, et retourne le texte en clair.

### Exemple

```
>>> texte_clair = "HELLO"
>>> cle = 3
>>> texte_chiffre = chiffre_substitution(texte_clair, cle)
>>> print(texte_chiffre)
"KHOOR"
>>> texte_dechiffre = dechiffre_substitution(texte_chiffre, cle)
>>> print(texte_dechiffre)
"HELLO"
```

### Contraintes

- Vous devez uniquement utiliser les fonctionnalités de base de python, c'est à dire les variables, les boucles et les conditions.

### Astuces

- Notez que le chiffrement par substitution n'est pas sensible à la casse, vous pouvez donc convertir toutes les lettres en majuscules ou en minuscules pour simplifier le processus.
- Pour gérer le débordement (par exemple, pour Z avec un décalage de 1), vous pouvez utiliser le modulo de la taille de l'alphabet (26 pour l'alphabet anglais).
- voici [un lien supplémentaire pour comprendre le chiffrement par substitution](https://fr.wikipedia.org/wiki/Chiffrement_par_substitution)