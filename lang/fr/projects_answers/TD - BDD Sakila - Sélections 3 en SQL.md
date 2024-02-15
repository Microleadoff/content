## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

Les retours à la ligne sont faits pour une meilleure lisibilité
      
1. Sélectionner les prénoms distincts des employés et des clients sans doublon
```sql
SELECT DISTINCT `first_name` 
FROM `staff`  
UNION 
SELECT DISTINCT `first_name` 
FROM `customer`;
```
       
2. Sélectionner les identifiants des films associés à des acteurs et à des catégories sans doublon
```sql
SELECT `film_id` 
FROM `film_actor` 
UNION 
SELECT `film_id` 
FROM `film_category`;
```
       
3. Sélectionner les identifiants d’adresse des employés et des clients sans doublon
```sql
SELECT `address_id` 
FROM `staff` 
UNION 
SELECT `address_id` 
FROM `customer`;
```
       
4. Sélectionner les identifiants des clients et des employés pour les paiements et les retours de locations effectués entre le 1er et le 2 Janvier 2021 ordonné par identifiant client et employé sans doublon
```sql
SELECT `customer_id`, `staff_id` 
FROM `payment` 
WHERE `payment_date` BETWEEN '2021-01-01' AND '2021-01-02' 
UNION 
SELECT `customer_id`, `staff_id` 
FROM `rental`  
WHERE `return_date` BETWEEN '2021-01-01' AND '2021-01-02' 
ORDER BY `customer_id`, `staff_id`;
```
       
5. Sélectionner les identifiants des employés ayant reçu des paiements et eu des retours de location pour les identifi	ants de location commençant par « 28 » sans doublon
```sql
SELECT `staff_id` 
FROM `payment` 
WHERE `rental_id` LIKE '28%' 
UNION 
SELECT `staff_id` 
FROM `rental` 
WHERE `rental_id` LIKE '28%' 
ORDER BY `staff_id`;
```
       
6. Sélectionner les prénoms distincts des employés et des clients avec possibles doublons
```sql
SELECT DISTINCT `first_name` 
FROM `staff`  
UNION ALL 
SELECT DISTINCT `first_name` 
FROM `customer`;
```
       
7. Sélectionner les identifiants des films associés à des acteurs et à des catégories avec possibles doublons
```sql
SELECT `film_id` 
FROM `film_actor` 
UNION ALL 
SELECT `film_id` 
FROM `film_category`;
```
       
8. Sélectionner les identifiants d’adresse des employés et des clients avec possibles doublons
```sql
SELECT `address_id` 
FROM `staff` 
UNION ALL 
SELECT `address_id` 
FROM `customer`;
```
       
9. Sélectionner les identifiants des clients et des employés pour les paiements et les retours de locations effectués entre le 1er et le 2 Janvier 2021 ordonné par identifiant client et employé avec possibles doublons
```sql
SELECT `customer_id`, `staff_id` 
FROM `payment` 
WHERE `payment_date` BETWEEN '2021-01-01' AND '2021-01-02' 
UNION ALL 
SELECT `customer_id`, `staff_id` 
FROM `rental` 
WHERE `return_date` BETWEEN '2021-01-01' AND '2021-01-02' 
ORDER BY `customer_id`, `staff_id`;
```
       
10. Sélectionner les identifiants des employés ayant reçu des paiements et eu des retours de location pour les identifiants de location commençant par « 28 » avec possibles doublons
```sql
SELECT `staff_id` 
FROM `payment` 
WHERE `rental_id` LIKE '28%' 
UNION ALL 
SELECT `staff_id` 
FROM `rental` 
WHERE `rental_id` LIKE '28%' 
ORDER BY `staff_id`;
```
       
11. Sélectionner les clients qui ont effectué un retour en Juin 2010 (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT * 
FROM `customer` 
WHERE `customer_id` IN (
    SELECT `customer_id` 
    FROM `rental` 
    WHERE `return_date` LIKE '2010-06%'
    );
```
       
12. Sélectionner les prénoms et les noms des acteurs dont le prénom est aussi dans ceux des clients (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT `first_name`, `last_name`
FROM `actor`
WHERE `first_name` IN (
    SELECT `first_name`
    FROM `customer`
);
```
       
13. Sélectionner les clients qui ont effectué un paiement entre le 1er et le 5 Janvier 2010 (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT * 
FROM `customer` 
WHERE `Customer_id` IN ( 
    SELECT `Customer_id` 
    FROM `payment` 
    WHERE `payment_date` BETWEEN '2010-01-01' AND '2010-01-05'
    );
```
       
14. Sélectionner les adresses qui se trouvent à la fois dans la table des adresses et dans la table des villes (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT `address`
FROM `address`
WHERE `city_id` IN (
    SELECT `city_id`
    FROM `city`
);
```
       
15. Sélectionner les clients qui ont une somme totale de factures supérieure à 50$ (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT * 
FROM `customer` 
WHERE `customer_id` IN (
    SELECT `customer_id` 
    FROM `payment` 
    GROUP BY `customer_id` 
    HAVING SUM(`amount`) > 50
    );
```
       
16. Sélectionner les prénoms distincts des clients à l’exception de ceux étant également présents dans les employés (EXCEPT)
```sql
SELECT DISTINCT `first_name` 
FROM `customer` 
EXCEPT 
SELECT DISTINCT `first_name` 
FROM `staff`;
```
       
17. Sélectionner les identifiants des clients à l’exception de ceux ayant fait un retour de location en 2010 (EXCEPT)
```sql
SELECT `customer_id` 
FROM `customer` 
EXCEPT  
SELECT DISTINCT `customer_id` 
FROM `rental` 
WHERE `return_date` LIKE '2010%';
```

18. Sélectionner les identifiants des clients à l’exception de ceux ayant effectué un paiement entre le 1er Janvier et le 31 Décembre 2010 (EXCEPT)
```sql
SELECT `customer_id` 
FROM `customer` 
EXCEPT  
SELECT DISTINCT `customer_id` 
FROM `payment` 
WHERE `payment_date` BETWEEN '2010-01-01' AND '2010-12-31';
```
       
19. Sélectionner les identifiants des films à l’exception de ceux qui ont été loués entre le 1er Janvier 2020 et le 31 Décembre 2022 (EXCEPT)
```sql
SELECT `film_id` 
FROM `film` 
EXCEPT 
SELECT DISTINCT `inventory_id` 
FROM `rental` 
WHERE `rental_date` BETWEEN '2020-01-01' AND '2022-12-31';
```
       
20. Sélectionner les identifiants des adresses des clients à l’exception de ceux également présents pour les employés (EXCEPT)
```sql
SELECT `address_id` 
FROM `customer` 
EXCEPT 
SELECT `address_id` FROM `staff`;
```