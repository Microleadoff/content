## Gestion des Fichiers d'Environnement en Python

Les fichiers d'environnement sont utilisés pour stocker des variables d'environnement, séparant ainsi la configuration sensible ou spécifique à un environnement du code. En Python, le module ```os``` et la bibliothèque ```python-dotenv``` sont couramment utilisés pour manipuler ces fichiers.

## Utilisation du Module ```os``` pour les Variables d'Environnement

### Importation du Module ```os```
```python
import os
```

## Accès aux Variables d'Environnement

### Lecture 

Utilisez ```os.environ``` pour accéder aux variables d'environnement.

```python
db_password = os.environ.get('DB_PASSWORD')
```

### Modification 

Affectez des valeurs à ```os.environ```.

```python
os.environ['DB_PASSWORD'] = 'secret'
```

## Utilisation de python-dotenv pour Gérer les Fichiers ```.env```

### Installation de ```python-dotenv```

```shell
pip install python-dotenv
```

## Création d'un Fichier ```.env```

Créez un fichier ```.env``` dans le répertoire racine de votre projet et ajoutez des variables d'environnement :

```makefile
DB_PASSWORD=secret
API_KEY=mon_api_key
```

## Chargement des Variables Depuis le Fichier ```.env```

### Syntaxe

```python
from dotenv import load_dotenv
load_dotenv()
```

### Accès aux Variables

```python
db_password = os.environ.get('DB_PASSWORD')
```

## Bonnes Pratiques

**Sécurité** : Ne stockez jamais de fichiers .env dans des dépôts de code source publics.
**```.env``` pour le Développement** : Utilisez des fichiers ```.env``` principalement pour le développement et les tests.
**Variables d'Environnement pour la Production** : En production, configurez les variables d'environnement directement sur l'hôte ou le service d'hébergement.
**Documentation** : Documentez les variables d'environnement requises dans votre ```README``` ou une documentation séparée.