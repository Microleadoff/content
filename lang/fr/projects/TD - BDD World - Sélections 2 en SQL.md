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
6. Calculer la somme des latitudes et des longitudes par region_id ainsi que la somme de chaque
7. Calculer la moyenne des latitudes et des longitudes par country_id ainsi que la moyenne en tout
8. Calculer les latitudes et longitudes minimales de chaque ville ainsi que la valeur minimale globale
9. Calculer la moyenne des "fips_code" par pays et renvoyer également le total des moyennes
10. [KO] Calculer la somme des latitudes et longitudes avec un total général
11. Calculer la moyenne de la latitude par État ayant une moyenne supérieure à 40
12. Calculer la moyenne de la longitude par État ayant une moyenne supérieure à -100
13. Calculer la moyenne de la latitude par pays ayant une moyenne supérieure à 35
14. Calculer la moyenne de la longitude par pays ayant une moyenne supérieure à -90
15. Calculer la moyenne de la latitude et longitude avec une moyenne supérieure à 0
16. Sélectionner les noms des continents dans l'ordre décroissant
17. Sélectionner tous les pays qui ont une latitude supérieure à 20 dans l'ordre croissant
18. Sélectionner les Etats dans lequel le mot "Region" apparait par ordre croissant
19. [KO] Sélectionner les noms des produits et leurs prix unitaires, triés par prix décroissant, puis par date d'ajout au catalogue
20. [KO] Sélectionner les noms des produits et leurs prix unitaires, triés par prix décroissant, puis par quantité en stock
21. Sélectionner les noms des États et des codes d'État en renommant les colonnes "nom_de_l_etat" et "code_de_l_etat"
22. Sélectionner les noms des pays et des codes de pays en renommant les colonnes "nom_du_pays" et "code_du_pays"
23. Sélectionner les latitudes et longitudes des villes en renommant les colonnes "latitude_de_la_ville" et "longitude_de_la_ville"
24. Sélectionner les dates de création et de mise à jour des enregistrements en renommant les colonnes "date_de_creation" et "date_de_mise_a_jour"
25. Sélectionner les indicateurs de drapeau et les identifiants WikiData en renommant les colonnes "indicateur_de_drapeau" et "identifiant_WikiData"
26. Sélectionner les 10 premières lignes de la table des villes
27. Sélectionner les 10 villes avec les latitudes les plus élevées
28. Sélectionner les 10 villes avec les longitudes les plus basses
29. Sélectionner les 10 villes dans l'état ayant l'id 123
30. Sélectionner les 10 villes dans le pays ayant un id inférieur à 456
31. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" (si la latitue est supérieure à 50, alors vous devrez retourner "Élevée", si elle est supérieure à 40 retournez "Modérée")
32. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" (si la latitude est supérieure à 60, retournez "Très élevée", si elle est supérieure à 50, alors vous devrez retourner "Élevée", si elle est supérieure à 40 retournez "Modérée")
33. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" (si la latitude est supérieure à 45, alors vous devrez retourner "Élevée", si elle est supérieure à 35 retournez "Modérée")
34. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" (si la latitude est supérieure à 47, retournez "Très élevée", si elle est supérieure à 42, alors vous devrez retourner "Élevée", si elle est supérieure à 37 retournez "Modérée")
35. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" (si la latitude est supérieure à 55, retournez "Très élevée", si elle est supérieure à 50, alors vous devrez retourner "Élevée", si elle est supérieure à 45 retournez "Modérée")

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée