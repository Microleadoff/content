## Code

```python
def plus_grand_nombre_pair(liste):
    max_pair = None
    for nombre in liste:
        if nombre % 2 == 0:
            if max_pair is None or nombre > max_pair:
                max_pair = nombre
    return max_pair
```

## Explications

- La fonction ```plus_grand_nombre_pair``` prend en entrée une liste de nombres entiers liste.
- On initialise une variable ```max_pair``` à ```None```, qui va contenir le plus grand nombre pair de la liste.
- On itère sur tous les nombres de la liste avec une boucle ```for```.
- Pour chaque nombre, on vérifie s'il est pair en utilisant l'opérateur modulo ```%```.
- Si le nombre est pair, on vérifie s'il est plus grand que le maximum précédent (```max_pair```) avec une condition ```if```.
- Si c'est le cas, on met à jour ```max_pair``` avec le nouveau nombre.
- Enfin, on retourne ```max_pair```. Si aucun nombre pair n'a été trouvé dans la liste, ```max_pair``` aura gardé sa valeur ```None```.