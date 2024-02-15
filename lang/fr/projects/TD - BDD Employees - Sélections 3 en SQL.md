## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développer un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Employees" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :


1. Sélectionner les employés et managers des départements sans doublons
2. Sélectionner les employés et managers du département d001 sans doublon
3. Sélectionner les numéros des employés et managers du département d001 dont l’embauche a été faite en Janvier 1985 sans doublon
4. Sélectionner les employés et managers du département d001 dont le numéro d’employé est compris entre 110000 et 120000 sans doublon
5. Sélectionner le nombre d’employés et de manager par départements
6. Sélectionner les employés et managers du département d001 avec possibles doublons
7. Sélectionner les employés et managers du département d001 dont le numéro d’employé est compris entre 110000 et 120000 avec possibles doublons
8. Sélectionner les numéros des employés et managers du département d001 dont l’embauche a été faite en Janvier 1985 avec possibles doublons
9. Sélectionner les employés qui ont été ou sont managers de département (INTERSECT - VERSION MySQL Workbench)
10. Sélectionner les employés qui ont été ou sont managers du département « d001 » (INTERSECT - VERSION MySQL Workbench)
11. Sélectionner le nombre d’employés par département qui ont été ou sont managers, utiliser des alias (INTERSECT - VERSION MySQL Workbench)	
12. Sélectionner le nombre d’employés par département qui ont été ou sont managers en 1988, utiliser des alias (INTERSECT - VERSION MySQL Workbench)
13. Sélectionner les employés des départements en excluant ceux qui ont été ou sont managers (EXCEPT)
14. Sélectionner les employés par département si leur numéro est compris entre 110000 et 120000 en excluant ceux qui ont été ou sont managers (EXCEPT)
15. Sélectionner les départements et les employés qui ont été ou sont managers en excluant les employés du département « d004 » (EXCEPT)

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée