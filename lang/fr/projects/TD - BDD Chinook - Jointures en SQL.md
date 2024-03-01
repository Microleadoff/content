## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développé un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Chinook" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Sélectionner les titres des albums dont l'artiste est « Led Zeppelin » (JOIN)
2. Sélectionner les titres des albums et les noms des artistes correspondants (INNER JOIN)
3. Sélectionner les noms et prénoms des clients associés aux noms et prénoms des employés responsables du service (INNER JOIN)
4. Sélectionner les titres des chansons associées au genre (INNER JOIN)
5. Sélectionner les titres des Chansons, des albums et les noms des artistes associés (INNER JOIN)
6. Sélectionner les noms des playlists et les titres des chansons associées (INNER JOIN)
7. Sélectionner les noms et prénoms des clients qui ont acheté des chansons du genre « Metal » (INNER JOIN et sous-requête)
8. Sélectionner les noms des artistes et les types de média (CROSS JOIN)
9. Sélectionner les noms des chansons et les genres musicaux (CROSS JOIN)
10. Sélectionner les titres des albums et les types de média (CROSS JOIN)
11. Sélectionner les noms des playlists, les titres des chansons et les types de médias (CROSS JOIN)
12. Sélectionner les titres des chansons et les genres musicaux (CROSS JOIN)
13. Sélectionner les genres musicaux et le nombre de chansons de chaque genre (LEFT JOIN)
14. Sélectionner les genres musicaux et le nombre de chansons de chaque genre qui ont été achetées, par ordre décroissant (LEFT JOIN)
15. Sélectionner les noms, prénoms et les ventes totales par clients (LEFT JOIN)
16. Sélectionner les prénoms des employés et de leurs subordonnés directs (LEFT JOIN)
17. Sélectionner les noms des artistes et le nombre d'album par artistes  (LEFT JOIN)
18. Sélectionner les noms des artistes et les titres albums associés (RIGHT JOIN)
19. Sélectionner les noms et prénoms des clients et les identifiants des factures associées (RIGHT JOIN)
20. Sélectionner les genres musicaux et les chansons associées (RIGHT JOIN)
21. Sélectionner les genres musicaux et la somme des achats par genre (RIGHT JOIN)
22. Sélectionner les informations sur les factures avec les lignes de factures associées (FULL JOIN) 
23. Sélectionner les noms et prénoms des employés et de leurs subordonnés (FULL JOIN) 
24. Sélectionner les noms et prénoms des clients et les factures associées (FULL JOIN) 
25. Sélectionner les artistes et les albums associés (FULL JOIN) 
26. Sélectionner les factures avec leurs lignes de factures et les chansons correspondantes (FULL JOIN) 
27. Sélectionner les noms et prénoms des employés et leur manager associé (SELF JOIN)
28. Sélectionner les noms et prénoms des clients ayant le même prénom (SELF JOIN)
29. Sélectionner les identifiants et les titres des albums partageant le même artiste (SELF JOIN)
30. Sélectionner les identifiants et les titres des chansons partageant la même durée (SELF JOIN)
31. Sélectionner les identifiants des factures et des lignes de factures associées (NATURAL JOIN)
32. Sélectionner les albums avec leurs genres (NATURAL JOIN)
33. Sélectionner les noms et prénoms des clients et les identifiants des factures associées (NATURAL JOIN)
34. Sélectionner les noms des artistes et les titres de leurs albums (NATURAL JOIN)
35. Sélectionner les identifiants des factures et des lignes de factures ainsi que les titres des chansons correspondantes (NATURAL JOIN)


### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée