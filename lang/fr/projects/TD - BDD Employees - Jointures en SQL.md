## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développer un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Employees" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Sélectionner les noms, prénoms et numéros des employés et leur département actuel (INNER JOIN)
2. Sélectionner les prénoms, noms et titres actuels des employés (INNER JOIN)
4. Sélectionner les noms, prénoms et salaires des employés en Juin 1989 (INNER JOIN)
5. Sélectionner les noms, prénoms et départements actuels des managers (INNER JOIN)
6. Sélectionner les noms, prénoms et dates de début d'emploi des employés avec leur département (INNER JOIN)
7. Sélectionner les noms et départements des employés ayant le même département que les managers ayant été embauchés après le 1er Janvier 1996 (INNER JOIN et Sous-requêtes)
8. Sélectionner les employés et leur date d'embauche dans les départements où le salaire moyen est supérieur à 80000 (INNER JOIN et Sous-requêtes)
9. Sélectionner les employés et les départements (CROSS JOIN)
10. Sélectionner les postes actuels des employés avec les noms des départements (CROSS JOIN)
11. Sélectionner les dates d'emploi des employés et les noms des départements (JOIN et CROSS JOIN)
12. Sélectionner les noms, prénoms, dates d’embauche et départements des employés même s’ils n’ont pas de département associé (LEFT JOIN)
13. Sélectionner les noms, prénoms et titres des employés même s’ils n’ont pas de titre associé (LEFT JOIN)
14. Sélectionner les noms, prénoms et salaires des employés depuis 1985 (LEFT JOIN)
15. Sélectionner les noms, prénoms et départements des employés même s’ils n’ont pas de département associé (RIGHT JOIN)
16. Sélectionner les noms, prénoms et salaires des employés depuis 1985 (RIGHT JOIN)
17. Sélectionner les noms, prénoms et titres des employés même s’ils n’ont pas de titre associé (RIGHT JOIN)
18. Sélectionner les noms, prénoms et départements des employés même s’ils n’ont pas de département associé (FULL JOIN)
19. Sélectionner les noms, prénoms et salaires des employés depuis 1985 (FULL JOIN)
20. Sélectionner les noms, prénoms et titres des employés même s’ils n’ont pas de titre associé (FULL JOIN)
21. Sélectionner les managers ayant le même département que d'autres managers (SELF JOIN)
22. Sélectionner les managers ayant la même date d’embauche que d'autres managers (SELF JOIN)
23. Sélectionner les informations sur les employés et leurs salaires (NATURAL JOIN)
24. Sélectionner les informations sur les employés managers (NATURAL JOIN)
25. Sélectionner les informations sur les employés managers et leur département (NATURAL JOIN)
26. Sélectionner les identifiants, noms et prénoms des employés et la somme de leur salaire par identifiant (NATURAL JOIN)
27. Sélectionner la somme des salaires par département (NATURAL JOIN)


### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée