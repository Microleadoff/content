## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

Les retours à la ligne sont faits pour une meilleure lisibilité

1. Sélectionner le nombre d'acteurs par nom de famille
```sql
SELECT `last_name`, COUNT(*) 
FROM `actor` 
GROUP BY `last_name`;
```
 
2. Sélectionner la moyenne de durée des films par prix de locations
```sql
SELECT `rental_rate`, AVG(`length`) 
FROM `film` 
GROUP BY `rental_rate`;
```
 
3. Sélectionner le nombre de films par catégorie
```sql
SELECT `category_id`, COUNT(*) 
FROM `film_category` 
GROUP BY `category_id`;
```
 
4. Sélectionner le nombre de locations par client
```sql
SELECT `customer_id`, COUNT(*) 
FROM `rental` 
GROUP BY `customer_id`;
```
 
5. Sélectionner la durée maximum et minimum de location des films par prix de locations
```sql
SELECT `rental_rate`, MAX(`rental_duration`), MIN(`rental_duration`) 
FROM `film` 
GROUP BY `rental_rate`;
```
 
6. Sélectionner le nombre d'acteurs par nom de famille avec un résumé général
```sql
SELECT `last_name`, COUNT(*) 
FROM `actor` 
GROUP BY `last_name` WITH ROLLUP;
```
 
7. Sélectionner le nombre de films par catégorie avec un résumé général
```sql
SELECT `category_id`, COUNT(*) 
FROM `film_category` 
GROUP BY `category_id` WITH ROLLUP;
```
 
8. Sélectionner la moyenne de durée des films par prix de locations avec un résumé général
```sql
SELECT `rental_rate`, AVG(`length`) 
FROM `film` 
GROUP BY `rental_rate` WITH ROLLUP;
```
 
9. Sélectionner le nombre de films par acteur avec un résumé général
```sql
SELECT `actor_id`, COUNT(*) 
FROM `film_actor` 
GROUP BY `actor_id` WITH ROLLUP;
```
 
10. Sélectionner la durée moyenne de location par prix de location avec un résumé général
```sql
SELECT `rental_rate`, AVG(`rental_duration`) 
FROM `film` 
GROUP BY `rental_rate` WITH ROLLUP;
```
 
11. Sélectionner le nombre de locations par client pour les clients ayant un total de plus de 80 locations
```sql
SELECT `customer_id`, COUNT(*) 
FROM `rental` 
GROUP BY `customer_id` 
HAVING COUNT(*) > 80;
```
 
12. Sélectionner le nombre de films par acteur pour les acteurs ayant plus de 40 films
```sql
SELECT `actor_id`, COUNT(*) 
FROM `film_actor` 
GROUP BY `actor_id` 
HAVING COUNT(*) > 40;
```
 
13. Sélectionner le nombre de paiements par employé pour ceux ayant encaissé plus de 200 paiements
```sql
SELECT `staff_id`, COUNT(*) 
FROM `payment` 
GROUP BY `staff_id` 
HAVING COUNT(*) > 700;
```
 
14. Sélectionner la moyenne des montants des factures par client pour les clients ayant une moyenne de facture supérieure à 50$
```sql
SELECT `customer_id`, AVG(`amount`) 
FROM `payment` 
GROUP BY `customer_id` 
HAVING AVG(`amount`) > 50;
```
 
15. Sélectionner la durée moyenne de location par durée de film pour les films de 1h à 3h
```sql
SELECT `length`, AVG(`rental_duration`) 
FROM `film` 
GROUP BY `length` 
HAVING `length` BETWEEN 120 AND 180;
```
 
16. Sélectionner le montant total des paiements par client pour les clients ayant effectué plus de 100 locations
```sql
SELECT `customer_id`, SUM(`amount`) 
FROM `payment` 
GROUP BY `customer_id` 
HAVING COUNT(`rental_id`) > 100;
```
 
17. Sélectionner la moyenne du prix de location par durée de location pour celles ayant une durée supérieure à 4 jours
```sql
SELECT `rental_duration`, AVG(`rental_rate`) 
FROM `film` 
GROUP BY `rental_duration` 
HAVING `rental_duration` > 4;
```
 
18. Sélectionner les acteurs par ordre alphabétique de noms et de prénoms
```sql
SELECT * 
FROM `actor` 
ORDER BY `last_name`, `first_name`;
```
 
19. Sélectionner les films avec un taux de location supérieur à 4.99$, ordonnés par titre
```sql
SELECT * FROM `film` 
WHERE `rental_rate` = 4.99 
ORDER BY `title`;
```
 
20. Sélectionner le nombre de films par catégories, ordonnés par nombre de films décroissant
```sql
SELECT `category_id`, COUNT(*) 
FROM `film_category` 
GROUP BY `category_id` 
ORDER BY `film_count` DESC;
```
 
