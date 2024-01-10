## Générateurs en Python

Les générateurs en Python sont un type d'itérable, comme les listes ou les tuples. Cependant, contrairement aux listes, les générateurs ne stockent pas leurs contenus en mémoire. Ils génèrent les éléments à la volée.

## Création de Générateurs

### Utilisation de Fonctions et ```yield```
- **Définition** : Un générateur est créé avec une fonction qui utilise l'instruction ```yield```.
- **Syntaxe** :

  ```python
def mon_generateur():
    yield valeur
```

### Exemple :

```python
def compte_jusqu_a_trois():
    yield 1
    yield 2
    yield 3
```

## Générateurs avec Expressions

**Syntaxe** : (expression for item in iterable)
**Exemple** :

```python
carres = (x**2 for x in range(10))
```

## Utilisation des Générateurs

**Itération** : Utilisez une boucle for pour itérer sur les valeurs générées.
**Fonctions Intégrées** : ```next()``` pour obtenir la prochaine valeur, ```iter()``` pour convertir en itérateur.

```python
gen = compte_jusqu_a_trois()
next(gen)  # Renvoie 1
next(gen)  # Renvoie 2
```

## Avantages des Générateurs

**Économie de Mémoire** : Ils consomment moins de mémoire car ils génèrent des éléments à la demande.
**Génération à la Volée** : Utile pour générer de grandes séquences de données sans épuiser la mémoire.
**Utilisation dans des Boucles** : Parfait pour traiter chaque élément d'une séquence au fur et à mesure qu'ils sont générés.

## Exemples de Générateurs

### Générateur Simple

```python
def mon_generateur():
  n = 1
  print("C'est parti!")
  yield n

  n += 1
  print("C'est le numéro deux!")
  yield n

  n += 1
  print("Et finalement trois!")
  yield n
```

### Utilisation de Générateurs dans des Boucles

```python
for nombre in mon_generateur():
  print(nombre)
```

## Bonnes Pratiques

**Utilisation Judicieuse** : Employez des générateurs pour les grandes données ou pour des opérations qui ne nécessitent pas la conservation de tous les éléments en mémoire.

**Gestion de l'État** : Soyez conscient que l'état interne d'un générateur ne peut pas être réinitialisé; une fois consommé, il ne peut pas être réutilisé.