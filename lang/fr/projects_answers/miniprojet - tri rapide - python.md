## Code

```python
def tri_rapide(liste):
    if len(liste) <= 1:
        return liste
    
    # Choisir un pivot et diviser la liste en deux sous-listes
    pivot = liste[0]
    gauche = [x for x in liste[1:] if x < pivot]
    droite = [x for x in liste[1:] if x >= pivot]
    
    # Trier récursivement chaque sous-liste
    gauche = tri_rapide(gauche)
    droite = tri_rapide(droite)
    
    # Concaténer les sous-listes triées
    resultat = gauche + [pivot] + droite
    
    return resultat
```

## Explications

- Si la liste contient un seul élément ou moins, elle est déjà triée, donc on la retourne.
- Sinon, on choisit un élément pivot dans la liste, généralement le premier élément de la liste.
- On divise la liste en deux sous-listes, l'une contenant les éléments plus petits que le pivot et l'autre contenant les éléments plus grands ou égaux au pivot. Pour cela, on compare chaque élément de la liste avec le pivot et on place l'élément dans la sous-liste correspondante.
- On trie récursivement chaque sous-liste en appelant la fonction tri_rapide sur chaque sous-liste.
- On concatène les sous-listes triées pour obtenir la liste triée finale. On ajoute d'abord la sous-liste triée de gauche, puis le pivot, puis la sous-liste triée de droite.
- Enfin, on retourne la liste triée.