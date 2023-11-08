## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développer un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "World" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :


1. Sélectionner le nombre de villes par État
2. Sélectionner le nombre de villes par code d'État
3. Sélectionner le nombre de villes par pays
4. Sélectionner le nombre de villes par code de pays
5. Sélectionner le nombre de villes par drapeau (flag)
6. Calculer la somme des latitudes par État avec un total général
7. Calculer la somme des longitudes par État avec un total général
8. Calculer la somme des latitudes par pays avec un total général
9. Calculer la somme des longitudes par pays avec un total général
10. Calculer la somme des latitudes et longitudes avec un total général
11. Calculer la moyenne de la latitude par État ayant une moyenne supérieure à 40
12. Calculer la moyenne de la longitude par État ayant une moyenne supérieure à -100
13. Calculer la moyenne de la latitude par pays ayant une moyenne supérieure à 35
14. Calculer la moyenne de la longitude par pays ayant une moyenne supérieure à -90
15. Calculer la moyenne de la latitude et longitude avec une moyenne supérieure à 0
16. Sélectionner les noms des produits et leurs prix unitaires, triés par prix décroissant
17. Sélectionner les noms des produits et leurs prix unitaires, triés par prix décroissant, puis par nom de produit
18. Sélectionner les noms des produits et leurs prix unitaires, triés par prix décroissant, puis par catégorie de produit
19. Sélectionner les noms des produits et leurs prix unitaires, triés par prix décroissant, puis par date d'ajout au catalogue
20. Sélectionner les noms des produits et leurs prix unitaires, triés par prix décroissant, puis par quantité en stock
21. Sélectionner les noms des États et des codes d'État en renommant les colonnes "nom_de_l_etat" et "code_de_l_etat"
22. Sélectionner les noms des pays et des codes de pays en renommant les colonnes "nom_du_pays" et "code_du_pays"
23. Sélectionner les latitudes et longitudes des villes en renommant les colonnes "latitude_de_la_ville" et "longitude_de_la_ville"
24. Sélectionner les dates de création et de mise à jour des enregistrements en renommant les colonnes "date_de_creation" et "date_de_mise_a_jour"
25. Sélectionner les indicateurs de drapeau et les identifiants WikiData en renommant les colonnes "indicateur_de_drapeau" et "identifiant_WikiData"
26. Sélectionner les 10 premières lignes de la table des villes
27. Sélectionner les 10 villes avec les latitudes les plus élevées
28. Sélectionner les 10 villes avec les longitudes les plus basses
29. Sélectionner les 10 villes dans l'état ayant l'id 123
30. Sélectionner les 10 villes dans le pays ayant l'id 456
31. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN"
32. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN"
33. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN"
34. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN"
35. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN"

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée