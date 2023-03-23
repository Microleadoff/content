## Durée approximative

30 minutes

## Prérequis

- <a href="https://microlead.fr/echelles/python" title="Prérequis en Python" target="_blank">Python niveau 5</a>

## Énoncé

### Description courte

Écrire une fonction Python tri_fusion(liste) qui prend en entrée une liste de nombres et qui trie les éléments de la liste par ordre croissant en utilisant l'algorithme de tri fusion.

### Exemple

```
>>> liste = [9, 4, 6, 2, 8, 1, 7, 3, 5]
>>> tri_fusion(liste)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Dans cet exemple, la fonction tri_fusion(liste) prend en entrée la liste [9, 4, 6, 2, 8, 1, 7, 3, 5] et retourne la liste triée [1, 2, 3, 4, 5, 6, 7, 8, 9] en utilisant l'algorithme de tri fusion.

### Principe du tri fusion

Le tri fusion consiste à diviser une liste en deux sous-listes de taille à peu près égale, à trier ces deux sous-listes de manière récursive, puis à fusionner les deux sous-listes triées pour obtenir la liste triée finale. L'algorithme de tri fusion utilise une approche "diviser pour mieux régner" pour trier une liste.

- On divise récursivement la liste en deux sous-listes de taille à peu près égale jusqu'à ce que chaque sous-liste contienne un seul élément (cas de base de la récursion).
- On fusionne ensuite les deux sous-listes triées en une seule liste triée. Pour cela, on compare les éléments de la première sous-liste avec les éléments de la deuxième sous-liste, en prenant à chaque fois le plus petit des deux éléments. On ajoute le plus petit élément dans la liste triée et on passe à l'élément suivant de la sous-liste correspondante. On continue ainsi jusqu'à ce que les deux sous-listes soient entièrement parcourues.


### Contraintes

- Vous devez implémenter l'algorithme de tri fusion en utilisant une fonction récursive.
- Vous ne devez pas utiliser la fonction sort() de Python.
- La fonction doit retourner la liste triée.