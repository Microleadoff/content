## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

1. Sélectionner tous les Pays
```sql
SELECT * 
FROM `countries`;
```
 
2. Sélectionner tous les Pays par leur nom et leur code iso3
```sql
SELECT `name`, `iso3` 
FROM `countries`;
```
 
3. Sélectionner les monnaies distinctes des pays 
```sql
SELECT DISTINCT `currency` 
FROM `countries`;
```
 
4. Sélectionner les monnaies et les symboles des monnaies distinctes des pays 
```sql 
SELECT DISTINCT `currency`, `currency_symbol` 
FROM `countries`;
```
 
5. Sélectionner les nom des villes et le code pays dont le code pays est « AO » 
```sql
SELECT `name`, `country_code` 
FROM `cities` 
WHERE `country_code` = 'AO';
```

6. Sélectionner les villes dont le code pays est « AO» et le code d'État « HUI»
```sql
SELECT * 
FROM `cities` 
WHERE `country_code` = 'AO' 
AND `state_code` = 'HUI';
```
 
7. Sélectionner les villes et le code pays dont le code pays est « AO » ou « AZ » en utilisant « OR »
```sql
SELECT * 
FROM `cities` 
WHERE `country_code` = 'AO' 
OR `country_code` = 'AZ';
```
 
8. Sélectionner les villes et le code pays dont le code pays est « AO » ou « AZ » en utilisant « IN »
```sql
SELECT * 
FROM `cities` 
WHERE `country_code` IN ('AO', 'AZ');
```
 
9. Sélectionner les villes dont le code pays est « AO» et le code d’État « HUI» ou « MOX » en utilisant « OR »
```sql
SELECT * 
FROM `cities` 
WHERE `country_code` = 'AO' 
AND (
    `state_code` = 'HUI' 
    OR `state_code` = 'MOX'
    );
```
 
10. Sélectionner les villes dont le code pays est « AO» et le code d’État « HUI» ou « MOX » en utilisant « IN »
```sql
SELECT * 
FROM `cities` 
WHERE `country_code` = 'AO' 
AND `state_code` IN ('HUI', 'MOX');
```
 
11. Sélectionner les pays dont le code numérique est compris entre 50 et 100 
```sql
SELECT * 
FROM `countries` 
WHERE `numeric_code` BETWEEN 50 AND 100;
```
 
12. Sélectionner les pays dont le la monnaie est « USD » et le code numérique est compris entre 50 et 100
```sql
SELECT * 
FROM `countries` 
WHERE `currency` = 'USD' 
AND `numeric_code` BETWEEN 50 AND 100;
```
 
13. Sélectionner les villes dont le code pays est « AO » et, le code d’État est « BIE» ou la longitude est comprise entre 13 et 14
```sql
SELECT * 
FROM `cities` 
WHERE `country_code` = 'AO' 
AND (
    `state_code` = 'BIE' 
    OR `longitude` BETWEEN 13 AND 14
    );
```
 
14. Sélectionner les villes dont le code pays est « AO » ou, le code d’État est « BIE» ou « HUI » et la longitude est comprise entre 13 et 14
```sql
SELECT * 
FROM `cities` 
WHERE `country_code` = 'AO' 
OR (
    `state_code` IN ('BIE', 'HUI') 
    AND `longitude` BETWEEN 13 AND 14
    );
```
	
15. Sélectionner les pays dont le nom commence par un « C»
```sql
SELECT * 
FROM `countries` 
WHERE `name` LIKE 'C%';
```
 
16. Sélectionner les pays dont la monnaie est « EUR » et la deuxième lettre du nom est un « A »
```sql
SELECT * 
FROM `countries` 
WHERE `currency` = 'EUR' 
AND `name` LIKE '_A%';
```
 
17. Sélectionner les pays dont la monnaie est « EUR » et la deuxième lettre du nom est un « A » ou le code numérique est compris entre 200 et 300
```sql
SELECT * 
FROM `countries` 
WHERE `currency` = 'EUR' 
AND (
    `name` LIKE 'A%' 
    OR `numeric_code` BETWEEN 200 AND 300
    );
```
 
18. Sélectionner les pays dont le nom commence et termine par un « A» 
```sql
SELECT * 
FROM `countries` 
WHERE `name` LIKE 'A%A' ;
```
 
19. Sélectionner les pays dont le nom commence par un « A» et la 3ème lettre est un « G »
```sql
SELECT * 
FROM `countries` 
WHERE `name` LIKE 'A_G%' ;
```
 
20. Sélectionner les pays dont le nom commence par un « F» , la 3ème lettre est un « E» et la monnaie est « EUR » 
```sql
SELECT * 
FROM `countries` 
WHERE `name` LIKE 'F_E%' 
AND `currency` = 'EUR';
```
 
21. Sélectionner les pays dont le nom contient « ENC »
```sql
SELECT * 
FROM `countries` 
WHERE `name` LIKE '%ENC%';
```
 
22. Sélectionner les pays dont la monnaie est « USD » ou dont le code numérique est compris entre 300 et 500 et, le nom contient « NE »
```sql
SELECT * 
FROM `countries` 
WHERE `name` LIKE '%NE%' 
AND (
    `currency` = 'USD' 
    OR `numeric_code` BETWEEN 300 AND 500
    );
```
 
23. Sélectionner les pays dont l’avant-dernière lettre est un « E »
```sql
SELECT * 
FROM `countries` 
WHERE `name` LIKE '%E_';
```
 
24. Sélectionner les pays dont l’avant-dernière lettre du nom est un « E », la monnaie est « EUR » et le code numérique est compris entre 0 et 300
```sql
SELECT * 
FROM `countries` 
WHERE `name` LIKE '%E_' 
AND `currency` = 'EUR' 
AND `numeric_code` BETWEEN 0 AND 300;
```
 
25. Sélectionner les villes dont le code pays est « AD» ou « AE » et le nom se termine par « A» ou dont la latitude est comprise entre 40 et 50 
```sql
SELECT * 
FROM `cities` 
WHERE `country_code` IN ('AD', 'AE') 
AND (
    `name` LIKE '%A' 
    OR `latitude` BETWEEN 40 AND 50
    );
```

26. Sélectionner les pays pour lesquels l’id région est null
```sql
SELECT * 
FROM `countries` 
WHERE `region_id` IS NULL;
```