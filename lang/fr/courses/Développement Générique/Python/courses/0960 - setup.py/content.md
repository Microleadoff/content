## Création d'un Fichier ```setup.py``` en Python

Le fichier ```setup.py``` est un script de configuration utilisé pour la distribution de packages Python. Il définit les métadonnées et les options de configuration pour le package, et est utilisé par des outils comme ```setuptools``` pour créer des distributions de package.

## Structure de Base de ```setup.py```

```python
from setuptools import setup, find_packages

setup(
    name='mon_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Dépendances nécessaires ici
    ],
    # Autres métadonnées
)
```

## Éléments Clés de ```setup.py```

**name** : Nom du package.
**version** : Version du package.
**packages** : Liste des packages à inclure. ```find_packages()``` trouve automatiquement tous les packages.
**install_requires** : Liste des dépendances nécessaires à installer avec le package.
**Autres Métadonnées** : Comme author, description, url, etc.

## Ajout de Scripts Exécutables

```python
setup(
    # ... autres options ...
    scripts=['bin/mon_script']
)
```

## Gestion des Dépendances

**Dépendances Externes** : Spécifiez toutes les bibliothèques externes dont votre package a besoin dans install_requires.
**Dépendances de Développement** : Utilisez extras_require pour spécifier des dépendances optionnelles, par exemple pour le développement ou les tests.

## Utilisation de setuptools

### Installation Locale : Pour installer le package localement (par exemple, pour le développement), utilisez :

```shell
pip install -e .
```

### Création de Distributions : Pour créer une distribution (comme une archive source ou une roue), utilisez :

```shell
python setup.py sdist bdist_wheel
```

## Bonnes Pratiques

**Lisibilité** : Assurez-vous que votre fichier setup.py est clair et documente correctement les dépendances et les métadonnées de votre package.
**Versionnage** : Gérez soigneusement les versions de votre package pour une meilleure compatibilité et un suivi facile.
**Tests** : Testez votre package dans différents environnements pour vous assurer qu'il s'installe et fonctionne correctement.