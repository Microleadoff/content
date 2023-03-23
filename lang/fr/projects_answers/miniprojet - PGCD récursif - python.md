## Code

```python
def pgcd(a, b):
    """
    Calcule le PGCD de deux nombres entiers positifs a et b en utilisant l'algorithme d'Euclide.
    """
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)
```

## Explications

- La fonction ```pgcd(a, b)``` prend en entrée deux nombres entiers positifs ```a``` et ```b```.
- Si ```b``` est égal à zéro, alors le PGCD de ```a``` et ```b``` est égal à ```a```, donc la fonction retourne ```a```.
- Sinon, la fonction calcule le reste ```r``` de la division euclidienne de ```a``` par ```b```.
- Ensuite, la fonction appelle récursivement la fonction ```pgcd(b, r)``` pour calculer le PGCD de ```b``` et ```r```.
- La fonction retourne finalement le PGCD calculé.