## Code

```python
def tri_insertion(liste):
    for i in range(1, len(liste)):
        valeur_courante = liste[i]
        position = i
        
        while position > 0 and liste[position - 1] > valeur_courante:
            liste[position] = liste[position - 1]
            position -= 1
        
        liste[position] = valeur_courante
    
    return liste
```

## Explications

- On commence par boucler sur les indices de la liste à partir de l'indice 1 jusqu'à la fin de la liste.
- On récupère la valeur de l'élément courant et on stocke sa position dans une variable.
- On compare la valeur courante avec les éléments de la liste triée précédemment, en partant de la fin de la liste triée jusqu'à l'élément d'indice 0.
- Tant que l'élément courant est plus petit que l'élément de la liste triée, on déplace l'élément de la liste triée vers la droite pour faire de la place pour l'élément courant. On continue à déplacer les éléments triés tant que l'on n'a pas atteint la fin de la liste triée ou que l'on a trouvé l'emplacement correct pour l'élément courant.
- On insère finalement l'élément courant à sa position correcte dans la liste triée.
- On répète ce processus pour tous les éléments de la liste à trier.
- Enfin, on retourne la liste triée.