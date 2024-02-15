## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

1. Sélectionner le nombre de chansons par genre musical
```sql
SELECT `GenreId`, COUNT(*) 
FROM `track` 
GROUP BY `GenreId`;
```
 
2. Sélectionner le montant moyen des factures par pays
```sql
SELECT `BillingCountry`, AVG(`Total`) 
FROM `invoice` 
GROUP BY `BillingCountry`;
```
 
3. Sélectionner le nombre d’employés par ville
```sql
SELECT `City`, COUNT(*) 
FROM `employee` 
GROUP BY `City`;
```
 
4. Sélectionner le nombre et le montant total des factures par pays 
```sql
SELECT `BillingCountry`, COUNT(*), SUM(`Total`) 
FROM `invoice` 
GROUP BY `BillingCountry`;
```
 
5. Sélectionner le nombre de chansons par artistes
```sql
SELECT `ArtistId`, COUNT(*) 
FROM `album` 
GROUP BY `ArtistId`;
```
 
6. Sélectionner le montant total des factures par pays pour les pays commençant par « C » ou « S »
```sql
SELECT `BillingCountry`, SUM(`Total`) 
FROM `invoice` 
WHERE `BillingCountry` LIKE 'C%' 
OR `BillingCountry` LIKE 'S%' 
GROUP BY `BillingCountry`;
```
 
7. Sélectionner le nombre de chansons par genre musical avec un résumé général
```sql
SELECT `GenreId`, COUNT(*) 
FROM `track` 
GROUP BY `GenreId` WITH ROLLUP;
```
 
8. Sélectionner le nombre et le montant moyen des factures par pays avec un résumé général
```sql
SELECT `BillingCountry`, COUNT(*), AVG(`Total`) 
FROM `invoice` 
GROUP BY `BillingCountry` WITH ROLLUP;
```
 
9. Sélectionner le nombre d’employés par ville avec un résumé général
```sql
SELECT `City`, COUNT(*) 
FROM `employee` 
GROUP BY `City` WITH ROLLUP;
```
 
10. Sélectionner le montant total des factures par pays avec un résumé général
```sql
SELECT `BillingCountry`, SUM(`Total`) 
FROM `invoice` 
GROUP BY `BillingCountry` WITH ROLLUP;
```
 
11. Sélectionner le nombre d'employés par titre pour les titres « Sales Support Agent » ou « IT Manager » avec un résumé général
```sql
SELECT `Title`, COUNT(`EmployeeId`) 
FROM `employee` 
WHERE `Title` IN ('Sales Support Agent', 'IT Manager') 
GROUP BY `Title` WITH ROLLUP;
```

12. Sélectionner le nombre de chansons par genre musical si elles sont plus de 30
```sql
SELECT `GenreId`, COUNT(*) 
FROM `track` 
GROUP BY `GenreId` 
HAVING COUNT(*) > 30;
```
 
13. Sélectionner le nombre et le montant total des factures par pays ayant un montant total supérieur à 100$
```sql
SELECT `BillingCountry`, COUNT(*), SUM(`Total`) 
FROM `invoice` 
GROUP BY `BillingCountry` 
HAVING SUM(Total) > 100;
```
 
14. Sélectionner le nombre d’employés par ville ayant plus d’un employé par ville
```sql
SELECT `City`, COUNT(*) 
FROM `employee` 
GROUP BY `City` 
HAVING COUNT(*) > 1;
```
 
15. Sélectionner le nombre et la moyenne du montant total des factures par pays ayant plus de 50 factures et dont la moyenne du montant est supérieure à 5$
```sql
SELECT `BillingCountry`, COUNT(*), AVG(`Total`) 
FROM `invoice` 
GROUP BY `BillingCountry` 
HAVING COUNT(*) > 50 
AND AVG(Total) > 5;
```
 
16. Sélectionner les pays : « USA », « Canada », « France » et le nombre de clients par pays en ayant plus de 5
```sql
SELECT `Country`, COUNT(*) 
FROM `customer` 
WHERE `Country` IN ('USA', 'Canada', 'France') 
GROUP BY `Country` 
HAVING COUNT(*) > 5;
```
 
17. Sélectionner les identifiants des clients ayant un montant total d'achats supérieur à 50$
```sql
SELECT `CustomerId`, SUM(`Total`) 
FROM `invoice` 
GROUP BY `CustomerId` 
HAVING SUM(`Total`) > 40;
```
 
18. Sélectionner tous les employés ordonnés par noms
```sql
SELECT * 
FROM `employee` 
ORDER BY `LastName`;
```
 
19. Sélectionner les chansons dont l’artiste/compositeur n’est pas null, ordonnées par artiste et par nom
```sql
SELECT * 
FROM `track` 
WHERE `Composer` IS NOT NULL 
ORDER BY `Composer`, `Name`;
```
 
20. Sélectionner les prénoms, noms et pays des clients ordonné par pays et par nom
```sql
SELECT `FirstName`, `LastName`, `Country` 
FROM `customer` 
ORDER BY `Country`, `LastName`;
```
 
21. Sélectionner le nombre de factures par pays ayant total supérieur à 15$ ordonné par nombre de factures
```sql
SELECT `BillingCountry`, COUNT(*) 
FROM `invoice` 
WHERE `Total` > 15 
GROUP BY `BillingCountry` 
ORDER BY COUNT(*) DESC;
```
 
