## Code

```python
def pgcd(a, b):
    """
    Calcule le PGCD (Plus Grand Commun Diviseur) de deux nombres entiers positifs a et b en utilisant l'algorithme d'Euclide.
    
    :param a: Le premier nombre entier positif.
    :param b: Le deuxième nombre entier positif.
    :return: Le PGCD de a et b.
    """
    # Vérification des entrées
    if a <= 0 or b <= 0:
        raise ValueError("Les deux nombres doivent être entiers positifs.")
    
    # Algorithme d'Euclide
    while b != 0:
        r = a % b
        a = b
        b = r
    
    # Retourne le PGCD
    return a
```

## Explications

La fonction pgcd prend en entrée deux nombres entiers positifs ```a``` et ```b``` et retourne leur PGCD. La fonction commence par vérifier que les entrées sont valides, c'est-à-dire que les nombres sont entiers positifs. Si ce n'est pas le cas, la fonction lève une exception ```ValueError```. Ensuite, la fonction applique l'algorithme d'Euclide en utilisant une boucle ```while```. L'algorithme consiste à diviser ```a``` par ```b``` et à calculer le reste ```r```. Si ```r``` est nul, alors le PGCD de ```a``` et ```b``` est égal à ```b```. Sinon, on remplace ```a``` par ```b``` et ```b``` par ```r```, et on répète le processus jusqu'à ce que le reste soit nul. Enfin, la fonction retourne le PGCD calculé.