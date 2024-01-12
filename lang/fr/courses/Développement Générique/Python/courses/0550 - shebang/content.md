## Shebang en Python

Le shebang, ou ```#!```, est une ligne d'en-tête dans les scripts exécutables sous les systèmes Unix et Linux. Il indique au système comment exécuter le fichier.

## Qu'est-ce qu'un Shebang ?

**Définition** : Le shebang est la combinaison des caractères ```#!``` suivie du chemin d'accès à un interpréteur.
**But** : Indique au système d'exploitation quel interpréteur utiliser pour exécuter le script.

### Syntaxe du Shebang en Python

**Shebang Standard pour Python** :
```python
#!/usr/bin/env python3
```
### Exemple de Script Python avec Shebang

```python
#!/usr/bin/env python3
print("Hello, World!")
```

## Utilisation et Importance

**Scripts Exécutables** : Rend les scripts Python directement exécutables comme des programmes.
**Portabilité** : L'utilisation de ```/usr/bin/env``` assure que le script utilise l'interpréteur Python disponible dans l'environnement d'exécution.

## Création de Scripts Exécutables

**Ajoutez le Shebang** : Placez le shebang en première ligne de votre script Python.
**Rendez le Script Exécutable** : Changez les permissions du fichier pour le rendre exécutable.

```shell
chmod +x mon_script.py
```

### Exécutez le Script Directement

```shell
./mon_script.py
```

## Bonnes Pratiques

**Version Spécifique de Python** : Précisez python3 dans le shebang pour utiliser explicitement Python 3.
**Scripts Portables** : Utilisez ```/usr/bin/env``` pour une meilleure portabilité entre différents systèmes Unix/Linux.
**Droits d'Exécution** : Assurez-vous que le script a les droits d'exécution appropriés.