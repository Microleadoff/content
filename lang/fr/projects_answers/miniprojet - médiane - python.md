## Code

```python
def median(liste):
    # Trier la liste en ordre croissant
    liste_triee = sorted(liste)
    
    # Calculer l'indice du milieu de la liste
    milieu = len(liste_triee) // 2
    
    if len(liste_triee) % 2 == 0:
        # Si la liste a un nombre pair d'éléments, retourner la moyenne des deux valeurs du milieu
        return (liste_triee[milieu - 1] + liste_triee[milieu]) / 2
    else:
        # Si la liste a un nombre impair d'éléments, retourner la valeur au milieu
        return liste_triee[milieu]
```

## Explications

Dans cette solution, nous avons défini une fonction ```median``` qui prend une liste en entrée. La fonction commence par trier la liste en ordre croissant en utilisant la fonction ```sorted```. Ensuite, la fonction calcule l'indice du milieu de la liste en divisant la longueur de la liste par 2 et en utilisant l'opérateur ```//``` pour obtenir un entier. Si la liste a un nombre pair d'éléments, la fonction retourne la moyenne des deux valeurs du milieu en utilisant l'indice ```milieu``` et l'indice ```milieu-1``` pour accéder à ces valeurs dans la liste triée. Si la liste a un nombre impair d'éléments, la fonction retourne simplement la valeur au milieu de la liste triée en utilisant l'indice ```milieu```.