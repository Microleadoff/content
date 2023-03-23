## Code

```python
def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    
    # Diviser la liste en deux sous-listes
    milieu = len(liste) // 2
    gauche = liste[:milieu]
    droite = liste[milieu:]
    
    # Trier récursivement chaque sous-liste
    gauche = tri_fusion(gauche)
    droite = tri_fusion(droite)
    
    # Fusionner les deux sous-listes triées
    resultat = []
    i, j = 0, 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    
    resultat += gauche[i:]
    resultat += droite[j:]
    
    return resultat
```

## Explications

- Si la liste contient un seul élément ou moins, elle est déjà triée, donc on la retourne.
- Sinon, on divise récursivement la liste en deux sous-listes de taille à peu près égale, en trouvant l'indice du milieu de la liste et en découpant la liste en deux parties à cet indice.
- On trie récursivement chaque sous-liste en appelant la fonction tri_fusion sur chaque sous-liste.
- On fusionne les deux sous-listes triées en une seule liste triée en comparant les éléments de chaque sous-liste. On ajoute le plus petit élément dans la liste triée et on passe à l'élément suivant de la sous-liste correspondante.
- On continue à fusionner les deux sous-listes triées jusqu'à ce que toutes les valeurs aient été ajoutées à la liste triée.
- Enfin, on retourne la liste triée.