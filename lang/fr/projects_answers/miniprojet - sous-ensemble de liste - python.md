## Code

```python
def trouver_sous_ensembles(liste, k):
    resultat = []
    n = len(liste)

    for i in range(2**n):
        sous_ensemble = []
        for j in range(n):
            if i & (1 << j):
                sous_ensemble.append(liste[j])

        if sum(sous_ensemble) == k:
            resultat.append(sous_ensemble)

    return resultat
```

## Explications

La première ligne déclare une fonction appelée trouver_sous_ensembles qui prend en entrée une liste de nombres liste et une valeur cible k.

```python
def trouver_sous_ensembles(liste, k):
```

La deuxième ligne crée une liste vide appelée resultat qui sera utilisée pour stocker les sous-ensembles de liste dont la somme est égale à k.

```python
    resultat = []
```

La troisième ligne détermine la longueur de la liste liste et la stocke dans la variable n.

```python
    n = len(liste)
```

La boucle for suivante itère sur tous les entiers entre ```0``` et ```2**n```, c'est-à-dire tous les nombres binaires de ```n``` bits. Elle utilise la fonction ```range``` pour générer une séquence d'entiers allant de ```0``` à ```2**n - 1```, inclusivement.

```python
    for i in range(2**n):
```

Pour chaque entier ```i```, la boucle interne suivante crée un nouveau sous-ensemble de liste en examinant chaque bit de ```i``` et en ajoutant l'élément correspondant de liste au sous-ensemble si le bit est 1. Elle utilise la fonction range pour générer une séquence d'entiers allant de ```0``` à ```n - 1```, inclusivement.

```python
        sous_ensemble = []
        for j in range(n):
            if i & (1 << j):
                sous_ensemble.append(liste[j])
```

Si la somme des éléments du sous-ensemble est égale à ```k```, le sous-ensemble est ajouté à la liste resultat.

```python
        if sum(sous_ensemble) == k:
            resultat.append(sous_ensemble)
```

Après avoir parcouru tous les entiers de ```0``` à ```2**n - 1```, la fonction retourne la liste resultat contenant tous les sous-ensembles de liste dont la somme est égale à ```k```.

```python
    return resultat
```

En somme, cette fonction utilise une méthode de force brute pour trouver tous les sous-ensembles de ```liste``` dont la somme est égale à ```k```. Elle examine tous les nombres binaires de ```n``` bits et ajoute chaque élément de liste correspondant à un bit 1 pour construire tous les sous-ensembles possibles. Enfin, elle vérifie si la somme des éléments de chaque sous-ensemble est égale à ```k```, et stocke ceux qui le sont dans la liste resultat.