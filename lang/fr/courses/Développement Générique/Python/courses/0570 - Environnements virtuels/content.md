## Environnements Virtuels en Python

Les environnements virtuels en Python sont des espaces isolés utilisés pour gérer les dépendances de projets Python individuels. Ils permettent d'installer des paquets sans affecter d'autres projets ou la configuration globale du système.

## Pourquoi Utiliser des Environnements Virtuels ?

### Isolation  

Permet de travailler sur des projets avec des dépendances différentes sans conflits.

### Contrôle des Versions 

Chaque environnement peut avoir ses propres versions spécifiques de paquets.

### Facilité de Reproduction 

Rend les projets plus faciles à partager et à reproduire sur d'autres machines.

## Création d'un Environnement Virtuel

### Utilisation de ```venv``` (Python 3.3 et Plus)

**Création** :

```shell
python3 -m venv nom_du_env
```

### Activation

#### Sur Linux/macOS

```shell
source nom_du_env/bin/activate
```

#### Sur Windows

```shell
.\nom_du_env\Scripts\activate
```

### Utilisation de virtualenv (Versions Antérieures de Python)

#### Installation de virtualenv

```shell
pip install virtualenv
```

#### Création

```shell
virtualenv nom_du_env
```

#### Activation 

Identique à venv.

## Gestion des Paquets dans un Environnement Virtuel

### Installation des Paquets 

Utilisez pip pour installer des paquets spécifiques à l'environnement.

```shell
pip install <paquet>
```

### Création d'un requirements.txt

```shell
pip freeze > requirements.txt
```

## Désactivation de l'Environnement Virtuel

### Désactivation

```shell
deactivate
```

## Bonnes Pratiques

**Un Environnement par Projet** : Créez un environnement virtuel distinct pour chaque projet.
**Versionnage de requirements.txt** : Versionnez le fichier requirements.txt pour assurer la reproductibilité des dépendances.
**Ignorer les Fichiers d'Environnement** : Utilisez ```.gitignore``` pour ignorer les dossiers d'environnement virtuel dans les systèmes de contrôle de version.