22. Sélectionner le nombre de chansons par album, ordonné par nombre de chansons décroissant
```sql
SELECT `AlbumId`, COUNT(*) 
FROM `track` 
GROUP BY `AlbumId` 
ORDER BY COUNT(*) DESC;
```

23. Sélectionner les identifiants et les noms des artistes, utiliser des alias
```sql
SELECT `ArtistId` AS `ID` , `Name` AS `Artiste` 
FROM `artist`;
```
 
24. Sélectionner le nombre de chansons par genre musical, utiliser des alias
```sql
SELECT `GenreId`, COUNT(*) AS `Nombre de chansons` 
FROM `track` 
GROUP BY `GenreId`;
```
 
25. Sélectionner les genres avec plus de 10 chansons et un prix unitaire moyen supérieur à 1$, utiliser des alias
```sql
SELECT `GenreId`, COUNT(*) AS `Nombre de chansons` , AVG(`UnitPrice`) AS `Prix moyen` 
FROM `track` 
GROUP BY `GenreId` 
HAVING COUNT(*) > 10 
AND AVG(`UnitPrice`) > 1;
```
 
26. Sélectionner le montant total des factures par pays entre les années 2000 et 2010, avec un résumé général, pour les pays ayant un montant total des factures supérieur à 25$, utiliser des alias
```sql
SELECT `BillingCountry` AS `Pays` , SUM(`Total`) AS `Montant total` 
FROM `invoice` 
WHERE YEAR(`InvoiceDate`) BETWEEN 2000 AND 2010 
GROUP BY `BillingCountry` WITH ROLLUP 
HAVING SUM(`Total`) > 25;
```
 
27. Sélectionner les 10 premières factures
```sql
SELECT * 
FROM `invoice` 
LIMIT 10;
```
 
28. Sélectionner les 10 factures à partir de la 5ème
```sql
SELECT * 
FROM `invoice` 
LIMIT 10 OFFSET 5;  (ou : LIMIT 5, 10)
```

29. Sélectionner les 10 titres des chansons à partir de la 5ème par ordre alphabétique inversé, utiliser des alias
```sql
SELECT `Name` AS `Titre` 
FROM `track` 
ORDER BY `Name` DESC 
LIMIT 5, 10; (ou : LIMIT 10 OFFSET 5)
```
 
30. Sélectionner les 10 premiers ID de facture, pays et montant total pour les factures des États-Unis 
```sql
SELECT `InvoiceId`, `BillingCountry`, `Total` 
FROM `invoice` 
WHERE `BillingCountry` = 'USA' 
LIMIT 10;
```
 
31. Sélectionner les 5 premiers genres musicaux ayant le plus grand nombre de chansons, utiliser des alias
```sql
SELECT `GenreId`, COUNT(*) AS 'Nombre de chansons' 
FROM `track` 
GROUP BY `GenreId` 
ORDER BY 'Nombre de chansons' DESC 
LIMIT 5;
```

32. Sélectionner les 10 premiers pays avec nombre le plus élevé de factures, le montant maximum et minimum total, pour les pays ayant entre 5 et 20 factures
```sql
SELECT `BillingCountry`, MAX(`Total`), MIN(`Total`) 
FROM `invoice` 
GROUP BY `BillingCountry` 
HAVING COUNT(`InvoiceId`) BETWEEN 5 AND 20 
ORDER BY COUNT(`InvoiceId`) DESC 
LIMIT 10;
```
 
33. Sélectionner la liste des chansons triées par durée et afficher les catégories : inférieur à 1800 millisecondes = « Moins de 3 min » sinon = « Plus de 3 minutes »
```sql
SELECT `Name`, `Milliseconds`,
CASE
    WHEN `Milliseconds` < 180000 THEN 'Moins de 3 min'
    ELSE 'Plus de 3 min'
END
FROM `track`
ORDER BY `Milliseconds`;
```
 
34. Sélectionner les genres musicaux et afficher les catégories en fonction du nombre de chanson : supérieur à 50 = « Élevé », supérieur ou égal à 20 = « Correct » sinon « Faible », utiliser des alias
```sql
SELECT `GenreId`, COUNT(*) AS `Nombre de chansons`,
CASE
    WHEN COUNT(*) > 50 THEN 'Élevé'
    WHEN COUNT(*) >= 20 THEN 'Correct'
    ELSE 'Faible'
END AS `Nombre de chansons par Genre`
FROM `track`
GROUP BY `GenreId`;
```
 
35. Sélectionner la somme des factures pour chaque année et chaque mois et attribuer une catégorie selon le chiffre d'affaires mensuel : supérieur à 45$ = « Élevé », supérieur ou égal à 35$ = « Moyen » sinon « Faible », utiliser des alias
```sql
SELECT YEAR(`InvoiceDate`) AS `Année`, MONTH(`InvoiceDate`) AS `Mois`, SUM(`Total`) AS `CA`,
CASE
    WHEN SUM(`Total`) > 45 THEN 'Élevé'
    WHEN SUM(`Total`) >= 35 THEN 'Moyen'
    ELSE 'Faible'
END AS `Catégorie`
FROM `invoice`
GROUP BY YEAR(`InvoiceDate`), MONTH(`InvoiceDate`);
```