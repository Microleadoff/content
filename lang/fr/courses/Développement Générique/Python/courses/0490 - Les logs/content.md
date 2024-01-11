## Mise en Place des Logs en Python avec le Module ```logging```

Le logging est essentiel pour suivre les événements qui se produisent lors de l'exécution d'un programme. En Python, le module ```logging``` offre des fonctionnalités flexibles pour la journalisation.

## Importation du Module ```logging```

```python
import logging
```

## Configuration de Base

### Configuration Simple

#### Utilisation

Configure le niveau de logging et le format par défaut.

#### Syntaxe

```python
logging.basicConfig(level=logging.INFO)
```

### Niveaux de Logging

```logging.DEBUG```: Pour des informations de débogage détaillées.
```logging.INFO```: Pour des informations générales.
```logging.WARNING```: Pour des avertissements (niveau par défaut).
```logging.ERROR```: Pour signaler des erreurs.
```logging.CRITICAL```: Pour des problèmes graves.

## Utilisation des Loggers

### Création d'un Logger

#### Syntaxe

```python
logger = logging.getLogger(__name__)
```

### Écriture de Messages de Log

#### Syntaxe

```python
logger.debug('Message de debug')
logger.info('Message informatif')
logger.warning('Message d’avertissement')
logger.error('Message d’erreur')
logger.critical('Message critique')
```

## Configuration Avancée

### Format des Messages

#### Syntaxe

```python
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
```

### Redirection des Logs vers un Fichier

#### Syntaxe

```python
logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG)
```

## Handlers et Formatters

### Utilisation de Handlers

#### But 

Permet de diriger les logs vers différents endroits.

#### Exemple

```python
handler = logging.FileHandler('app.log')
logger.addHandler(handler)
```

### Utilisation de Formatters

#### But 

Permet de configurer le format des messages de log.

#### Exemple

```python
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
```

## Bonnes Pratiques

**Niveau de Logging Approprié** : Utilisez le niveau de logging approprié pour chaque message.
**Gestion des Exceptions** : Utilisez ```logger.exception()``` dans un bloc except pour enregistrer des exceptions.
**Configuration Centralisée** : Configurez le logging au début de votre programme.
**Évitez les Logs Verbeux** : N'enregistrez que les informations nécessaires pour éviter des logs trop verbeux.