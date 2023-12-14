## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

1. Sélectionner tous les noms des Artistes
```sql
SELECT `Name` 
FROM `artist`;
```
 
2. Sélectionner tous les Employés
```sql
SELECT * 
FROM `employee`;
```
 
3. Sélectionner toutes les pistes/chansons (tracks) 
```sql
SELECT * 
FROM `track`;
```
 
4. Sélectionner tous les noms des playlists
```sql
SELECT `Name` 
FROM `playlist`;
```
 
5. Sélectionner tous les noms et prénoms des clients
```sql
SELECT `LastName`, `FirstName` 
FROM `customer`;
```
 
6. Sélectionner toutes les villes distinctes des Employés
```sql
SELECT DISTINCT `city `
FROM `employee`;
```
 
7. Sélectionner tous les noms distincts des playlists
```sql
SELECT DISTINCT `Name `
FROM `playlist`;
```
 
8. Sélectionner tous les prénoms distincts des clients
```sql
SELECT DISTINCT `FirstName` 
FROM `customer`;
```
 
9. Sélectionner tous les compositeurs/artistes distincts des pistes/chansons (tracks) 
```sql
SELECT DISTINCT `composer` 
FROM `track`;
```
 
10. Sélectionner les clients qui vivent en France
```sql
SELECT * 
FROM `customer `
WHERE `country` = 'France';
```
 
11. Sélectionner les pistes/chansons (tracks) du genre Raggae (8)
```sql
SELECT * 
FROM `track` 
WHERE `GenreId` = 8;
```
 
12. Sélectionner les pistes/chansons (tracks) dont le compositeur/artiste est « AC/DC »
```sql
SELECT * 
FROM `track` 
WHERE `composer` = 'AC/DC';
```
 
13. Sélectionner les factures du 01 Juin 2013
```sql
SELECT * 
FROM `invoice` 
WHERE `invoiceDate` = '2013-06-01';
```
 
14. Sélectionner les factures émises au Brésil et dont le total est supérieur à 5$
```sql
SELECT * 
FROM `invoice` 
WHERE `BillingCountry` = 'Brazil' 
AND `Total` > 5;
```
 
15. Sélectionner les pistes de genre Metal (3) et dont le média est du type MPEG audio file (1)
```sql
SELECT * 
FROM `track` 
WHERE `GenreId` = 3 
AND `MediaTypeId` = 1;
```
 
16. Sélectionner les clients qui vivent dans l’État « CA » et dont le prénom est « Frank »
```sql
SELECT * 
FROM `customer` 
WHERE `State` = 'CA' 
AND `FirstName` = 'Frank';
```
 
17. Sélectionner les factures émises en Allemagne ou ayant un total supérieur à 15$
```sql
SELECT * 
FROM `invoice` 
WHERE `BillingCountry` = 'Germany' 
OR `Total` > 15;
```
 
18. Sélectionner les clients qui vivent dans les États « CA » ou « NY »
```sql
SELECT * 
FROM `customer` 
WHERE `State` = 'CA' 
OR `State` = 'NY';
```
 
19. Sélectionner les pistes de genre Rock (1) et dont le média est du type Protected AAC audio file (2) ou AAC audio file (5) en utilisant OR
```sql
SELECT * 
FROM `track` 
WHERE `GenreId` = 1 
AND (
    `MediaTypeId` = 2 
    OR `MediaTypeId` = 5
    );
```
 
20. Sélectionner les noms, prénoms et fonctions des employés qui sont « General Manager » ou « Sales Manager » en utilisant OR
```sql
SELECT `LastName`, `FirstName`, `Title` 
FROM `employee` 
WHERE `Title` = 'General Manager' 
OR `Title` = 'Sales Manager';
```
 
21. Sélectionner les pistes de genre Rock (1) et dont le média est du type Protected AAC audio file (2) ou AAC audio file (5) en utilisant IN
```sql
SELECT * 
FROM `track` 
WHERE `GenreId` = 1 
AND `MediaTypeId` IN(2,5);
```
 
22. Sélectionner les factures émises pour les villes de « Mountain View » ou « Tucson » avec un montant total supérieur à 2$ en utilisant IN
```sql
SELECT * 
FROM `invoice` 
WHERE `BillingCity` IN ('Mountain View', 'Tucson') 
AND `Total` > 2;
```
 
23. Sélectionner les factures émises entre le 1er et le 31 Mars 2010
```sql
SELECT * 
FROM `invoice` 
WHERE `InvoiceDate` BETWEEN '2010-03-01' AND '2010-03-31';
```
 
24. Sélectionner les factures entre 5 et 15$
```sql
SELECT * 
FROM `invoice` 
WHERE `Total` BETWEEN 5 AND 15;
```
 
25. Sélectionner les factures émises pour les USA et la France dont le total est compris entre 5 et 10$
```sql
SELECT * 
FROM `invoice` 
WHERE `BillingCountry` IN('USA', 'France') 
AND `Total` BETWEEN 5 AND 10;
```
 
26. Sélectionner les factures des USA supérieurs à 20$ ou d’Allemagne supérieur à 10$
```sql
SELECT * 
FROM `invoice` 
WHERE (
    `BillingCountry` = 'USA' 
    AND `Total` > 20
    ) 
OR (
    `BillingCountry` = 'Germany' 
    AND `Total` > 10
    );
```
 
27. Sélectionner les pistes dont le nom de l’artiste contient « young »
```sql
SELECT * 
FROM `track` 
WHERE `composer` LIKE '%young%';
```
 
28. Sélectionner les playlists dont le nom commence par un « C »
```sql
SELECT * 
FROM `playlist` 
WHERE `name` LIKE 'C%';
```
 
29. Sélectionner les playlists dont la 2ème lettre du nom est un « u »
```sql
SELECT * 
FROM `playlist` 
WHERE `name` LIKE '_u%';
```
 
30. Sélectionner les factures de Juin 2009
```sql
SELECT * 
FROM `invoice` 
WHERE `InvoiceDate` LIKE '2009-06%';
```
 
31. Sélectionner les factures émises aux USA en 2009
```sql
SELECT * 
FROM `invoice` 
WHERE `BillingCountry` = 'USA' 
AND `InvoiceDate` LIKE '2009%';
```
 
32. Sélectionner les factures émises pour la France ou, émises en 2009 dont le total est compris entre 15 et 20$
```sql
SELECT * 
FROM `invoice` 
WHERE `BillingCountry` = 'USA' 
AND `InvoiceDate` LIKE '2009%';
```
 
33. Sélectionner les pistes pour lesquelles le compositeur/artiste est null
```sql
SELECT * 
FROM `track` 
WHERE `composer` IS NULL;
```
 
34. Sélectionner les factures dont le code postal est NULL
```sql
SELECT * 
FROM `invoice` 
WHERE `BillingPostalCode` IS NULL;
```
 
35. Sélectionner les factures dont le code postal est NULL mais pas l’État
```sql
SELECT * 
FROM `invoice` 
WHERE `BillingPostalCode` IS NULL 
AND `BillingState` IS NOT NULL;
```