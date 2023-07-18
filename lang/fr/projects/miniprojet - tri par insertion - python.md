## Énoncé

### Description courte

Écrire une fonction Python tri_insertion(liste) qui prend en entrée une liste de nombres et qui trie les éléments de la liste par ordre croissant en utilisant l'algorithme de tri par insertion.

### Exemple

```
Copy code
>>> liste = [9, 4, 6, 2, 8, 1, 7, 3, 5]
>>> tri_insertion(liste)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Dans cet exemple, la fonction tri_insertion(liste) prend en entrée la liste [9, 4, 6, 2, 8, 1, 7, 3, 5] et retourne la liste triée [1, 2, 3, 4, 5, 6, 7, 8, 9] en utilisant l'algorithme de tri par insertion.

### Principe du tri à bulle

Le tri par insertion consiste à trier une liste en insérant chaque élément dans sa position correcte dans la liste triée précédente. Pour trier une liste de n éléments, il faut n-1 itérations pour trier complètement la liste.

- Pour chaque élément de la liste à trier, on le compare avec les éléments de la liste triée précédemment à partir de la fin de la liste triée.
- Si l'élément est plus petit que l'élément de la liste triée, on le déplace vers la droite pour faire de la place pour l'élément plus petit.
- On répète cette opération jusqu'à ce que l'élément soit inséré à la bonne position dans la liste triée.


### Contraintes

Vous devez implémenter l'algorithme de tri par insertion en utilisant une boucle "for" et une boucle "while".
- Vous ne devez pas utiliser la fonction sort() de Python.
- La fonction doit retourner la liste triée.