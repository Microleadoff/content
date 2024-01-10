## Le Module ```random``` en Python

Le module ```random``` de Python permet de générer des nombres pseudo-aléatoires pour divers cas d'utilisation, comme la simulation, les jeux ou la sécurité.

## Importation du Module

```python
import random
```
## Fonctions Principales

```random.random()```

**Utilisation** : Génère un nombre flottant aléatoire entre 0.0 et 1.0.
**Exemple** :

```python
nombre = random.random()
```

### random.randint(a, b)

**Utilisation** : Génère un entier aléatoire N tel que a <= N <= b.
**Exemple** :

```python
nombre = random.randint(1, 10)
```
### random.randrange(start, stop[, step])

**Utilisation** : Génère un entier aléatoirement sélectionné de la série générée par range(start, stop, step).
**Exemple** :

```python
nombre = random.randrange(0, 100, 5)
```

### random.choice(seq)

**Utilisation** : Sélectionne un élément aléatoire d'une liste non vide seq.
**Exemple** :

```python
element = random.choice(['pomme', 'banane', 'cerise'])
```
### random.shuffle(seq)

**Utilisation** : Mélange les éléments de la liste seq.
**Exemple** :

```python
liste = [1, 2, 3, 4, 5]
random.shuffle(liste)
```

### random.sample(population, k)

**Utilisation** : Retourne une liste de longueur k d'éléments uniques choisis à partir de la population.
**Exemple** :

```python
echantillon = random.sample(range(100), 5)
```

## Sécurité et Répétabilité

### Sécurité

Les fonctions de random ne sont pas sûres pour la cryptographie. Utilisez secrets pour les besoins de sécurité.

### Répétabilité

Utilisez random.seed(a=None) pour initialiser le générateur de nombres aléatoires. Donner le même seed produira la même séquence de nombres.

## Bonnes Pratiques

**Choix de Fonctions** : Utilisez la fonction appropriée pour vos besoins spécifiques pour éviter des erreurs inattendues.

**Comprendre la Répétabilité** : Utilisez seed pour les tests ou la simulation, mais pas pour la génération de données aléatoires sécurisées.