## Énoncé

### Introduction

La recherche de sous-chaînes est une tâche courante en programmation. Python offre plusieurs méthodes pour effectuer cette opération, mais dans le cadre de cet exercice, nous allons mettre en place notre propre fonction de recherche de sous-chaînes pour mieux comprendre comment cela fonctionne.

### Description courte

Votre mission est d'écrire une fonction en Python, nommée ```recherche_sous_chaine```, qui prend en entrée une chaîne de caractères et une sous-chaîne à rechercher. Votre fonction doit retourner l'index de départ de la première occurrence de cette sous-chaîne dans la chaîne principale. Si la sous-chaîne n'est pas trouvée, votre fonction doit retourner ```-1```.

### Exemple

```
>>> ma_chaine = "Bonjour tout le monde"
>>> recherche_sous_chaine(ma_chaine, "tout")
8
>>> recherche_sous_chaine(ma_chaine, "salut")
-1
```

Dans le premier exemple, la sous-chaîne "tout" est trouvée à partir de l'index 8 de la chaîne principale. Dans le deuxième exemple, la sous-chaîne "salut" n'est pas présente dans la chaîne principale, donc la fonction retourne -1.

### Contraintes

- Vous devez uniquement utiliser les fonctionnalités de base de python, c'est à dire les variables, les boucles et les conditions.
- Vous ne pouvez pas utiliser des fonctions prédéfinies de python comme ```index``` ou ```find``` pour accomplir cette tâche.
- Vous pouvez utiliser la fonction len pour obtenir la longueur des chaînes.