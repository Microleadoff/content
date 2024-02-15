## Analyse de Fichiers CSV en Python

Les fichiers CSV (Comma-Separated Values) sont un format populaire pour la représentation de données tabulaires. Python fournit le module ```csv``` pour lire et écrire des fichiers CSV, et la bibliothèque ```pandas``` offre des fonctionnalités avancées pour manipuler ces fichiers.

## Utilisation du Module ```csv```

### Importation du Module ```csv```
```python
import csv
```

## Lecture d'un Fichier CSV

### Syntaxe de Base avec ```csv.reader```

```python
with open('fichier.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

## Écriture dans un Fichier CSV

### Syntaxe de Base avec ```csv.writer```

```python
with open('fichier.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nom', 'Age'])
    writer.writerow(['Alice', 30])
```

## Utilisation de pandas pour les Fichiers CSV

### Importation de pandas

```python
import pandas as pd
```

## Lecture d'un Fichier CSV avec pandas

### Syntaxe

```python
df = pd.read_csv('fichier.csv')
```

## Écriture dans un Fichier CSV avec pandas

### Syntaxe

```python
df.to_csv('fichier.csv', index=False)
```

## Options et Paramètres Utiles

### ```csv Module```

#### ```Delimiter```

Spécifiez un délimiteur autre que la virgule.

```python
csv.reader(file, delimiter=';')
```

#### ```Quotechar```

Spécifiez un caractère de citation pour les champs contenant des délimiteurs.

```python
csv.reader(file, quotechar='"')
```

### ```pandas```

#### Sélection de Colonnes 

Lisez seulement certaines colonnes.

```python
pd.read_csv('fichier.csv', usecols=['Nom', 'Age'])
```

#### Gestion des Dates 

Parsez les colonnes de dates automatiquement.

```python
pd.read_csv('fichier.csv', parse_dates=['Date'])
```

## Bonnes Pratiques

**Gestion des Exceptions** : Utilisez des blocs ```try``` et ```except``` pour gérer les erreurs de lecture/écriture.
**Nettoyage des Données** : Nettoyez et validez les données lors du parsing pour éviter des erreurs.
**Choix d'Outils** : Utilisez ```pandas``` pour des fonctionnalités plus avancées, surtout avec de grands ensembles de données.