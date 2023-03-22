## Code

```python
def newton_sqrt(x, tolerance=1e-6):
    """
    Calcule une approximation de la racine carrée de x en utilisant la méthode de Newton.
    
    :param x: Le nombre dont on cherche la racine carrée.
    :param tolerance: La différence absolue maximale entre deux approximations successives de la racine carrée.
                      Par défaut, la tolérance est de 10^-6.
    :return: Une approximation de la racine carrée de x.
    """
    # Définition de l'approximation initiale
    x0 = x / 2
    
    # Boucle itérative pour calculer les approximations successives
    while True:
        # Calcul de l'approximation suivante
        xn = (x0 + x / x0) / 2
        
        # Vérification de la condition d'arrêt
        if abs(xn - x0) < tolerance:
            break
        
        # Mise à jour de l'approximation courante
        x0 = xn
    
    # Retourne l'approximation finale de la racine carrée
    return xn
```

## Explications

La fonction ```newton_sqrt``` prend en entrée un nombre ```x``` et une tolérance facultative ```tolerance``` qui indique la différence absolue maximale entre deux approximations successives de la racine carrée. Par défaut, la tolérance est de ```10^-6```. La fonction commence par définir une approximation initiale ```x0``` de la racine carrée de ```x```, qui est simplement égale à ```x/2```. Ensuite, la fonction entre dans une boucle itérative qui calcule les approximations successives de la racine carrée en utilisant la formule de récurrence de la méthode de Newton. La boucle s'arrête lorsque la différence absolue entre l'approximation courante et l'approximation précédente est inférieure à la tolérance donnée. Enfin, la fonction retourne l'approximation finale de la racine carrée.