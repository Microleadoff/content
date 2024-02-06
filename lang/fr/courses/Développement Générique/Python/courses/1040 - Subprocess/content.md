## Utilisation de ```subprocess``` en Python

Le module ```subprocess``` permet à votre programme Python d'interagir avec d'autres programmes et processus. Il remplace plusieurs anciens modules et fonctions, tels que ```os.system``` et le module ```os.spawn```.

## Importation de ```subprocess```
```python
import subprocess
```

## Fonctions Principales de subprocess

### subprocess.run

#### Usage

Exécute une commande, attend qu'elle se termine, puis retourne un objet CompletedProcess.

#### Exemple

```python
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
```

### subprocess.Popen

#### Usage 

Permet une interaction plus avancée avec le processus (entrées/sorties).

#### Exemple

```python
with subprocess.Popen(['grep', 'motif'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) as proc:
    stdout, _ = proc.communicate('Recherchez ce texte\nune autre ligne')
    print(stdout)
```

## Exécution de Commandes Simples

```python
subprocess.run(['echo', 'Bonjour le monde!'])
```

## Capturer la Sortie d'une Commande

```python
result = subprocess.run(['ls', '-l', '/dossier/inexistant'], capture_output=True, text=True, check=True)
print("Sortie:", result.stdout)
print("Erreur:", result.stderr)
```

## Exécution de Commandes Shell

### Avec ```shell=True```

```python
subprocess.run('cat mon_fichier.txt | grep motif', shell=True)
```

## Gestion des Exceptions

**```subprocess.CalledProcessError```** : Se produit lorsque la commande exécutée avec ```check=True``` se termine par un code de sortie non nul.

## Gestion de l'Exception

```python
try:
    subprocess.run(['ls', '-l', '/dossier/inexistant'], check=True)
except subprocess.CalledProcessError as e:
    print('Erreur:', e)
```

## Bonnes Pratiques

**Sécurité** : Évitez shell=True autant que possible, car cela peut être une faille de sécurité, en particulier si vous exécutez des commandes construites à partir d'entrées utilisateur.
**Gestion des Ressources** : Utilisez le gestionnaire de contexte (```with```) avec ```subprocess.Popen``` pour vous assurer que les ressources sont libérées.
**Validation des Entrées** : Soyez prudent avec les données entrées dans les commandes pour éviter les injections de commandes.