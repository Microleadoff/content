## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre


1. Sélectionner les noms des acteurs ayant joué dans plus de 35 films, utiliser des alias pour les résultats et les appels des tables 
```sql
SELECT `a`.`first_name` AS `Prénom de l'acteur`, `a`.`last_name` AS `Nom de l'acteur` 
FROM `actor` AS `a` 
WHERE `a`.`actor_id` IN (
    SELECT `fa`.`actor_id` 
    FROM `film_actor` AS `fa` 
    GROUP BY `fa`.`actor_id` 
    HAVING COUNT(*) > 35
    );
```
       
2. Sélectionner les noms des catégories de films ayant moins de 60 films associés, utiliser des alias pour les résultats et les appels des tables
```sql
SELECT `c`.`name` AS `Nom de la catégorie` 
FROM `category` AS `c` 
WHERE `c`.`category_id` IN (
    SELECT `fc`.`category_id` 
    FROM `film_category` AS `fc` 
    GROUP BY `fc`.`category_id` 
    HAVING COUNT(*) < 60
    );
```
       
3. Sélectionner les noms et prénoms des clients dont le montant total des paiements est supérieur à 3500$, utiliser des alias
```sql
SELECT `c`.`first_name` AS `Prénom du client`, `c`.`last_name` AS `Nom du client` 
FROM `customer` AS c 
WHERE `c`.`customer_id` IN (
    SELECT `p`.`customer_id` 
    FROM `payment` AS `p` 
    GROUP BY `p`.`customer_id` 
    HAVING SUM(`p`.`amount`) > 3500
    );
```
       
4. Sélectionner les identifiants, noms et prénoms des clients qui ont effectué plus de 80 locations, utiliser des alias
```sql
SELECT `c`.`customer_id`, `c`.`first_name`, `c`.`last_name` 
FROM `customer` AS `c` 
WHERE `c`.`customer_id` IN (
    SELECT `r`.`customer_id` 
    FROM `rental` AS `r`
    GROUP BY `r`.`customer_id` 
    HAVING COUNT(*) > 80 
    ) 
GROUP BY `c`.`customer_id`;
```
       
5. Sélectionner les titres des films appartenant au genre « Drama », utiliser des alias
```sql
SELECT `f`.`title` AS `Titre du film` 
FROM `film` AS `f` 
WHERE `f`.`film_id` IN (
    SELECT `fc`.`film_id` 
    FROM `film_category` AS `fc` 
    WHERE `fc`.`category_id` IN (
        SELECT `c`.`category_id` 
        FROM `category` AS `c` 
        WHERE `c`.`name` = 'Drama'
        )
    );
```
       
6. Sélectionner le nombre de locations par magasin, utiliser des alias
```sql
SELECT `s`.`store_id` AS `ID du magasin`, ( 
    SELECT COUNT(`r`.`rental_id`) 
    FROM `rental` AS `r` 
    WHERE `r`.`inventory_id` IN(
        SELECT `i`.`inventory_id`
        FROM `inventory` AS `i` 
        WHERE `i`.`store_id` = `s`.`store_id`
        )
    ) AS `Nombre de locations` 
FROM `store` AS `s`;
```
       
7. Sélectionner les acteurs ayant joué dans au moins 1 film, utiliser des alias (EXISTS)
```sql
SELECT `first_name`, `last_name` 
FROM `actor` AS `a` 
WHERE EXISTS (
    SELECT `fa`.`actor_id` 
    FROM `film_actor` AS `fa` 
    WHERE `fa`.`actor_id` = `a`.`actor_id`
    );
```
       
8. Sélectionner les villes n’ayant aucune adresse associée, utiliser des alias (EXISTS)
```sql
SELECT `c`.`city` 
FROM `city` AS `c` 
WHERE NOT EXISTS (
    SELECT `ad`.`city_id` 
    FROM `address` AS `ad` 
    WHERE `ad`.`city_id` = `c`.`city_id`
    );
```
       
9. Sélectionner les catégories qui ont au moins un film associé, utiliser des alias (EXISTS)
```sql
SELECT `c`.`name` 
FROM `category` AS `c` 
WHERE EXISTS (
    SELECT `fc`.`category_id` 
    FROM `film_category` AS `fc` 
    WHERE `fc`.`category_id` = `c`.`category_id`
    );
```
       
10. Sélectionner les clients ayant effectué au moins une location et dont la date de retour est comprise entre le 1er et le 2 Janvier 2021 ordonné par nom (EXISTS)
```sql
SELECT `c`.`last_name`, `c`.`first_name` 
FROM `customer` AS `c` 
WHERE EXISTS (
    SELECT `r`.`customer_id` 
    FROM `rental` AS `r` 
    WHERE `r`.`customer_id` = `c`.`customer_id` 
    AND `r`.`return_date` BETWEEN '2021-01-01' AND '2021-01-02'
    ) 
ORDER BY `c`.`last_name`;
```
       
