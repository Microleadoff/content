## Utilisation de ```sys.argv``` en Python

```sys.argv``` est une liste en Python, accessible dans le module ```sys```, qui contient les arguments de ligne de commande passés à un script Python. Elle est souvent utilisée pour obtenir des entrées utilisateur pour des scripts en ligne de commande.

## Importation du Module ```sys```
```python
import sys
```

## Fonctionnement de ```sys.argv```

**Contenu** : ```sys.argv[0]``` est le nom du script. Les arguments suivants sont ceux passés au script.
**Exemple** : Si un script est exécuté avec python ```mon_script.py arg1 arg2```, alors ```sys.argv``` sera ```['mon_script.py', 'arg1', 'arg2']```.

## Utilisation de Base

### Récupération des Arguments

```python
# mon_script.py
import sys

if len(sys.argv) > 1:
    premier_argument = sys.argv[1]
    print(f"Premier argument: {premier_argument}")
```

### Gestion des Arguments

**Taille de ```sys.argv```** : Utilisez ```len(sys.argv)``` pour vérifier le nombre d'arguments.
**Itération sur les Arguments** :

```python
for arg in sys.argv[1:]:
    print(arg)
```

## Exemple Simple

```python

# addition.py
import sys

if len(sys.argv) == 3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(f"La somme est {a + b}")
else:
    print("Usage: python addition.py <nombre1> <nombre2>")
```

## Bonnes Pratiques

**Validation des Entrées** : Vérifiez et validez les arguments pour éviter les erreurs.
**Gestion des Erreurs** : Ajoutez une gestion d'erreurs pour les entrées incorrectes.
**Aide et Documentation** : Fournissez des instructions claires sur l'utilisation du script en ligne de commande.
**Utilisation Limitée** : Pour des besoins plus complexes, envisagez d'utiliser des modules comme ```argparse```.