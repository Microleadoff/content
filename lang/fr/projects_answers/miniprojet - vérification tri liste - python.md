## Code

```python
def est_triee(liste):
    if len(liste) < 2:
        return True
    for i in range(1, len(liste)):
        if liste[i] < liste[i-1]:
            return False
    return True
```

## Explications

- La fonction ```est_triee``` prend en entrée une liste de nombres entiers liste.
- On vérifie d'abord si la liste contient un seul élément ou moins avec la condition ```if len(liste) < 2:```. Si c'est le cas, la liste est considérée comme triée et la fonction retourne ```True```.
- On itère ensuite sur tous les éléments de la liste à partir de l'indice 1 avec une boucle ```for```.
- Pour chaque élément, on compare sa valeur avec celle de l'élément précédent (```liste[i-1]```).
- Si l'élément est plus petit que l'élément précédent, cela signifie que la liste n'est pas triée par ordre croissant, et on retourne ```False```.
- Si tous les éléments sont parcourus sans qu'on ait trouvé d'élément non trié, la liste est considérée comme triée et la fonction retourne ```True```.