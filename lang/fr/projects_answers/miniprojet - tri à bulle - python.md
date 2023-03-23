## Code

```python
def tri_a_bulle(liste):
    """
    Trie une liste de nombres par ordre croissant en utilisant l'algorithme de tri à bulle.
    """
    n = len(liste)
    for i in range(n):
        for j in range(n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste
```

## Explications

- La fonction ```tri_a_bulle(liste)``` prend en entrée une liste de nombres liste.
- La variable ```n``` est initialisée à la longueur de la liste.
- La première boucle ```for``` parcourt la liste ```n``` fois, où ```n``` est la longueur de la liste.
- La deuxième boucle for parcourt la liste en comparant chaque élément avec son successeur et en échangeant leur position si nécessaire.
- Si l'élément ```liste[j]``` est plus grand que l'élément ```liste[j+1]```, on échange leur position à l'aide d'une instruction d'affectation simultanée : ```liste[j]```, ```liste[j+1] = liste[j+1]```, ```liste[j]```.
- On continue ainsi de suite jusqu'à ce que la liste soit triée.
- La fonction retourne la liste triée.