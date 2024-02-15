## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre


1. Sélectionner titres de films et les identifiants d'acteurs auxquels ils sont associés (INNER JOIN)
```sql
SELECT `f`.`title`, `fa`.`actor_id` 
FROM `film` AS `f` 
INNER JOIN `film_actor` AS `fa` ON `f`.`film_id` = `fa`.`film_id`;
```
       
2. Sélectionner les noms et prénoms distincts des clients ayant effectué des paiements (INNER JOIN)
```sql
SELECT DISTINCT `c`.`last_name`, `c`.`first_name` 
FROM `customer` AS `c` 
INNER JOIN `payment` AS `p` ON `c`.`customer_id` = `p`.`customer_id`;
```
       
3. Sélectionner les noms des catégories et les titres des films associés (INNER JOIN)
```sql
SELECT `c`.`name` AS `Categorie`, `f`.`title` 
FROM `category` AS `c` 
INNER JOIN `film_category` AS `fc` ON `c`.`category_id` = `fc`.`category_id` 
INNER JOIN `film` AS `f` ON `fc`.`film_id` = `f`.`film_id`;
```
       
4. Sélectionner les titres des films, les noms et prénoms des acteurs qui ont joué dans ces films (INNER JOIN)
```sql
SELECT `f`.`title`, `a`.`last_name`, `a`.`first_name`  
FROM `film` AS `f` 
INNER JOIN `film_actor` AS `fa` ON `f`.`film_id` = `fa`.`film_id` 
INNER JOIN `actor` AS `a` ON `fa`.`actor_id` = `a`.`actor_id`;
```
       
5. Sélectionner les titres des films et les montants des paiements associés à leurs locations (INNER JOIN)
```sql
SELECT `f`.`title`, `p`.`amount` 
FROM `film` AS `f` 
INNER JOIN `inventory` AS `i` ON `f`.`film_id` = `i`.`film_id` 
INNER JOIN `rental` AS `r` ON `i`.`inventory_id` = `r`.`inventory_id` 
INNER JOIN `payment` AS `p` ON `r`.`rental_id` = `p`.`rental_id`;
```
       
6. Sélectionner les noms et prénoms des clients ayant effectué des paiements pour des films de la catégorie « Action » (INNER JOIN et sous-requête)
```sql
SELECT `c`.`last_name`, `c`.`first_name` 
FROM `customer` AS `c` 
INNER JOIN `payment` AS `p` ON `c`.`customer_id` = `p`.`customer_id` 
WHERE `p`.`rental_id` IN (
    SELECT `r`.`rental_id` 
    FROM `rental` AS `r` 
    INNER JOIN `inventory` AS `i` ON `r`.`inventory_id` = `i`.`inventory_id` 
    INNER JOIN `film` AS `f` ON `i`.`film_id` = `f`.`film_id` 
    INNER JOIN `film_category` AS `fc` ON `f`.`film_id` = `fc`.`film_id` 
    INNER JOIN `category` AS `cat` ON `fc`.`category_id` = `cat`.`category_id` 
    WHERE `cat`.`name` = 'Action');
```
       
7. Sélectionner  les titres des films et les langues (CROSS JOIN)
```sql
SELECT `f`.`title`, `l`.`name` AS `Langue` 
FROM `film` AS `f` 
CROSS JOIN `language` AS `l`;
```
       
8. Sélectionner les noms et prénoms des clients et les adresses (CROSS JOIN)
```sql
SELECT `c`.`last_name`, `c`.`first_name`, `ad`.`address` 
FROM `customer` AS `c` 
CROSS JOIN `address` AS `ad`;
```
       
9. Sélectionner les noms et prénoms des acteurs et les films (CROSS JOIN)
```sql
SELECT `a`.`last_name`, `a`.`first_name`, `f`.`title` 
FROM `actor` AS `a` 
CROSS JOIN `film` AS `f`;
```
       
10. Sélectionner les noms des catégories et les titres des films (CROSS JOIN)
```sql
SELECT `cat`.`name` AS `Categorie`, `f`.`title` 
FROM `category` AS `cat` 
CROSS JOIN `film` AS `f`;
```
       
11. Sélectionner les noms et prénoms des clients, les adresses et les noms des villes (CROSS JOIN)
```sql
SELECT `c`.`last_name`, `c`.`first_name`, `ad`.`address`, `ci`.`city` 
FROM `customer` AS `c` 
CROSS JOIN `address` AS `ad` 
JOIN `city` AS `ci` ON `ad`.`city_id` = `ci`.`city_id`;
```
       
12. Sélectionner les titres des films et les langues auxquelles ils sont associés (LEFT JOIN)
```sql
SELECT `f`.`title`, `l`.`name` AS `Langue` 
FROM `film` AS `f` 
LEFT JOIN `language` AS `l` ON `f`.`language_id` = `l`.`language_id`;
```
       