11. Sélectionner les films ayant au moins une catégorie et dont la durée est supérieure à 180min (EXISTS)
```sql
SELECT `f`.`title` 
FROM `film` AS `f` 
WHERE EXISTS (
    SELECT `fc`.`film_id` 
    FROM `film_category` AS `fc` 
    WHERE `fc`.`film_id` = `f`.`film_id` 
    AND `f`.`length` > 180
    );
```
       
12. Sélectionner les clients dont la date de dernière mise à jour est antérieure ou égale à la plus récente des mises à jour enregistrées pour les adresses (ALL)
```sql
SELECT * 
FROM `customer` 
WHERE `last_update` <= ALL (
    SELECT MAX(`last_update`) 
    FROM `address` 
    GROUP BY `customer_id` 
    );
```
       
13. Sélectionner les acteurs dont le prénom est plus fréquent que tous les autres prénoms (ALL)
```sql
SELECT * 
FROM `actor` 
WHERE `first_name` >= ALL (
    SELECT `first_name` 
    FROM `actor` 
    GROUP BY `first_name` 
    HAVING COUNT(*) >= ALL (
        SELECT COUNT(*) 
        FROM `actor` 
        GROUP BY `first_name`
        )
    );
```
       
14. Sélectionner les identifiants des films ayant le plus grand nombre de locations (ALL)
```sql
SELECT `film_id`  
FROM `inventory` 
GROUP BY `film_id` 
HAVING COUNT(*) >= ALL (
    SELECT COUNT(*) 
    FROM `inventory` 
    GROUP BY `film_id`
    );
```

15. Sélectionner les employés ayant enregistré le plus grand nombre de locations (ALL)
```sql
SELECT `first_name`, `last_name` 
FROM `staff` 
WHERE `staff_id` IN (
    SELECT `staff_id` 
    FROM `rental` 
    GROUP BY `staff_id` 
    HAVING COUNT(*) >= ALL (
        SELECT COUNT(*) 
        FROM `rental` 
        GROUP BY `staff_id`
        )
    );
```
       
16. Sélectionner le prénom et le nom du client ayant le montant total de paiement le plus élevé (ALL)
```sql
SELECT `first_name`, `last_name` 
FROM `customer` 
WHERE `customer_id` = ALL (
    SELECT `customer_id` 
    FROM `payment` 
    GROUP BY `customer_id` 
    HAVING SUM(`amount`) >= ALL (
        SELECT SUM(`amount`) 
        FROM `payment` 
        GROUP BY `customer_id` 
        )
    );
```
       
17. Sélectionner les noms des catégories avec au moins un film ayant une durée supérieure à 3 heures (ANY)
```sql
SELECT `name` 
FROM `category` 
WHERE `category_id` = ANY (
    SELECT `category_id` 
    FROM `film_category` 
    WHERE `film_id` IN (
        SELECT `film_id` 
        FROM `film` 
        WHERE `length` > 180
        )
    );
```
       
18. Sélectionner prénoms des acteurs ayant joué dans au moins un film de la catégorie 5 (« Comedy »), utiliser des alias (ANY)
```sql
SELECT `a`.`first_name` AS `Prénom_de_l_acteur` 
FROM `actor` AS `a` 
WHERE `a`.`actor_id` = ANY (
    SELECT `fa`.`actor_id` 
    FROM `film_actor` AS `fa` 
    WHERE `fa`.`film_id` IN (
        SELECT `fc`.`film_id` 
        FROM `film_category` AS `fc` 
        WHERE `fc`.`category_id` = 5
        )
    );
```
       
19. Sélectionner les noms des langues avec un film avec une durée inférieure à 90 minutes, utiliser des alias (ANY)
```sql
SELECT `l`.`name` AS `Nom_de_la_langue` 
FROM `language` AS `l` 
WHERE `l`.`language_id` = ANY (
    SELECT f.`language_id` 
    FROM `film` AS `f` 
    WHERE `f`.`length` < 90
    );
```
       
20. Sélectionner les adresses avec un client dont le nom commence par la lettre « R » (ANY)
```sql
SELECT `address` 
FROM `address` 
WHERE `address_id` = ANY (
    SELECT `address_id` 
    FROM `customer` 
    WHERE `last_name` LIKE 'R%'
    );
```
       
21. Sélectionner les titres des films dans lesquels un acteur se nomme est « WOOD » (ANY)
```sql
SELECT `title` 
FROM `film` 
WHERE `film_id` = ANY (
    SELECT `film_id` 
    FROM `film_actor` 
    WHERE `actor_id` IN (
        SELECT `actor_id` 
        FROM `actor` 
        WHERE `last_name` = 'WOOD'
        )
    );
```