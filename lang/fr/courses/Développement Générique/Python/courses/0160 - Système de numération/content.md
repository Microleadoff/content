## Systèmes de Numération en Python

Python offre des outils pour travailler avec différents systèmes de numération (bases), notamment binaire (base 2), octal (base 8), décimal (base 10), et hexadécimal (base 16).

## Binaire (Base 2)
- **Représentation :** Les nombres binaires sont composés uniquement de 0 et de 1.
- **Préfixe Python :** `0b` ou `0B`.

  binary_number = 0b101  # équivalent décimal est 5

## Octal (Base 8)

Représentation : Les nombres octaux utilisent les chiffres de 0 à 7.
Préfixe Python : 0o ou 0O.
```octal_number = 0o7  # équivalent décimal est 7```

## Décimal (Base 10)

Représentation : Le système que nous utilisons habituellement avec les chiffres de 0 à 9.
Aucun préfixe particulier n'est nécessaire.
```python
decimal_number = 10  # c'est déjà en base 10
```

## Hexadécimal (Base 16)

Représentation : Utilise les chiffres de 0 à 9 et les lettres de A (10) à F (15).
Préfixe Python : 0x ou 0X.

```python
hexadecimal_number = 0xA  # équivalent décimal est 10
```
## Conversion entre les Systèmes

### De Binaire :


```python 
int('101', 2)  # Convertit une chaîne binaire en entier décimal
```

### De Octal :

```python
int('7', 8)  # Convertit une chaîne octale en entier décimal
```

### De Hexadécimal :

```python
int('A', 16)  # Convertit une chaîne hexadécimale en entier décimal
```

### Conversion vers les Systèmes

### Vers Binaire :

```python
bin(5)  # Convertit un nombre décimal en chaîne binaire
```

### Vers Octal :

```python
oct(7)  # Convertit un nombre décimal en chaîne octale
```

### Vers Hexadécimal :

```python
hex(10)  # Convertit un nombre décimal en chaîne hexadécimale
```

## Bonnes Pratiques

Clarté : Utilisez des noms de variables clairs pour indiquer le système de numération.

Vérification : Vérifiez toujours le type et la validité des données lors de la conversion entre les systèmes.

Commentaires : Ajoutez des commentaires pour clarifier les conversions et les valeurs particulières.



Les systèmes de numération sont une partie fondamentale de l'informatique. Comprendre comment les manipuler en Python est essentiel pour travailler avec des données à bas niveau, effectuer des opérations de bit, ou simplement pour convertir des valeurs entre différents systèmes.