## Code

```python
def deuxieme_plus_grand_nombre(liste):
    if len(liste) < 2:
        return None
    max_nombre = max(liste[0], liste[1])
    deuxieme_max_nombre = min(liste[0], liste[1])
    for i in range(2, len(liste)):
        if liste[i] > max_nombre:
            deuxieme_max_nombre = max_nombre
            max_nombre = liste[i]
        elif liste[i] > deuxieme_max_nombre:
            deuxieme_max_nombre = liste[i]
    return deuxieme_max_nombre
```

## Explications

- La fonction ```deuxieme_plus_grand_nombre``` prend en entrée une liste de nombres entiers liste.
- On vérifie d'abord si la liste contient moins de deux éléments avec la condition ```if len(liste) < 2:```. Si c'est le cas, la fonction retourne ```None```.
- On initialise deux variables ```max_nombre``` et ```deuxieme_max_nombre``` avec les deux premiers éléments de la liste.
- On itère ensuite sur tous les éléments de la liste à partir de l'indice 2 avec une boucle ```for```.
- Pour chaque élément, on compare sa valeur avec les variables ```max_nombre``` et ```deuxieme_max_nombre```.
- Si l'élément est plus grand que ```max_nombre```, on met à jour ```deuxieme_max_nombre``` avec l'ancienne valeur de ```max_nombre```, et ```max_nombre``` avec la nouvelle valeur de l'élément.
- Sinon, si l'élément est plus grand que ```deuxieme_max_nombre``` mais plus petit que ```max_nombre```, on met à jour uniquement ```deuxieme_max_nombre``` avec la valeur de l'élément.
- Enfin, on retourne ```deuxieme_max_nombre```.