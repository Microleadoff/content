## Énoncé

### Introduction

Le chiffrement de Vigenère est une méthode de chiffrement par substitution alphabétique polyalphabétique simple qui utilise une série de différentes substitutions de César basées sur les lettres d'un mot clé. Il a été décrit pour la première fois par Giovan Battista Bellaso en 1553, mais est souvent attribué à Blaise de Vigenère.

### Description courte

Votre mission est d'écrire deux fonctions en Python, ```chiffre_vigenere``` et ```dechiffre_vigenere```. La fonction ```chiffre_vigenere``` prend en entrée une chaîne de caractères (le texte en clair) et une clé sous forme de chaîne de caractères, et retourne le texte chiffré. La fonction ```dechiffre_vigenere``` fait l'inverse, elle prend en entrée une chaîne de caractères (le texte chiffré) et une clé, et retourne le texte en clair.

### Exemple

```
>>> texte_clair = "ATTACKATDAWN"
>>> cle = "LEMON"
>>> texte_chiffre = chiffre_vigenere(texte_clair, cle)
>>> print(texte_chiffre)
"LXFOPVEFRNHR"
>>> texte_dechiffre = dechiffre_vigenere(texte_chiffre, cle)
>>> print(texte_dechiffre)
"ATTACKATDAWN"
```

### Contraintes

- Vous devez uniquement utiliser les fonctionnalités de base de python, c'est à dire les variables, les boucles et les conditions.

### Astuces

- Notez que le chiffrement de Vigenère n'est pas sensible à la casse, vous pouvez donc convertir toutes les lettres en majuscules ou en minuscules pour simplifier le processus.
- La clé est répétée ou tronquée pour qu'elle ait la même longueur que le texte à chiffrer ou déchiffrer.
- Chaque lettre du texte est décalée vers la droite ou vers la gauche (pour le chiffrement ou le déchiffrement, respectivement) de l'alphabet de la position équivalente à la lettre de la clé (A correspond à un décalage de 0, B à un décalage de 1, etc.)
- voici [un lien supplémentaire pour comprendre le chiffrement de vigenère](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re)