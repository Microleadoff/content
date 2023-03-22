## Code

```python
def recherche_dichotomique(liste, valeur):
    """Recherche dichotomique de la valeur dans la liste."""
    gauche, droite = 0, len(liste) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if liste[milieu] < valeur:
            gauche = milieu + 1
        elif liste[milieu] > valeur:
            droite = milieu - 1
        else:
            return milieu

    return -1
```

## Explications

Voici la fonction recherche_dichotomique avec une explication ligne par ligne :

```python
def recherche_dichotomique(liste, valeur):
    """Recherche dichotomique de la valeur dans la liste."""
```

Cette ligne définit une fonction nommée "recherche_dichotomique" qui prend deux arguments, "liste" et "valeur". La docstring de la fonction explique brièvement ce que fait la fonction.

```python
    gauche, droite = 0, len(liste) - 1
```

Ici, on initialise deux variables, "gauche" et "droite", respectivement à 0 et à la longueur de "liste" diminuée de 1. Ces deux variables vont représenter les bornes de l'intervalle de recherche.

```python
    while gauche <= droite:
```

Cette ligne démarre une boucle while qui va s'exécuter tant que l'intervalle de recherche n'a pas été réduit à un seul élément.

```python
        milieu = (gauche + droite) // 2
```

Ici, on calcule l'indice du milieu de l'intervalle de recherche en prenant la partie entière de la division entière de la somme de "gauche" et "droite" par 2.

```python
        if liste[milieu] < valeur:
            gauche = milieu + 1
```

Si la valeur de l'élément à l'indice "milieu" de "liste" est inférieure à "valeur", alors on sait que la valeur recherchée doit être dans la moitié supérieure de l'intervalle de recherche, donc on déplace "gauche" à l'indice "milieu + 1".

```python
        elif liste[milieu] > valeur:
            droite = milieu - 1
```

Si la valeur de l'élément à l'indice "milieu" de "liste" est supérieure à "valeur", alors on sait que la valeur recherchée doit être dans la moitié inférieure de l'intervalle de recherche, donc on déplace "droite" à l'indice "milieu - 1".

```python
        else:
            return milieu
```

Si la valeur de l'élément à l'indice "milieu" de "liste" est égale à "valeur", alors on a trouvé la valeur recherchée, donc on renvoie l'indice "milieu".

```python
    return -1
```

Si la boucle while se termine sans avoir trouvé la valeur recherchée, alors on renvoie -1 pour indiquer que la valeur n'a pas été trouvée dans la liste.