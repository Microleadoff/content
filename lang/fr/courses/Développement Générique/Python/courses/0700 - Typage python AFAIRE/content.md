## Typage en Python

Python est un langage de programmation dynamiquement typé, mais à partir de Python 3.5, le support pour le typage statique via les annotations de types a été introduit, offrant des avantages en termes de lisibilité et de débogage.

## Annotations de Types en Python

**Objectif :** Améliorer la lisibilité du code, faciliter le débogage et permettre aux outils de vérifier les types de variables, de paramètres de fonction, et de valeurs de retour.
**PEP 484 :** Introduit le concept d'annotations de types en Python.

## Syntaxe des Annotations de Types

### Annotation des Variables
```python
variable: Type = valeur
```

### Annotation des Fonctions

```python
def fonction(parametre: Type) -> TypeRetour:
    pass
```

## Exemples

### Annotation de Variables Simples

```python
age: int = 25
nom: str = "Alice"
```

### Annotation de Fonctions

```python
def addition(a: int, b: int) -> int:
    return a + b
```

### Types Composés

```python
from typing import List, Dict

nombres: List[int] = [1, 2, 3]
caracteristiques: Dict[str, str] = {"nom": "Alice", "job": "Développeuse"}
```

## Utilisation de mypy pour la Vérification des Types

### ```mypy``` 

Un vérificateur de type statique pour Python.

### Installation

```shell
pip install mypy
```

### Utilisation

```shell
mypy script.py
```

## Avantages du Typage Statique en Python

**Détection Précoce des Erreurs** : Les erreurs de type peuvent être détectées avant l'exécution du code.
**Clarté du Code** : Les annotations de types rendent le code plus facile à comprendre.
**Aide à l'Édition de Code** : Les IDE peuvent utiliser les annotations de types pour l'autocomplétion et l'analyse de code.

## Bonnes Pratiques

**Utilisation Judicieuse** : Utilisez les annotations de types pour clarifier des parties complexes du code, surtout dans les grandes bases de code.
**Types Génériques et Union** : Utilisez des types génériques et Union pour des cas plus complexes.
**Compatibilité** : Gardez à l'esprit la compatibilité avec les versions antérieures de Python qui ne supportent pas les annotations de types.