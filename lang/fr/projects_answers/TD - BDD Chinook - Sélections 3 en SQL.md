## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

1. Sélectionner les identifiants des chansons des lignes de factures et des pistes des playlists sans doublon, utiliser des alias
```sql
SELECT `trackId` AS `Identifiant Chanson` 
FROM `invoiceline` 
UNION 
SELECT `trackId` 
FROM `playlisttrack`;
```
       
2. Sélectionner les pays distincts des clients et des factures sans doublon
```sql
SELECT DISTINCT `Country` 
FROM `customer` 
UNION 
SELECT DISTINCT `BillingCountry` 
FROM `invoice`;
```
       
3. Sélectionner les identifiants et prix unitaire des chansons des lignes de factures et des pistes sans doublon
```sql
SELECT `trackId`, `UnitPrice` 
FROM `invoiceline` 
UNION 
SELECT `trackId`, `UnitPrice` 
FROM `track`;
```

4. Sélectionner les noms des playlists et des albums sans doublon, utiliser des alias
```sql
SELECT `Name` AS `Nom_Playlist` 
FROM `playlist`  
UNION SELECT `Title` 
FROM `album`;
```
       
5. Sélectionner les États et les identifiants clients s’ils ne sont pas null des tables : clients et factures ordonnés par État sans doublon
```sql
SELECT `State`, `CustomerId` 
FROM `customer` 
WHERE `State` IS NOT NULL 
UNION 
SELECT `BillingState`, `CustomerId` 
FROM `invoice` 
WHERE `BillingState` IS NOT NULL 
ORDER BY `State` ASC;
```
       
6. Sélectionner les identifiants des chansons des lignes de factures et des pistes des playlists avec possibles doublons
```sql
SELECT `trackId` 
FROM `invoiceline` 
UNION ALL 
SELECT `trackId` 
FROM `playlisttrack`;
```
       
7. Sélectionner les pays des clients et des factures avec possibles doublons
```sql
SELECT `Country` 
FROM `customer` 
UNION ALL 
SELECT `BillingCountry` 
FROM `invoice`;
```
       
8. Sélectionner les noms des playlists et des albums avec possibles doublons, utiliser des alias
```sql
SELECT `Name` AS `Nom_Playlist` 
FROM `playlist`  
UNION ALL 
SELECT `Title` 
FROM `album`;
```
       
9. Sélectionner les États et les identifiants clients s’ils ne sont pas null des tables : clients et factures ordonnés par État avec possibles doublons
```sql
SELECT `State`, `CustomerId` 
FROM `customer` 
WHERE `State` IS NOT NULL 
UNION ALL 
SELECT `BillingState`, `CustomerId` 
FROM `invoice` 
WHERE `BillingState` IS NOT NULL 
ORDER BY `State` ASC;
```
       
10. Sélectionner les clients qui ont été facturés le 03 Novembre 2013 (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT * 
FROM `customer` 
WHERE `CustomerId` IN ( 
    SELECT `CustomerId` 
    FROM `invoice` 
    WHERE `InvoiceDate` = '2013-11-03' 
    );
```
       
11. Sélectionner les clients qui ont été facturés dans les pays suivants : « USA », « France », « Allemagne » (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT * 
FROM `customer` 
WHERE `CustomerId` IN (
    SELECT `CustomerId` 
    FROM `invoice` 
    WHERE `BillingCountry` 
    IN ('USA', ' France ', 'Germany')
    );
```
       
12. Sélectionner les noms et prénoms des clients résidant dans des pays où le montant total des factures dépasse 100$ (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT `LastName`, `FirstName` 
FROM `customer` 
WHERE `Country` IN (
    SELECT `BillingCountry` 
    FROM `invoice` 
    GROUP BY `BillingCountry` 
    HAVING SUM(`Total`) > 100
    );
```
       
13. Sélectionner le nombre d’album dont le genre est « Rock » (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT `AlbumId`,  COUNT(*) 
FROM `track` 
WHERE `GenreId` IN ( 
    SELECT `GenreId` 
    FROM `genre` 
    WHERE `Name` = 'Rock' 
    ) 
GROUP BY `AlbumId`;
```
       
14. Sélectionner les clients qui ont une somme totale de factures supérieure à 40$ (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT * 
FROM `customer` 
WHERE `CustomerId` IN ( 
    SELECT `CustomerId` 
    FROM `invoice` 
    GROUP BY `CustomerId` 
    HAVING SUM(`Total`) > 40 
    );
```

15. Sélectionner le nombre de fois que chaque chanson (par son nom) a été ajoutée dans une playlist, si elle apparaît plus de 3 fois. Ordonner par nombre décroissant puis par ordre alphabétique de nom, utiliser des alias pour les résultats et pour l’appel des tables (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT `t`.`Name` AS `Nom de la Chanson`, COUNT(*) AS `Nombre d'Ajouts dans les Playlists` 
FROM `track` `t` 
WHERE `t`.`TrackId` IN ( 
    SELECT `TrackId` 
    FROM `playlisttrack` 
    ) 
GROUP BY `t`.`Name` 
HAVING COUNT(*) >= 3 
ORDER BY COUNT(*) DESC, `t`.`Name`;
```
       
16. Sélectionner les villes des clients à l’exception de celles des employés (EXCEPT)
```sql
SELECT DISTINCT `City` 
FROM `customer` 
EXCEPT 
SELECT DISTINCT `City` 
FROM `employee`;
```
       
17. Sélectionner les identifiants des chansons présents dans les playlists à l’exception de ceux présents dans les lignes de factures (EXCEPT)
```sql
SELECT `TrackId` 
FROM `playlisttrack` 
EXCEPT 
SELECT `TrackId` 
FROM `invoiceline`;
```
       
18. Sélectionner les identifiants des clients à l’exception de ceux qui ont une moyenne de facturation inférieure à 5,5$ (EXCEPT)
```sql
SELECT `CustomerId` 
FROM `customer` 
EXCEPT 
SELECT `CustomerId` 
FROM `invoice` 
GROUP BY `CustomerId` 
HAVING AVG(`Total`) < 5.5;
```
       
19. Sélectionner les identifiants des artistes à l’exception de ceux associés à des albums (EXCEPT)
```sql
SELECT `ArtistId` 
FROM `artist` 
EXCEPT 
SELECT `ArtistId` 
FROM `album`;
```
       
20. Sélectionner les villes des clients à l’exception de celles dont la somme de facturation est supérieure 80$ (EXCEPT)
```sql
SELECT `City` 
FROM `customer` 
EXCEPT  
SELECT `BillingCity` 
FROM `invoice` 
GROUP BY `BillingCity` 
HAVING SUM(`Total`) > 80;
```