21. Sélectionner les paiements supérieurs à 50$ effectués après le 2020-01-01, ordonnés par montant décroissant
```sql
SELECT * 
FROM `payment` 
WHERE `amount` > 50 
AND `payment_date` > '2020-01-01' 
ORDER BY `amount` DESC;
```
 
22. Sélectionner les acteurs ayant joué dans plus de 40 films ordonnés par nombre de films décroissant
```sql
SELECT `actor_id`, COUNT(*) AS `film_count` 
FROM `film_actor` 
GROUP BY `actor_id` 
HAVING `film_count` > 40 
ORDER BY `film_count` DESC;
```

23. Sélectionner les prénoms des acteurs distincts en utilisant l’alias « Prénom »
```sql
SELECT DISTINCT `first_name` AS `Prénom` 
FROM `actor`;
```

24. Sélectionner les identifiants des adresses dont le code est NULL, utiliser des alias
```sql
SELECT `address_id` AS `Adresse ID` 
FROM `address` 
WHERE `postal_code` IS NULL;
```
 
25. Sélectionner les paiements effectués après 2020, avec un montant supérieur à 90$, utiliser des alias
```sql
SELECT `payment_id` AS `ID paiement`, `amount` AS `Montant` 
FROM `payment` 
WHERE `payment_date` > '2020-01-01' 
AND `amount` > 90;
```
 
26. Sélectionner les clients ayant retourné les films et le nombre de locations s’ils en ont effectué plus de 80, utiliser des alias
```sql
SELECT `customer_id` AS `ID client`, COUNT(*) AS `Nombre de commandes` 
FROM `rental` 
WHERE `return_date` IS NOT NULL 
GROUP BY `customer_id` 
HAVING COUNT(*) > 80;
```
 
27. Sélectionner les 10 premières adresses
```sql
SELECT * 
FROM `address` 
LIMIT 10;
```
 
28. Sélectionner les 10 premiers films
```sql
SELECT * 
FROM `film` 
LIMIT 10;
```
 
29. Sélectionner les 10 films à partir de la 5ème
```sql
SELECT * 
FROM `film` 
LIMIT 10 OFFSET 5; (ou LIMIT 5, 10)
```
 
30. Sélectionner les 10 premiers acteurs par ordre alphabétique inversé des noms, utiliser des alias
```sql
SELECT `actor_id` AS `ID acteur`, `first_name` AS `Prénom`, `last_name` AS `Nom` 
FROM `actor` 
ORDER BY `last_name` DESC 
LIMIT 10;
```
 
31. Sélectionner 5 acteurs à partir du 5ème par ordre alphabétique inversé des noms
```sql
SELECT `actor_id` , `first_name` , `last_name` 
FROM `actor` 
ORDER BY `last_name` DESC 
LIMIT 5, 5 ; (ou LIMIT 5 OFFSET 5)
```

32. Sélectionner les 10 premiers films par durée décroissante, utiliser des alias
```sql
SELECT `film_id` AS `ID film`, `title` AS `Titre`, `length` AS `Durée` 
FROM `film` 
ORDER BY `length` DESC 
LIMIT 10;
```
 
33. Sélectionner les films par durée et afficher les catégories : durée inférieure à 120 = « Moins de 2 heures » sinon = « Plus de 2 heures »
```sql
SELECT `title`, `length`,
CASE
    WHEN `length` < 120 THEN 'Moins de 2 heures'
    ELSE 'Plus de 2 heures'
END
FROM `film`
ORDER BY `length`;
```

34. Sélectionner le nombre de film par genre et afficher les catégories : supérieur à 50 = « Élevé », supérieur ou égal à 20 = « Correct » sinon « Faible », utiliser des alias
```sql
SELECT `category_id` AS `ID catégorie`, COUNT(*) AS `Nombre de film`,
CASE
    WHEN COUNT(*) > 50 THEN 'Élevé'
    WHEN COUNT(*) >= 20 THEN 'Correct'
    ELSE 'Faible'
END AS `Film par Genre`
FROM `film_category`
GROUP BY `category_id`;
```
 
35. Sélectionner la somme des paiements pour chaque année et chaque mois et attribuer une catégorie selon le chiffre d'affaires mensuel : supérieur à 45$ = « Élevé », supérieur ou égal à 35$ = « Moyen » sinon « Faible », utiliser des alias
```sql
SELECT YEAR(`payment_date`) AS `Annee`, MONTH(`payment_date`) AS `Mois`, SUM(`amount`) AS `CA`,
CASE
    WHEN SUM(`amount`) > 10000 THEN 'Élevé'
    WHEN SUM(`amount`) >= 5000 THEN 'Moyen'
    ELSE 'Faible'
END AS `Categorie`
FROM `payment`
GROUP BY `Annee`, `Mois`;
```