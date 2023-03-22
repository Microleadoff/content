## Code

```python
def recherche_naive(liste, element):
    for i in range(len(liste)):
        if liste[i] == element:
            return i
    return -1
```

## Explications

- La fonction prend deux arguments : ```liste``` qui est la liste dans laquelle l'élément sera recherché, et ```element``` qui est l'élément recherché.
- La fonction utilise une boucle ```for``` qui parcourt chaque index ```i``` de la liste ```liste``` en utilisant la fonction ```range(len(liste))```. La fonction ```len(liste)``` renvoie la longueur de la liste.
- Dans chaque itération de la boucle, la fonction vérifie si l'élément à l'index ```i``` de la liste est égal à l'élément recherché en utilisant l'instruction ```if liste[i] == element:```.
- Si l'élément est trouvé, la fonction retourne l'index de l'élément en utilisant l'instruction ```return i```.
- Si l'élément n'est pas trouvé après avoir parcouru toute la liste, la fonction retourne ```-1``` en utilisant l'instruction ```return -1```.