13. Sélectionner les noms et prénoms des clients et les montants de paiement auxquels ils sont associés (LEFT JOIN)
```sql
SELECT `c`.`last_name`, `c`.`first_name`, `p`.`amount` 
FROM `customer` AS `c` 
LEFT JOIN `payment` AS `p` ON `c`.`customer_id` = `p`.`customer_id`;
```
       
14. Sélectionner les titres des films et les noms et prénoms des acteurs auxquels ils sont associés (LEFT JOIN)
```sql
SELECT `f`.`title`,`a`.`last_name`, `a`.`first_name`  
FROM `film` AS `f` 
LEFT JOIN `film_actor` AS `fa` ON `f`.`film_id` = `fa`.`film_id` 
LEFT JOIN `actor` AS `a` ON `fa`.`actor_id` = `a`.`actor_id`;
```
       
15. Sélectionner les noms et prénoms des clients et les adresses auxquelles ils sont associés (LEFT JOIN)
```sql
SELECT `c`.`last_name`, `c`.`first_name`, `a`.`address` 
FROM `customer` AS `c` 
LEFT JOIN `address` AS `a` ON `c`.`address_id` = `a`.`address_id`;
```

16. Sélectionner les titres des films et les catégories associées (LEFT JOIN)
```sql
SELECT `f`.`title`, `c`.`name` AS `Categorie` 
FROM `film` AS `f` 
LEFT JOIN `film_category` AS `fc` ON `f`.`film_id` = `fc`.`film_id` 
LEFT JOIN `category` AS `c` ON `fc`.`category_id` = `c`.`category_id`;
```
       
17. Sélectionner les identifiants, titres des films et les catégories associées (RIGHT JOIN)
```sql
SELECT `fc`.`film_id`, `c`.`name` 
FROM `film_category` AS `fc` 
RIGHT JOIN `category` AS `c` ON `fc`.`category_id` = `c`.`category_id`;
```
       
18. Sélectionner les identifiants des adresses et les noms des villes auxquels ils sont associés (RIGHT JOIN)
```sql
SELECT `a`.`address_id`, `c`.`city` 
FROM `address` AS `a` 
RIGHT JOIN `city` AS `c` ON `a`.`city_id` = `c`.`city_id`;
```
       
19. Sélectionner les identifiants des clients et les montants de paiement auxquels ils sont associés (RIGHT JOIN)
```sql
SELECT `p`.`customer_id`, `p`.`amount` 
FROM `payment` AS `p` 
RIGHT JOIN `customer` AS `c` ON `c`.`customer_id` = `p`.`customer_id`;
```
       
20. Sélectionner les identifiants des pays et les noms des villes auxquelles ils sont associés (RIGHT JOIN)
```sql
SELECT `co`.`country_id`, `ci`.`city` 
FROM `country` AS `co` 
RIGHT JOIN `city` AS `ci` ON `co`.`country_id` = `ci`.`country_id`;
```
       
21. Sélectionner les noms et prénoms des acteurs et les films associés (FULL JOIN)
```sql
SELECT `a`.`first_name`, `a`.`last_name`, `f`.`title` 
FROM `actor` AS `a` 
FULL JOIN `film_actor` AS `fa` ON `a`.`actor_id` = `fa`.`actor_id` 
FULL JOIN `film` AS `f` ON `fa`.`film_id` = `f`.`film_id`;
```

VERSION MySQL Workbench :
```sql
SELECT `a`.`first_name`, `a`.`last_name`, `f`.`title` 
FROM `actor` AS `a` 
LEFT JOIN `film_actor` AS `fa` ON `a`.`actor_id` = `fa`.`actor_id` 
LEFT JOIN `film` AS `f` ON `fa`.`film_id` = `f`.`film_id` 
UNION 
SELECT `a`.`first_name`, `a`.`last_name`, `f`.`title` 
FROM `actor` AS `a` 
RIGHT JOIN `film_actor` AS `fa` ON `a`.`actor_id` = `fa`.`actor_id` 
RIGHT JOIN `film` AS `f` ON `fa`.`film_id` = `f`.`film_id`;
```
       
22. Sélectionner les catégories de films et les films associés (FULL JOIN)
```sql
SELECT `c`.`name` AS `Categorie`, `f`.`title` 
FROM `category` AS `c` 
FULL JOIN `film_category` AS `fc` ON `c`.`category_id` = `fc`.`category_id` 
FULL JOIN `film` AS `f` ON `fc`.`film_id` = `f`.`film_id`;
```

VERSION MySQL Workbench :
```sql
SELECT `c`.`name` AS `Categorie`, `f`.`title` 
FROM `category` AS `c` 
LEFT JOIN `film_category` AS `fc` ON `c`.`category_id` = `fc`.`category_id` 
LEFT JOIN `film` AS `f` ON `fc`.`film_id` = `f`.`film_id` 
UNION 
SELECT `c`.`name` AS `Categorie`, `f`.`title` 
FROM `category` AS `c` 
RIGHT JOIN `film_category` AS `fc` ON `c`.`category_id` = `fc`.`category_id` 
RIGHT JOIN `film` AS `f` ON `fc`.`film_id` = `f`.`film_id`;
```
       
