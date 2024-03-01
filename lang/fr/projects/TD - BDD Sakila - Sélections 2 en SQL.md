## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développé un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Sakila" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Sélectionner le nombre d'acteurs par nom de famille
2. Sélectionner la moyenne de durée des films par prix de locations
3. Sélectionner le nombre de films par catégorie
4. Sélectionner le nombre de locations par client
5. Sélectionner la durée maximum et minimum de location des films par prix de locations
6. Sélectionner le nombre d'acteurs par nom de famille avec un résumé général
7. Sélectionner le nombre de films par catégorie avec un résumé général
8. Sélectionner la moyenne de durée des films par prix de locations avec un résumé général
9. Sélectionner le nombre de films par acteur avec un résumé général
10. Sélectionner la durée moyenne de location par prix de location avec un résumé général
11. Sélectionner le nombre de locations par client pour les clients ayant un total de plus de 80 locations
12. Sélectionner le nombre de films par acteur pour les acteurs ayant plus de 40 films
13. Sélectionner le nombre de paiements par employé pour ceux ayant encaissé plus de 200 paiements
14. Sélectionner la moyenne des montants des factures par client pour les clients ayant une moyenne de facture supérieure à 50$
15. Sélectionner la durée moyenne de location par durée de film pour les films de 1h à 3h
16. Sélectionner le montant total des paiements par client pour les clients ayant effectué plus de 100 locations
17. Sélectionner la moyenne du prix de location par durée de location pour celles ayant une durée supérieure à 4 jours
18. Sélectionner les acteurs par ordre alphabétique de noms et de prénoms
19. Sélectionner les films avec un taux de location supérieur à 4.99$, ordonnés par titre
20. Sélectionner le nombre de films par catégories, ordonnés par nombre de films décroissant
21. Sélectionner les paiements supérieurs à 50$ effectués après le 2020-01-01, ordonnés par montant décroissant
22. Sélectionner les acteurs ayant joué dans plus de 40 films ordonnés par nombre de films décroissant
23. Sélectionner les prénoms des acteurs distincts en utilisant l’alias « Prénom »
24. Sélectionner les identifiants des adresses dont le code est NULL, utiliser des alias
25. Sélectionner les paiements effectués après 2020, avec un montant supérieur à 90$, utiliser des alias
26. Sélectionner les clients ayant retourné les films et le nombre de locations s’ils en ont effectué plus de 80, utiliser des alias
27. Sélectionner les 10 premières adresses
28. Sélectionner les 10 premiers films
29. Sélectionner les 10 films à partir de la 5ème
30. Sélectionner les 10 premiers acteurs par ordre alphabétique inversé des noms, utiliser des alias
31. Sélectionner 5 acteurs à partir du 5ème par ordre alphabétique inversé des noms
32. Sélectionner les 10 premiers films par durée décroissante, utiliser des alias
33. Sélectionner les films par durée et afficher les catégories : durée inférieure à 120 = « Moins de 2 heures » sinon = « Plus de 2 heures »
34. Sélectionner le nombre de film par genre et afficher les catégories : supérieur à 50 = « Élevé », supérieur ou égal à 20 = « Correct » sinon « Faible », utiliser des alias
35. Sélectionner la somme des paiements pour chaque année et chaque mois et attribuer une catégorie selon le chiffre d'affaires mensuel : supérieur à 45$ = « Élevé », supérieur ou égal à 35$ = « Moyen » sinon « Faible », utiliser des alias

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée