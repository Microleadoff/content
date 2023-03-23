## Durée approximative

30 minutes

## Prérequis

- <a href="https://microlead.fr/echelles/python" title="Prérequis en Python" target="_blank">Python niveau 5</a>

## Énoncé

### Description courte

Écrire une fonction Python tri_a_bulle(liste) qui prend en entrée une liste de nombres et qui trie les éléments de la liste par ordre croissant en utilisant l'algorithme de tri à bulle.

### Exemple

```
>>> liste = [9, 4, 6, 2, 8, 1, 7, 3, 5]
>>> tri_a_bulle(liste)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Dans cet exemple, la fonction tri_a_bulle(liste) prend en entrée la liste [9, 4, 6, 2, 8, 1, 7, 3, 5] et retourne la liste triée [1, 2, 3, 4, 5, 6, 7, 8, 9] en utilisant l'algorithme de tri à bulle.

### Principe du tri à bulle

- On commence par comparer le premier élément de la liste avec le deuxième élément. Si le premier élément est plus grand que le deuxième élément, on les échange de position. Sinon, on ne fait rien.
- Ensuite, on compare le deuxième élément avec le troisième élément. Si le deuxième élément est plus grand que le troisième élément, on les échange de position. Sinon, on ne fait rien.
- On continue ainsi de suite jusqu'à la fin de la liste en comparant chaque élément avec son successeur et en échangeant leur position si nécessaire. Cela forme une passe.
- Une fois la première passe terminée, le plus grand élément est placé en dernière position. On recommence alors le processus à partir du premier élément jusqu'à l'avant-dernier élément pour faire une deuxième passe.
- On continue ainsi de suite jusqu'à ce que la liste soit triée.

### Contraintes

- Vous devez implémenter l'algorithme de tri à bulle en utilisant une boucle for imbriquée dans une autre boucle for.
- Vous ne devez pas utiliser la fonction sort() de Python.
- La fonction doit retourner la liste triée.