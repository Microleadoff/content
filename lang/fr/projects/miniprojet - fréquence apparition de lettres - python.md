## Énoncé

### Introduction

L'analyse des fréquences de caractères est une opération couramment utilisée en cryptographie et en traitement de texte. Python offre plusieurs méthodes pour effectuer cela, mais dans le cadre de cet exercice, nous allons mettre en place notre propre fonction pour calculer la fréquence des caractères.

### Description courte

Votre mission est d'écrire une fonction en Python, nommée ```frequence_caracteres```, qui prend en entrée une chaîne de caractères et retourne un dictionnaire avec chaque caractère unique de la chaîne comme clé et le nombre de fois où ce caractère apparaît dans la chaîne comme valeur.

### Exemple

```
>>> ma_chaine = "Bonjour tout le monde"
>>> frequence_caracteres(ma_chaine)
{'B': 1, 'o': 3, 'n': 2, 'j': 1, 'u': 2, 'r': 1, ' ': 3, 't': 2, 'l': 1, 'e': 2, 'm': 1, 'd': 1}
```

Dans cet exemple, la fonction retourne un dictionnaire où chaque caractère de la chaîne est représenté par une clé, et le nombre d'occurrences de ce caractère est la valeur associée à cette clé.

### Contraintes

- Vous devez uniquement utiliser les fonctionnalités de base de python, c'est à dire les variables, les boucles et les conditions.
- Vous ne pouvez pas utiliser des fonctions prédéfinies de python comme ```count``` pour accomplir cette tâche.