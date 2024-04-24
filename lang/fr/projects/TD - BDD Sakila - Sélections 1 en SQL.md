## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développé un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Sakila" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Sélectionner toutes les adresses 
2. Sélectionner tous les noms et prénoms des acteurs
3. Sélectionner toutes les locations
5. Sélectionner tous les noms et prénoms des clients
6. Sélectionner les codes postaux distincts des adresses
7. Sélectionner les années distinctes de sortie des films
8. Sélectionner les identifiants clients distincts des locations
9. Sélectionner les coûts de remplacements distincts des films
10. Sélectionner les durées de locations distinctes des films
11. Sélectionner les employés dont le nom est « Johnson »
12. Sélectionner les paiements supérieurs à 95$
13. Sélectionner les identifiants de clients distincts qui ont des paiements supérieurs à 95$
14. Sélectionner les paiements du client ayant l’identifiant 15
15. Sélectionner les acteurs ayant joué dans le film qui porte l’identifiant 100
16. Sélectionner les paiements inférieurs à 25$ du client ayant l’identifiant 15
17. Sélectionner les films dont la durée est supérieure à 120 min et le coût de remplacement inférieur à 25$
18. Sélectionner les employés actifs du magasin 2
19. Sélectionner les paiements du client numéro 10 ou de l’employé numéro 10
20. Sélectionner les films loués 6 jours ou plus ou ceux qui ont une durée supérieure à 180 min
21. Sélectionner les films d’une durée supérieure à 180 min avec une note « PG » ou supérieure à 160 min avec une note « PG-13 »
22. Sélectionner les acteurs qui ont comme nom « Allen » ou « Bening » en utilisant IN
23. Sélectionner les films de catégories numéros 6 et 11
24. Sélectionner les films de 90 et 120 min
25. Sélectionner les paiements effectués entre le 1er et le 31 Janvier 2010
26. Sélectionner les films avec une note entre « PG-13 » et « R »
27. Sélectionner les paiements entre 5 et 20$ encaissés par l’employé numéro 18
28. Sélectionner les films dont le titre contient « love »
29. Sélectionner les acteurs dont le nom commence par « S » ou « T »
30. Sélectionner les clients dont le nom contient « ARD » à partir de la 2ème lettre
31. Sélectionner les paiements de 5, 10 et 15$ effectués en 2012
32. Sélectionner les clients inactifs ou dont le nom commence par un « S »
33. Sélectionner les employés inactifs dont le nom commence par un « R » ou par un « B »
34. Sélectionner les adresses qui ont un code postal NULL
35. Sélectionner les adresses qui ont un code postal NULL et dont l’identifiant de la ville est 300 



### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée