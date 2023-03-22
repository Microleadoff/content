## Code

```python
def trouver_sous_ensembles(liste, k):
    if not liste:
        return []
    if len(liste) == 1:
        return [[liste[0]]] if liste[0] == k else []
    res = []
    for sous_ensemble in trouver_sous_ensembles(liste[:-1], k):
        res.append(sous_ensemble)
        if sum(sous_ensemble) + liste[-1] == k:
            res.append(sous_ensemble + [liste[-1]])
    if liste[-1] == k:
        res.append([liste[-1]])
    return res
```

## Explications

- La fonction trouver_sous_ensembles prend en entrée une liste de nombres entiers liste et un nombre entier k.
- On commence par traiter les cas particuliers où la liste est vide ou contient un seul élément : dans ces cas-là, la fonction retourne une liste vide ou une liste contenant l'élément s'il est égal à k.
- Sinon, on appelle récursivement la fonction sur la liste sans le dernier élément (liste[:-1]), et on stocke le résultat dans la variable res.
- On parcourt ensuite tous les sous-ensembles trouvés dans res, et pour chacun d'entre eux, on ajoute le dernier élément de la liste s'il permet d'obtenir une somme égale à k. On stocke ensuite ce nouveau sous-ensemble dans res.
- Si le dernier élément de la liste est lui-même égal à k, on ajoute une liste contenant uniquement cet élément à res.
- Enfin, la fonction retourne res contenant tous les sous-ensembles trouvés ayant une somme égale à k.

**Note** : Cette solution utilise une approche récursive pour trouver tous les sous-ensembles. Cela peut être coûteux en temps de calcul pour des listes de grande taille. Il existe des algorithmes plus efficaces pour résoudre ce problème, mais ils sont également plus complexes à implémenter.