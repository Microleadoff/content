## Utilisation de ```__name__``` en Python

La variable ```__name__``` en Python est une variable spéciale utilisée pour déterminer si un fichier est exécuté en tant que programme principal ou importé en tant que module.

## Qu'est-ce que ```__name__``` ?

**Définition** : ```__name__``` est une variable intégrée qui obtient sa valeur en fonction de la manière dont le fichier est exécuté.
**Valeurs** :
- ```__main__``` si le fichier est exécuté comme script principal.
- Nom du module si le fichier est importé.

## Utilisation Courante de ```__name__```

### Point d'Entrée du Script
**Syntaxe Typique** :
```python
if __name__ == '__main__':
  # Le code ici est exécuté uniquement lorsque le fichier est le programme principal.
  main()
```

#### But 

Cela permet de séparer le code qui doit être exécuté lors de l'exécution du script du code qui doit être exécuté lors de l'importation en tant que module.

#### Avantages

**Modularité** : Permet de concevoir des fichiers qui peuvent être exécutés en tant que script ou réutilisés en tant que module.
**Test et Débogage** : Facilite le test en exécutant le code dans un contexte de script.

### Exemples

Exemple de Script avec ```__name__``` :

```python
def fonction_utilitaire():
    # Une fonction quelconque
    pass

def main():
    # Code principal
    fonction_utilitaire()

if __name__ == '__main__':
    main()
```

### Explication 

```main()``` est exécuté uniquement si le script est le programme principal. Si le script est importé, ```main()``` n'est pas exécuté.

## Importation du Script en tant que Module

En important ce script dans un autre fichier, seules les fonctions et les classes définies seront accessibles, sans exécuter le code dans ```main()```.

## Bonnes Pratiques

**Utilisez ```__name__``` pour le Point d'Entrée** : C'est une pratique standard pour rendre les scripts Python modulaires et testables.
**Nommez vos Fonctions et Classes de Manière Claire** : Assurez-vous que les fonctions et les classes sont nommées de manière descriptive pour clarifier leur utilisation lors de l'importation en tant que module.