23. Sélectionner les paiements et les dates de locations associées (FULL JOIN)
```sql
SELECT `p`.`amount`, `r`.`rental_date`, `r`.`return_date` 
FROM `payment` AS `p` 
FULL JOIN `rental` AS `r` ON `p`.`rental_id` = `r`.`rental_id`;
```

VERSION MySQL Workbench :
```sql
SELECT `p`.`amount`, `r`.`rental_date`, `r`.`return_date` 
FROM `payment` AS `p` 
LEFT JOIN `rental` AS `r` ON `p`.`rental_id` = `r`.`rental_id` 
UNION 
SELECT `p`.`amount`, `r`.`rental_date`, `r`.`return_date` 
FROM `payment` AS `p` 
RIGHT JOIN `rental` AS `r` ON `p`.`rental_id` = `r`.`rental_id`;
```
       
24. Sélectionner les ventes et les noms et prénoms des clients associés (FULL JOIN)
```sql
SELECT `p`.`payment_id`, `c`.`last_name`, `c`.`first_name`  
FROM `payment` AS `p` 
FULL JOIN `customer` AS `c` ON `p`.`customer_id` = `c`.`customer_id`;
```

VERSION MySQL Workbench :
```sql
SELECT `p`.`payment_id`, `c`.`last_name`, `c`.`first_name` 
FROM `payment` AS `p` 
LEFT JOIN `customer` AS `c` ON `p`.`customer_id` = `c`.`customer_id` 
UNION 
SELECT `p`.`payment_id`, `c`.`last_name`, `c`.`first_name` 
FROM `payment` AS `p` 
RIGHT JOIN `customer` AS `c` ON `p`.`customer_id` = `c`.`customer_id`;
```
       
25. Sélectionner les ventes et les noms et prénoms des employés associés (FULL JOIN)
```sql
SELECT `p`.`payment_id`, `s`.`last_name`, `s`.`first_name` 
FROM `payment` AS `p` 
FULL JOIN `staff` AS `s` ON `p`.`staff_id` = `s`.`staff_id`;
```

VERSION MySQL Workbench :
```sql
SELECT `p`.`payment_id`, `s`.`last_name`, `s`.`first_name` 
FROM `payment` AS `p` 
LEFT JOIN `staff` AS `s` ON `p`.`staff_id` = `s`.`staff_id` 
UNION 
SELECT `p`.`payment_id`, `s`.`last_name`, `s`.`first_name` 
FROM `payment` AS `p` 
RIGHT JOIN `staff` AS `s` ON `p`.`staff_id` = `s`.`staff_id`;
```
       
26. Sélectionner les noms et prénoms des acteurs ayant le même nom que d'autres acteurs (SELF JOIN)
```sql
SELECT `a1`.`first_name`, `a1`.`last_name`, `a2`.`first_name` AS `prénom acteur 2`
FROM `actor` AS `a1` 
INNER JOIN `actor` AS `a2` ON `a1`.`last_name` = `a2`.`last_name` 
AND `a1`.`actor_id` <> `a2`.`actor_id`;
```
       
27. Sélectionner adresses partageant la même ville (SELF JOIN)
```sql
SELECT `a1`.`address`, `a1`.`city_id`, `a2`.`address` AS `adresse 2` 
FROM `address` AS `a1` 
INNER JOIN `address` AS `a2` ON `a1`.`city_id` = `a2`.`city_id` 
AND `a1`.`address_id` <> `a2`.`address_id`;
```
       
28. Sélectionner les noms et prénoms des clients qui ont un prénom identique et fréquente le même magasin (SELF JOIN)
```sql
SELECT `c1`.`first_name`, `c1`.`last_name`, `c2`.`first_name` AS `prénom client 2`, `c1`.`store_id` 
FROM `customer` AS `c1` 
INNER JOIN `customer` AS `c2` ON `c1`.`first_name` = `c2`.`first_name` 
AND `c1`.`customer_id` <> `c2`.`customer_id` 
AND `c1`.`store_id` = `c2`.`store_id`;
```
       
29. Sélectionner les films qui ont des acteurs communs (SELF JOIN)
```sql
SELECT `fa1`.`film_id`, `fa1`.`actor_id`, `fa2`.`film_id` AS `film 2` 
FROM `film_actor` AS `fa1` 
INNER JOIN `film_actor` AS `fa2` ON `fa1`.`actor_id` = `fa2`.`actor_id` 
AND `fa1`.`film_id` <> `fa2`.`film_id`;
```

30. Sélectionner les villes ayant le même pays (SELF JOIN)
```sql
SELECT `c1`.`city_id`, `c2`.`city_id` AS `ville 2` 
FROM `city` AS `c1` 
INNER JOIN `city` AS `c2` ON `c1`.`country_id` = `c2`.`country_id` 
AND `c1`.`city_id` <> `c2`.`city_id`;
```