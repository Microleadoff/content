## PEP 8 : Guide de Style pour le Code Python

Le PEP 8 est une convention de style pour le code Python. Il vise à améliorer la lisibilité et la cohérence du code Python à travers la communauté.

## Principes Généraux

- **Lisibilité** : Le code doit être facile à lire et à comprendre.
- **Cohérence** : Le code au sein d'un projet doit être cohérent.
- **Conformité** : Suivez les conventions de style autant que possible.

## Règles de Formatage

### Indentation
- Utilisez 4 espaces par niveau d'indentation.

### Longueur des Lignes
- Limitez toutes les lignes à un maximum de 79 caractères pour le code et 72 pour les commentaires.

### Utilisation des Blancs
- Utilisez des espaces autour des opérateurs et après les virgules.
- Évitez les espaces superflus à l'intérieur des parenthèses, crochets, ou accolades.

### Commentaires
- Les commentaires doivent être des phrases complètes.
- Utilisez des commentaires pour expliquer le "pourquoi", pas le "comment".

### Nommage des Variables
- Les noms de fonctions, variables et attributs doivent être en ```snake_case```.
- Les constantes doivent être en ```UPPER_CASE```.
- Les noms de classes et d'exceptions doivent être en 
```CamelCase```.

## Organisation du Code

### Imports
- Les imports doivent être placés en haut du fichier.
- Chaque import doit être sur une ligne séparée.
- Groupez les imports par ordre :
  1. Bibliothèques standard.
  2. Bibliothèques tierces.
  3. Modules locaux de l'application.

### Espacement dans les Définitions de Fonctions et de Classes
- Utilisez deux lignes vides avant les définitions de classes et de fonctions de niveau supérieur.
- Utilisez une ligne vide entre les méthodes d'une classe.

## Conseils Supplémentaires

- **Code Explicit** : Préférez un code explicite et simple à du code complexe et implicite.
- **Erreurs Silencieuses** : Évitez de passer sous silence les exceptions.
- **Comparaisons** : Utilisez les mots-clés 
```is``` ou ```is not``` pour les comparaisons à ```None```.

Le respect du PEP 8 est recommandé pour la cohérence et la lisibilité dans la communauté Python. Cependant, il est important de savoir quand s'écarter de ces règles pour le bien du projet.

## Lien vers site officiel


<a href="https://peps.python.org/pep-0008/" title="pep-0008" target="_blank" rel="nofollow">PEP 8</a>