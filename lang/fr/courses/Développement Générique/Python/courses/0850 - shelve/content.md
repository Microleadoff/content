## Utilisation de ```shelve``` en Python

Le module ```shelve``` en Python crée un «dictionnaire persistant» pour le stockage d'objets Python, permettant ainsi de sauvegarder des objets entre les sessions.

## Importation de ```shelve```
```python
import shelve
```

## Fonctionnement de shelve

**Concept** : shelve utilise le module pickle pour sérialiser les objets, les sauvegardant dans un fichier qui peut être rouvert et modifié ultérieurement.
**Interface** : Fonctionne comme un dictionnaire où les clés sont des chaînes et les valeurs sont des objets Python.

## Ouverture d'une Étagère (Shelf)

### Création ou Ouverture

```python
with shelve.open('mon_etagere') as etagere:
    # Utilisation de l'étagère
```

**Persistant** : Les données dans etagere sont conservées entre les exécutions du programme.
**Mode d'Ouverture** : Par défaut, ouvre en mode lecture/écriture.

### Stockage d'Objets

```python
with shelve.open('mon_etagere') as etagere:
    etagere['cle'] = mon_objet  # Sauvegarde l'objet mon_objet
```

### Récupération d'Objets

```python
with shelve.open('mon_etagere') as etagere:
    mon_objet = etagere['cle']  # Récupère l'objet stocké
```

## Avantages de shelve

**Simplicité** : Interface simple pour stocker des objets persistants.
**Flexibilité** : Stocke presque tous les types d'objets Python.
**Pratique** : Alternative légère à des bases de données plus complexes.

## Limitations

**Non Thread-safe** : shelve n'est pas sécurisé pour les accès concurrents de multiples threads ou processus.
**Sécurité** : Comme il utilise pickle, ne stockez pas de données non fiables qui pourraient causer des problèmes de sécurité lors de la désérialisation.

## Bonnes Pratiques

**Fermeture de l'Étagère** : Assurez-vous que l'étagère est fermée correctement pour éviter la corruption des données.
**Gestion des Exceptions** : Gérez les exceptions pour gérer les erreurs de lecture/écriture.
**Utilisation Appropriée** : Idéal pour des projets simples nécessitant une persistance des données sans la complexité d'une base de données.