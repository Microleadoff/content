## Durée approximative

30 minutes

## Prérequis

- <a href="https://microlead.fr/echelles/python" title="Prérequis en Python" target="_blank">Python niveau 5</a>

## Énoncé

### Description courte

Écrire une fonction Python qui implémente la méthode de Newton pour trouver une approximation d'une racine carrée d'un nombre donné. La méthode de Newton est une méthode itérative qui converge rapidement vers une racine carrée en utilisant une formule de récurrence. Pour approximer la racine carrée de ```x```, la méthode de Newton utilise la formule suivante :

```xn+1 = (xn + x/xn) / 2```

où ```xn``` est l'approximation actuelle de la racine carrée de ```x```, et ```xn+1``` est l'approximation suivante. La méthode se poursuit jusqu'à ce que l'approximation courante soit suffisamment proche de la vraie racine carrée, c'est-à-dire jusqu'à ce que la différence absolue entre ```xn+1``` et ```xn``` soit inférieure à une certaine tolérance donnée.

### Exemple

Si ```x``` est égal à 2, nous pouvons commencer avec une approximation initiale ```x0``` égale à ```1```. En utilisant la formule de récurrence, nous obtenons :

```
x1 = (x0 + 2/x0) / 2 = (1 + 2/1) / 2 = 1.5
x2 = (x1 + 2/x1) / 2 = (1.5 + 2/1.5) / 2 = 1.4166666666666665
x3 = (x2 + 2/x2) / 2 = (1.4166666666666665 + 2/1.4166666666666665) / 2 = 1.4142156862745099
```

Nous pouvons continuer le processus jusqu'à ce que la différence absolue entre ```xn+1``` et ```xn``` soit inférieure à une certaine tolérance, par exemple ```10^-6```. Dans ce cas, nous pouvons arrêter après la troisième itération, car la différence absolue entre ```x2``` et ```x3``` est inférieure à ```10^-6```.

### Contraintes

- N'utilisez que les fonctionnalités de base de python (variables, boucles et conditions).
- vous pouvez exceptionnellement utiliser les fonctions ```len``` et ```sorted```