## Opérations Mathématiques de Base en Python

Python offre une gamme d'opérateurs mathématiques pour effectuer des calculs courants. 
Voici un guide sur leur utilisation :

### Addition (`+`)

Utilisation : Pour additionner deux nombres.
```result = 3 + 2  #result sera 5```

### Soustraction (`-`)

Utilisation : Pour soustraire un nombre d'un autre.
```result = 3 - 2  # result sera 1```

### Multiplication (`*`)

Utilisation : Pour multiplier deux nombres.
```result = 3 * 2  # result sera 6```

### Division (`/`)

Utilisation : Pour diviser un nombre par un autre. Renvoie toujours un float.
```result = 3 / 2  # result sera 1.5```

### Division Entière (`//`)

Utilisation : Pour une division qui renvoie la partie entière du quotient.
```result = 3 // 2  # result sera 1```

### Modulo (`%`)

Utilisation : Pour obtenir le reste d'une division.
```result = 3 % 2  # result sera 1```

### Puissance (`**`)

Utilisation : Pour élever un nombre à la puissance d'un autre.
```result = 3 ** 2  # result sera 9```

### Racine Carrée

Utilisation : Utilisez l'opérateur de puissance avec 0.5 ou la fonction sqrt du module math.
```python

racine = 9 ** 0.5  # racine sera 3

# ou

import math
racine = math.sqrt(9)  # racine sera 3
```

## Priorité des Opérateurs

Les opérations sont évaluées dans l'ordre suivant : `**`, `*`, `/`, `//`, `%`, `+`, `-`.
Utilisez des parenthèses pour modifier l'ordre d'évaluation.

## Bibliothèque Math

Pour des fonctions mathématiques plus avancées, utilisez le module math.
```python

import math
result = math.sin(math.pi / 2)  # result sera 1.0
```
## Bonnes Pratiques

Lisibilité : Utilisez des espaces autour des opérateurs pour une meilleure lisibilité.
Parenthèses : Utilisez-les pour clarifier l'ordre des opérations.
Importation Sélective : Importez uniquement les fonctions nécessaires depuis le module 
math pour économiser de l'espace mémoire.


Les opérations mathématiques sont fondamentales dans presque tous les programmes Python. 
Comprendre ces opérateurs et savoir comment les utiliser est crucial pour effectuer des 
calculs et résoudre des problèmes.

