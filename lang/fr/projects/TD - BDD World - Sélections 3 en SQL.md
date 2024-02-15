## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développer un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "World" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :


1. Sélectionner les identifiants et codes de pays des villes et des états sans doublon
2. Sélectionner les identifiants, noms et dates de créations des continents des tables : continent (regions) et pays (countries) si l’identifiant du continent est compris entre 1 et 3 sans doublon
3. Sélectionner les identifiants et codes de pays des villes et des états si les codes de pays contiennent la lettre « A » sans doublon
4. Sélectionner les identifiants et dates de création des continents et sous-continents si les identifiants sont compris entre 1 et 10 sans doublon
5. Sélectionner les identifiants et codes de pays des villes et des états si les codes de pays sont compris entre 1 et 10 
6. Sélectionner les identifiants et codes de pays des villes et des états avec possibles doublons
7. Sélectionner les identifiants, noms et dates de créations des continents tables : continent (regions) et pays (countries) si l’identifiant du continent est compris entre 1 et 3 avec possibles doublons
8. Sélectionner les identifiants et codes de pays des villes et des états si les codes de pays contiennent la lettre « A » avec possibles doublon
9. Sélectionner les identifiants et dates de création des continents et sous-continents si les identifiants sont compris entre 1 et 10 avec possibles doublons
10. Sélectionner les pays dont les identifiants correspondent à ceux référencés dans la table des villes (INTERSECT - VERSION MySQL Workbench)
11. Sélectionner les pays dont les identifiants correspondent à ceux référencés dans la table des villes si le code ISO2 du pays termine par un « E » (INTERSECT - VERSION MySQL Workbench)
12. Sélectionner les États dont les identifiants correspondent à ceux référencés dans la table des villes (INTERSECT - VERSION MySQL Workbench)
13. Sélectionner les états dont les identifiants correspondent à ceux des pays référencés dans les 200 premières entrées de la table des villes (INTERSECT - VERSION MySQL Workbench)
14. Sélectionner les identifiants et les codes ISO2 des pays en excluant ceux qui sont dans la table des villes (EXCEPT)
15. Sélectionner les identifiants et les codes des pays de la table des États en excluant ceux qui sont dans la table des villes (EXCEPT)

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée