## Utilisation de ```subprocess.Popen``` en Python

`subprocess.Popen` est une classe du module ```subprocess``` utilisée pour exécuter des commandes et des processus externes. Elle offre plus de flexibilité que la fonction ```subprocess.run``` pour interagir avec le processus en cours.

## Importation de ```subprocess```
```python
import subprocess
```

## Fonctionnement de Popen

### Création d'un Processus

```python
processus = subprocess.Popen(['commande', 'arg1', 'arg2'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
```

### Paramètres Importants :

```stdout```, ```stderr```, ```stdin``` : Permettent de rediriger les entrées, sorties et erreurs standards.

```shell``` : Si True, exécute la commande dans le shell.

## Communication avec le Processus

### Envoyer des Données

```python
processus.stdin.write('données')
processus.stdin.close()
```

### Lecture des Sorties

```python
sortie, erreur = processus.communicate()
```

## Exemple d'Utilisation de ```Popen```

```python
processus = subprocess.Popen(['grep', 'motif'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
sortie, erreur = processus.communicate('Recherchez ce texte\nune autre ligne')
print(sortie)
```

## Attente de la Fin d'un Processus

### Attente Passive 

```python
processus.wait()
```

## Avantages de Popen

**Contrôle Fin** : Permet un contrôle plus fin sur le processus, notamment pour la lecture et l'écriture dans ```stdin```/```stdout```/```stderr```.
**Non Bloquant** : Peut être utilisé de manière non bloquante avec ```communicate()```.

## Bonnes Pratiques

**Gestion des Ressources** : Assurez-vous de fermer les flux (```stdin```, ```stdout```, ```stderr```) et d'attendre la fin du processus.
**Gestion des Exceptions** : Préparez-vous à gérer les exceptions, notamment les erreurs de processus.
**Sécurité** : Évitez d'utiliser shell=True avec des entrées non fiables pour prévenir les failles de sécurité.