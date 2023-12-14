## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

1. Sélectionner toutes les adresses 
```sql
SELECT * 
FROM `address`;
```
 
2. Sélectionner tous les noms et prénoms des acteurs
```sql
SELECT `last_name`, `first_name` 
FROM `actor`;
```
 
3. Sélectionner toutes les locations
```sql
SELECT * 
FROM `rental`;
```
 
5. Sélectionner tous les noms et prénoms des clients
```sql
SELECT `last_name`, `first_name` 
FROM `customer`;
```
 
6. Sélectionner les codes postaux distincts des adresses
```sql
SELECT DISTINCT `postal_code` 
FROM `address`;
```
 
7. Sélectionner les années distinctes de sortie des films
```sql
SELECT DISTINCT `release_year` 
FROM `film`;
```
 
8. Sélectionner les identifiants clients distincts des locations
```sql
SELECT DISTINCT `customer_id` 
FROM `rental`;
```
 
9. Sélectionner les coûts de remplacements distincts des films
```sql
SELECT DISTINCT `replacement_cost` 
FROM `film`;
```
 
10. Sélectionner les durées de locations distinctes des films
```sql
SELECT DISTINCT `rental_duration` 
FROM `film`;
```
 
11. Sélectionner les employés dont le nom est « Johnson »
```sql
SELECT * 
FROM `staff` 
WHERE `last_name` = 'Johnson';
```
 
12. Sélectionner les paiements supérieurs à 95$
```sql
SELECT * 
FROM `payment` 
WHERE `amount` > 95;
```
 
13. Sélectionner les identifiants de clients distincts qui ont des paiements supérieurs à 95$
```sql
SELECT DISTINCT `customer_id` 
FROM `payment` 
WHERE `amount` > 95;
```
 
14. Sélectionner les paiements du client ayant l’identifiant 15
```sql
SELECT * 
FROM `payment` 
WHERE `customer_id` = 15;
```
 
15. Sélectionner les acteurs ayant joué dans le film qui porte l’identifiant 100
```sql
SELECT * 
FROM `film_actor` 
WHERE `film_id` = 100;
```
 
16. Sélectionner les paiements inférieurs à 25$ du client ayant l’identifiant 15
```sql
SELECT * 
FROM `payment` 
WHERE `customer_id` = 15 
AND `amount` < 25;
```
 
17. Sélectionner les films dont la durée est supérieure à 120 min et le coût de remplacement inférieur à 25$
```sql
SELECT * 
FROM `film` 
WHERE length > 120 
AND `replacement_cost` < 25;
```
 
18. Sélectionner les employés actifs du magasin 2
```sql
SELECT * 
FROM `staff` 
WHERE `active` = 1 
AND `store_id` = 2;
```
 
19. Sélectionner les paiements du client numéro 10 ou de l’employé numéro 10
```sql
SELECT * 
FROM `payment` 
WHERE `staff_id` = 10 
OR `customer_id` = 10;
```
 
20. Sélectionner les films loués 6 jours ou plus ou ceux qui ont une durée supérieure à 180 min
```sql
SELECT * 
FROM `film` 
WHERE `rental_duration` >= 6 
OR `length` > 180;
```
 
21. Sélectionner les films d’une durée supérieure à 180 min avec une note « PG » ou supérieure à 160 min avec une note « PG-13 »
```sql
SELECT * 
FROM `film` 
WHERE (
    `length` > 180 
    AND rating = 'PG'
    ) 
OR (
    `length` > 160 
    AND rating = 'PG-13'
    );
```
 
22. Sélectionner les acteurs qui ont comme nom « Allen » ou « Bening » en utilisant IN
```sql
SELECT * 
FROM `actor` 
WHERE `last_name` IN ('Allen', 'Bening');
```
 
23. Sélectionner les films de catégories numéros 6 et 11
```sql
SELECT * 
FROM `film_category` 
WHERE `category_id` IN (6, 11);
```
 
24. Sélectionner les films de 90 et 120 min
```sql
SELECT * 
FROM `film` 
WHERE `length` IN (90, 120);
```
 
25. Sélectionner les paiements effectués entre le 1er et le 31 Janvier 2010
```sql
SELECT * 
FROM `payment` 
WHERE `payment_date` BETWEEN '2010-01-01' AND '2010-01-31';
```
 
26. Sélectionner les films avec une note entre « PG-13 » et « R »
```sql
SELECT * 
FROM `film` 
WHERE `rating` BETWEEN 'PG-13' AND 'R';
```
 
27. Sélectionner les paiements entre 5 et 20$ encaissés par l’employé numéro 18
```sql
SELECT * 
FROM `payment` 
WHERE `staff_id` = 18 
AND `amount` BETWEEN 5 AND 20 ;
```
 
28. Sélectionner les films dont le titre contient « love »
```sql
SELECT * 
FROM `film` 
WHERE `title` LIKE '%love%';
```
 
29. Sélectionner les acteurs dont le nom commence par « S » ou « T »
```sql
SELECT * 
FROM `actor` 
WHERE `last_name` LIKE 'S%' 
OR `last_name` LIKE 'T%';
```
 
30. Sélectionner les clients dont le nom contient « ARD » à partir de la 2ème lettre
```sql
SELECT * 
FROM `customer` 
WHERE `last_name` LIKE '_ARD%'
```
 
31. Sélectionner les paiements de 5, 10 et 15$ effectués en 2012
```sql
SELECT * 
FROM `payment` 
WHERE `amount` IN (5, 10, 15) 
AND `payment_date` LIKE '2012%';
```
 
32. Sélectionner les clients inactifs ou dont le nom commence par un « S »
```sql
SELECT * 
FROM `customer` 
WHERE `active` = 0 
OR `last_name` LIKE 'S%';
```
 
33. Sélectionner les employés inactifs dont le nom commence par un « R » ou par un « B »
```sql
SELECT * 
FROM `staff` 
WHERE `active` = 0 
AND (`last_name` LIKE 'R%' OR `last_name` LIKE 'B%');
```
 
34. Sélectionner les adresses qui ont un code postal NULL
```sql
SELECT * 
FROM `address` 
WHERE `postal_code` IS NULL;
```
 
35. Sélectionner les adresses qui ont un code postal NULL et dont l’identifiant de la ville est 300
```sql
SELECT * 
FROM `address` 
WHERE `postal_code` IS NULL 
AND `city_id` = 300;
```
 