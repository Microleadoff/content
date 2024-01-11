## Packages en Python

Un package en Python est un moyen de structurer l'espace de noms Python en utilisant des "dossiers de modules". Il permet d'organiser et de regrouper des modules logiquement.

## Qu'est-ce qu'un Package ?

**Définition** : Un package est un dossier contenant un fichier spécial ```__init__.py``` et peut inclure des modules et des sous-packages.
**Objectif** : Organiser de manière logique des modules et des fonctions, facilitant la réutilisation et la navigation dans le code.

## Création d'un Package

1. **Créer un Dossier** : Nommez le dossier selon le nom de votre package.
2. **Ajouter ```__init__.py```** : Créez un fichier vide nommé ```__init__.py``` dans le dossier. Ce fichier indique à Python que le dossier doit être traité comme un package.
3. **Ajouter des Modules** : Placez vos fichiers de module Python (```.py```  ) dans ce dossier.

## Structure d'un Package

mon_package/
│ **init**.py
│ module1.py
│ module2.py
│ sous_package/
│ init.py
│ module3.py



## Utilisation d'un Package

### Importation d'un Module du Package
```python
from mon_package import module1
```

### Importation d'une Fonction Spécifique :

```python
from mon_package.module1 import ma_fonction
```

## Bonnes Pratiques

**Nom Clair et Descriptif** : Choisissez un nom clair et descriptif pour votre package et vos modules.
**Structure Logique** : Organisez les modules et fonctions dans un package de manière logique.
**Documentation** : Documentez clairement l'usage et les fonctions de chaque module dans votre package.

## Distribution de Packages

**setup.py** : Pour distribuer votre package, créez un fichier setup.py à la racine du package avec les informations nécessaires.
**Publication** : Utilisez des outils comme twine pour publier votre package sur PyPI.