## Énoncé

### Description courte

Écrire une fonction Python tri_rapide(liste) qui prend en entrée une liste de nombres et qui trie les éléments de la liste par ordre croissant en utilisant l'algorithme de tri rapide.

### Exemple

```
>>> liste = [9, 4, 6, 2, 8, 1, 7, 3, 5]
>>> tri_rapide(liste)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Dans cet exemple, la fonction tri_rapide(liste) prend en entrée la liste [9, 4, 6, 2, 8, 1, 7, 3, 5] et retourne la liste triée [1, 2, 3, 4, 5, 6, 7, 8, 9] en utilisant l'algorithme de tri rapide.

### Principe du tri rapide

Le tri rapide consiste à choisir un élément pivot dans la liste et à diviser la liste en deux sous-listes, l'une contenant les éléments plus petits que le pivot et l'autre contenant les éléments plus grands. On trie ensuite récursivement chaque sous-liste jusqu'à ce que toutes les sous-listes soient triées. L'algorithme de tri rapide utilise une approche "diviser pour mieux régner" pour trier une liste.

- On choisit un élément pivot dans la liste.
- On divise la liste en deux sous-listes, l'une contenant les éléments plus petits que le pivot et l'autre contenant les éléments plus grands. Pour cela, on compare chaque élément de la liste avec le pivot et on place l'élément dans la sous-liste correspondante.
- On trie récursivement chaque sous-liste jusqu'à ce que toutes les sous-listes soient triées.
- On concatène les sous-listes triées pour obtenir la liste triée finale.

### Contraintes

- Vous devez implémenter l'algorithme de tri rapide en utilisant une fonction récursive.
- Vous ne devez pas utiliser la fonction sort() de Python.
- La fonction doit retourner la liste triée.