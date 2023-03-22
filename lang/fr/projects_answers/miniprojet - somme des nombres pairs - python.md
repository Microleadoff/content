## Code

```python
def somme_nombres_pairs(liste):
    somme = 0
    for nombre in liste:
        if nombre % 2 == 0:
            somme += nombre
    return somme
```

## Explications

- La fonction ```somme_nombres_pairs``` prend en entrée une liste de nombres liste.
- On initialise une variable ```somme``` à 0 qui servira à accumuler la somme des nombres pairs.
- On parcourt ensuite tous les éléments de la liste avec une boucle ```for```.
- Pour chaque nombre, on vérifie s'il est pair en utilisant l'opérateur ```%``` qui calcule le reste de la division euclidienne par 2. Si ce reste est égal à 0, cela signifie que le nombre est pair, et on l'ajoute à la variable ```somme```.
- À la fin de la boucle, on retourne la variable somme qui contient la somme des nombres pairs de la liste.