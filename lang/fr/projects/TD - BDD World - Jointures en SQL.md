## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les jointures dans une base de données SQL au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développer un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "World" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Sélectionner les noms des pays et leurs sous-continents associés, triés par ordre alphabétique des sous-continents (INNER JOIN)
2. Sélectionner les noms des continents et leurs sous-continents correspondants (INNER JOIN)
3. Sélectionner les noms des pays et leurs capitales (INNER JOIN)
4. Sélectionner les noms des États et leurs pays correspondants (INNER JOIN)
5. Sélectionner le nombre de pays par continent (INNER JOIN)
6. Sélectionner les noms des sous-régions, des villes et leurs latitudes associées (INNER JOIN)
7. Sélectionner les noms des pays ayant au moins une ville répertoriée dans un sous-continent ayant plus de 10 villes (INNER JOIN et Sous-requête)
8. Sélectionner les pays et les États (CROSS JOIN)
9. Sélectionner les pays et les capitales (CROSS JOIN)
10. Sélectionner les continents et les États (CROSS JOIN)
11. Sélectionner les continents et les États (CROSS JOIN)
12. Sélectionner les pays associés à leurs capitales (LEFT JOIN)
13. Sélectionner le nombre de pays par continent (LEFT JOIN)
14. Sélectionner les noms des capitales avec les noms de ville pour les pays associés(LEFT JOIN)
15. Sélectionner les noms des pays avec leurs villes associées dont la latitude est supérieure à 45 degrés (LEFT JOIN)
16. Sélectionner les sous-continents et les noms de pays associés dont la latitude est inférieure à 30 degrés (LEFT JOIN)
17. Sélectionner les noms des villes avec leurs pays associés (RIGHT JOIN)
18. Sélectionner les noms des sous-continents avec les noms de ville pour les pays associés (RIGHT JOIN)
19. Sélectionner les noms des sous-continents et des villes pour les pays associés dont la latitude est inférieure à 30 degrés (RIGHT JOIN)
20. Sélectionner les noms des pays avec leurs villes associées ayant une latitude supérieure à 45 degrés (RIGHT JOIN)
21. Sélectionner les noms des pays et leurs capitales (FULL JOIN)
22. Sélectionner les noms des villes et des pays associés (FULL JOIN)
23. Sélectionner les noms des continents et les pays associés (FULL JOIN)
24. Sélectionner les noms des villes et leurs pays associés avec une latitude supérieure à 40 degrés (FULL JOIN)
25. Sélectionner les pays ayant la même latitude que d'autres pays (SELF JOIN)
26. Sélectionner les États partageant le même pays avec d'autres États (SELF JOIN)
27. Sélectionner les villes partageant le même nom avec d'autres villes (SELF JOIN)

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée