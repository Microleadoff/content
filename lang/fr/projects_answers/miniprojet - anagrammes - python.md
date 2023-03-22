## Code

```python
def est_anagramme(chaine1, chaine2):
    chaine1 = chaine1.lower().replace(" ", "")
    chaine2 = chaine2.lower().replace(" ", "")
    if len(chaine1) != len(chaine2):
        return False
    for c in chaine1:
        if chaine1.count(c) != chaine2.count(c):
            return False
    return True
```

## Explications

- La fonction ```est_anagramme``` prend en entrée deux chaînes de caractères ```chaine1``` et ```chaine2```.
- On commence par convertir les deux chaînes en minuscules et en supprimant les espaces avec les méthodes ```lower()``` et ```replace(" ", "")```.
- On vérifie ensuite si les deux chaînes ont la même longueur : si ce n'est pas le cas, on retourne ```False```.
- Pour chaque caractère de ```chaine1```, on compte le nombre d'occurrences de ce caractère dans ```chaine1``` et ```chaine2``` avec les méthodes ```count(c)```. Si ces nombres d'occurrences sont différents, cela signifie que ```chaine1``` et ```chaine2``` ne contiennent pas les mêmes lettres, et on retourne ```False```.
- Si tous les caractères ont été parcourus sans trouver de différence entre ```chaine1``` et ```chaine2```, cela signifie que ces deux chaînes sont des anagrammes, et on retourne ```True```.