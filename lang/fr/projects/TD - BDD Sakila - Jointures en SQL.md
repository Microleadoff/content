## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développer un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Sakila" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Sélectionner titres de films et les identifiants d'acteurs auxquels ils sont associés (INNER JOIN)
2. Sélectionner les noms et prénoms distincts des clients ayant effectué des paiements (INNER JOIN)
3. Sélectionner les noms des catégories et les titres des films associés (INNER JOIN)
4. Sélectionner les titres des films, les noms et prénoms des acteurs qui ont joué dans ces films (INNER JOIN)
5. Sélectionner les titres des films et les montants des paiements associés à leurs locations (INNER JOIN)
6. Sélectionner les noms et prénoms des clients ayant effectué des paiements pour des films de la catégorie « Action » (INNER JOIN et sous-requête)
7. Sélectionner  les titres des films et les langues (CROSS JOIN)
8. Sélectionner les noms et prénoms des clients et les adresses (CROSS JOIN)
9. Sélectionner les noms et prénoms des acteurs et les films (CROSS JOIN)
10. Sélectionner les noms des catégories et les titres des films (CROSS JOIN)
11. Sélectionner les noms et prénoms des clients, les adresses et les noms des villes (CROSS JOIN)
12. Sélectionner les titres des films et les langues auxquelles ils sont associés (LEFT JOIN)
13. Sélectionner les noms et prénoms des clients et les montants de paiement auxquels ils sont associés (LEFT JOIN)
14. Sélectionner les titres des films et les noms et prénoms des acteurs auxquels ils sont associés (LEFT JOIN)
15. Sélectionner les noms et prénoms des clients et les adresses auxquelles ils sont associés (LEFT JOIN)
16. Sélectionner les titres des films et les catégories associées (LEFT JOIN)
17. Sélectionner les identifiants, titres des films et les catégories associées (RIGHT JOIN)
18. Sélectionner les identifiants des adresses et les noms des villes auxquels ils sont associés (RIGHT JOIN)
19. Sélectionner les identifiants des clients et les montants de paiement auxquels ils sont associés (RIGHT JOIN)
20. Sélectionner les identifiants des pays et les noms des villes auxquelles ils sont associés (RIGHT JOIN)
21. Sélectionner les noms et prénoms des acteurs et les films associés (FULL JOIN)
22. Sélectionner les catégories de films et les films associés (FULL JOIN)
23. Sélectionner les paiements et les dates de locations associées (FULL JOIN)
24. Sélectionner les ventes et les noms et prénoms des clients associés (FULL JOIN)
25. Sélectionner les ventes et les noms et prénoms des employés associés (FULL JOIN)
26. Sélectionner les noms et prénoms des acteurs ayant le même nom que d'autres acteurs (SELF JOIN)
27. Sélectionner adresses partageant la même ville (SELF JOIN)
28. Sélectionner les noms et prénoms des clients qui ont un prénom identique et fréquente le même magasin (SELF JOIN)
29. Sélectionner les films qui ont des acteurs communs (SELF JOIN)
30. Sélectionner les villes ayant le même pays (SELF JOIN)

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée