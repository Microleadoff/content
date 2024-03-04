## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développé un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Chinook" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Sélectionner le nombre de chansons par genre musical
2. Sélectionner le montant moyen des factures par pays
3. Sélectionner le nombre d’employés par ville
4. Sélectionner le nombre et le montant total des factures par pays 
5. Sélectionner le nombre de chansons par artistes
6. Sélectionner le montant total des factures par pays pour les pays commençant par « C » ou « S »
7. Sélectionner le nombre de chansons par genre musical avec un résumé général
8. Sélectionner le nombre et le montant moyen des factures par pays avec un résumé général
9. Sélectionner le nombre d’employés par ville avec un résumé général
10. Sélectionner le montant total des factures par pays avec un résumé général
11. Sélectionner le nombre d'employés par titre pour les titres « Sales Support Agent » ou « IT Manager » avec un résumé général
12. Sélectionner le nombre de chansons par genre musical si elles sont plus de 30
13. Sélectionner le nombre et le montant total des factures par pays ayant un montant total supérieur à 100$
14. Sélectionner le nombre d’employés par ville ayant plus d’un employé par ville
15. Sélectionner le nombre et la moyenne du montant total des factures par pays ayant plus de 50 factures et dont la moyenne du montant est supérieure à 5$
16. Sélectionner les pays : « USA », « Canada », « France » et le nombre de clients par pays en ayant plus de 5
17. Sélectionner les identifiants des clients ayant un montant total d'achats supérieur à 50$
18. Sélectionner tous les employés ordonnés par noms
19. Sélectionner les chansons dont l’artiste/compositeur n’est pas null, ordonnées par artiste et par nom
20. Sélectionner les prénoms, noms et pays des clients ordonné par pays et par nom
21. Sélectionner le nombre de factures par pays ayant total supérieur à 15$ ordonné par nombre de factures
22. Sélectionner le nombre de chansons par album, ordonné par nombre de chansons décroissant
23. Sélectionner les identifiants et les noms des artistes, utiliser des alias
24. Sélectionner le nombre de chansons par genre musical, utiliser des alias
25. Sélectionner les genres avec plus de 10 chansons et un prix unitaire moyen supérieur à 1$, utiliser des alias
26. Sélectionner le montant total des factures par pays entre les années 2000 et 2010, avec un résumé général, pour les pays ayant un montant total des factures supérieur à 25$, utiliser des alias
27. Sélectionner les 10 premières factures
28. Sélectionner les 10 factures à partir de la 5ème
29. Sélectionner les 10 titres des chansons à partir de la 5ème par ordre alphabétique inversé, utiliser des alias
30. Sélectionner les 10 premiers ID de facture, pays et montant total pour les factures des États-Unis 
31. Sélectionner les 5 premiers genres musicaux ayant le plus grand nombre de chansons, utiliser des alias
32. Sélectionner les 10 premiers pays avec nombre le plus élevé de factures, le montant maximum et minimum total, pour les pays ayant entre 5 et 20 factures
33. Sélectionner la liste des chansons triées par durée et afficher les catégories : inférieur à 1800 millisecondes = « Moins de 3 min » sinon = « Plus de 3 minutes »
34. Sélectionner les genres musicaux et afficher les catégories en fonction du nombre de chanson : supérieur à 50 = « Élevé », supérieur ou égal à 20 = « Correct » sinon « Faible », utiliser des alias
35. Sélectionner la somme des factures pour chaque année et chaque mois et attribuer une catégorie selon le chiffre d'affaires mensuel : supérieur à 45$ = « Élevé », supérieur ou égal à 35$ = « Moyen » sinon « Faible », utiliser des alias

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée