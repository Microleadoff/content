## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

    
1. Sélectionner les titres des albums dont l'artiste est « Led Zeppelin » (JOIN)
```sql
SELECT DISTINCT `al`.`Title` 
FROM `album` AS `al` 
JOIN `artist` AS `ar` ON `al`.`ArtistId` = `ar`.`ArtistId` 
WHERE `ar`.`Name` = 'Led Zeppelin';
```
       
2. Sélectionner les titres des albums et les noms des artistes correspondants (INNER JOIN)
```sql
SELECT `al`.`Title`, `ar`.`Name` 
FROM `album` AS `al` 
INNER JOIN `artist` AS `ar` ON `al`.`ArtistId` = `ar`.`ArtistId`;
```
       
3. Sélectionner les noms et prénoms des clients associés aux noms et prénoms des employés responsables du service (INNER JOIN)
```sql
SELECT `cu`.`LastName`, `cu`.`FirstName`, `emp`.`LastName` AS `EmployéLastName`, `emp`.`FirstName` AS `EmployéFirstName` 
FROM `customer` AS `cu` 
INNER JOIN `employee` AS `emp` ON `cu`.`SupportRepId` = `emp`.`EmployeeId`;
```
       
4. Sélectionner les titres des chansons associées au genre (INNER JOIN)
```sql
SELECT `tr`.`Name` AS `Chansons`, `ge`.`Name` AS `Genres` 
FROM `track` AS `tr` 
INNER JOIN `genre` AS `ge` ON `tr`.`GenreId` = `ge`.`GenreId`;
```
       
5. Sélectionner les titres des Chansons, des albums et les noms des artistes associés (INNER JOIN)
```sql
SELECT `tr`.`Name` AS `Chansons`, `al`.`Title` AS `Albums`, `ar`.`Name` AS `Artists` 
FROM `track` AS `tr` 
INNER JOIN `album` AS `al` ON `tr`.`AlbumId` = `al`.`AlbumId` 
INNER JOIN `artist` AS `ar` ON `al`.`ArtistId` = `ar`.`ArtistId`;
```
       
6. Sélectionner les noms des playlists et les titres des chansons associées (INNER JOIN)
```sql
SELECT `pl`.`Name` AS `Playlists`, `tr`.`Name` AS `Chansons` 
FROM `playlist` AS `pl` 
INNER JOIN `playlisttrack` AS `pt` ON `pl`.`PlaylistId` = `pt`.`PlaylistId` 
INNER JOIN `track` AS `tr` ON `pt`.`TrackId` = `tr`.`TrackId`;
```
       
7. Sélectionner les noms et prénoms des clients qui ont acheté des chansons du genre « Metal » (INNER JOIN et sous-requête)
```sql
SELECT DISTINCT `cu`.`LastName`, `cu`.`FirstName` 
FROM `track` AS `tr` 
INNER JOIN `invoiceline` AS `il` ON `tr`.`TrackId` = `il`.`TrackId` 
INNER JOIN `invoice` AS `iv` ON `il`.`InvoiceId` = `iv`.`InvoiceId` 
INNER JOIN `customer` AS `cu` ON `iv`.`CustomerId` = `cu`.`CustomerId` 
WHERE `tr`.`GenreId` IN (
    SELECT `GenreId` 
    FROM `genre` 
    WHERE `Name` = 'Metal'
    );
```
       
8. Sélectionner les noms des artistes et les types de média (CROSS JOIN)
```sql
SELECT `ar`.`Name` AS `Artiste`, `m`.`Name` AS `TypeMedia` 
FROM `artist` AS `ar` 
CROSS JOIN `mediatype` AS `m`;
```
       
9. Sélectionner les noms des chansons et les genres musicaux (CROSS JOIN)
```sql
SELECT `t`.`Name` AS `Chanson`, `g`.`Name` AS `Genre` 
FROM `track` AS `t` 
CROSS JOIN `genre` AS `g`;
```
       
10. Sélectionner les titres des albums et les types de média (CROSS JOIN)
```sql
SELECT `a`.`Title` AS `Album`, `m`.`Name` AS `TypeMedia` 
FROM `album` AS `a` 
CROSS JOIN `mediatype` AS `m`;
```
       
11. Sélectionner les noms des playlists, les titres des chansons et les types de médias (CROSS JOIN)
```sql
SELECT `p`.`PlaylistId`, `t`.`Name` AS `Chansons`, `m`.`Name` AS `MediaType`
FROM `playlist` AS `p` 
CROSS JOIN `track` AS `t` 
CROSS JOIN `mediatype` AS `m`;
```
       
12. Sélectionner les titres des chansons et les genres musicaux (CROSS JOIN)
```sql
SELECT `t`.`Name` AS `Chanson`, `g`.`Name` AS `Genre` 
FROM `track` AS `t` 
CROSS JOIN `genre` AS `g`;
```

13. Sélectionner les genres musicaux et le nombre de chansons de chaque genre (LEFT JOIN)
```sql
SELECT `ge`.`Name` AS `Genre`, COUNT(`tr`.`TrackId`) AS `Nombre de Chansons` 
FROM `genre` AS `ge` 
LEFT JOIN `track` AS `tr` ON `ge`.`GenreId` = `tr`.`GenreId` 
GROUP BY `ge`.`Name`;
```
       
14. Sélectionner les genres musicaux et le nombre de chansons de chaque genre qui ont été achetées, par ordre décroissant (LEFT JOIN)
```sql
SELECT `ge`.`Name` AS `Genre`, COUNT(`tr`.`TrackId`) AS `TotalVentes` 
FROM `genre` AS `ge` 
LEFT JOIN `track` AS `tr` ON `ge`.`GenreId` = `tr`.`GenreId` 
LEFT JOIN `invoiceline` AS `il` ON `tr`.`TrackId` = `il`.`TrackId` 
GROUP BY `ge`.`GenreId` 
ORDER BY `TotalVentes` DESC;
```
       
15. Sélectionner les noms, prénoms et les ventes totales par clients (LEFT JOIN)
```sql
SELECT `cu`.`LastName`, `cu`.`FirstName`, SUM(`il`.`UnitPrice` * `il`.`Quantity`) AS `TotalVentes` 
FROM `customer` AS `cu` 
LEFT JOIN `invoice` AS `iv` ON `cu`.`CustomerId` = `iv`.`CustomerId` 
LEFT JOIN `invoiceline` AS `il` ON `iv`.`InvoiceId` = `il`.`InvoiceId` 
GROUP BY `cu`.`CustomerId`;
```
       
16. Sélectionner les prénoms des employés et de leurs subordonnés directs (LEFT JOIN)
```sql
SELECT `emp`.`FirstName` AS `Employé`, `sub`.`FirstName` AS `Subordonné` 
FROM `employee` AS `emp` 
LEFT JOIN `employee` AS `sub` ON `emp`.`EmployeeId` = `sub`.`ReportsTo`;
```

17. Sélectionner les noms des artistes et le nombre d'album par artistes  (LEFT JOIN)
```sql
SELECT `ar`.`Name` AS `Artiste`, COUNT(`al`.`AlbumId`) AS `NombreAlbums` 
FROM `artist` AS `ar` 
LEFT JOIN `album` AS `al` ON `ar`.`ArtistId` = `al`.`ArtistId` 
GROUP BY `ar`.`ArtistId`;
```

18. Sélectionner les noms des artistes et les titres albums associés (RIGHT JOIN)
```sql
SELECT `ar`.`Name` AS `Artiste`, `al`.`Title` AS `Album` 
FROM `artist` AS `ar`
RIGHT JOIN `album` AS `al` ON `ar`.`ArtistId` = `al`.`ArtistId`;
```
       
19. Sélectionner les noms et prénoms des clients et les identifiants des factures associées (RIGHT JOIN)
```sql
SELECT `cu`.`LastName`, `cu`.`FirstName`, `iv`.`InvoiceId` 
FROM `customer` AS `cu` 
RIGHT JOIN `invoice` AS `iv` ON `cu`.`CustomerId` = `iv`.`CustomerId`;
```
       
20. Sélectionner les genres musicaux et les chansons associées (RIGHT JOIN)
```sql
SELECT `ge`.`Name` AS `Genre`, `tr`.`Name` AS `Chanson` 
FROM `genre` AS `ge` 
RIGHT JOIN `track` AS `tr` ON `ge`.`GenreId` = `tr`.`GenreId`;
```
       
21. Sélectionner les genres musicaux et la somme des achats par genre (RIGHT JOIN)
```sql
SELECT `ge`.`Name` AS `Genre`, SUM(`il`.`UnitPrice` * `il`.`Quantity`) AS `TotalAchats` 
FROM `genre` AS `ge` 
RIGHT JOIN `track` AS `tr` ON `ge`.`GenreId` = `tr`.`GenreId` 
RIGHT JOIN `invoiceline` AS `il` ON `tr`.`TrackId` = `il`.`TrackId` 
GROUP BY `ge`.`GenreId` 
ORDER BY `ge`.`Name`;
```
       
22. Sélectionner les informations sur les factures avec les lignes de factures associées (FULL JOIN) 
```sql
SELECT `i`.`InvoiceId`, `il`.`InvoiceLineId` 
FROM `invoice` AS `i` 
FULL JOIN `invoiceline` AS `il` ON `i`.`InvoiceId` = `il`.`InvoiceId`;
```

VERSION MySQL Workbench :
```sql
SELECT `i`.`InvoiceId`, `il`.`InvoiceLineId` 
FROM `invoice` AS `i` 
LEFT JOIN `invoiceline` AS `il` ON `i`.`InvoiceId` = `il`.`InvoiceId` 
UNION SELECT `i`.`InvoiceId`, NULL AS `InvoiceLineId` 
FROM `invoice` AS `i` 
RIGHT JOIN `invoiceline` AS `il` ON `i`.`InvoiceId` = `il`.`InvoiceId`;
```
       
23. Sélectionner les noms et prénoms des employés et de leurs subordonnés (FULL JOIN) 
```sql
SELECT `e`.`LastName` AS `ManagerLastName`, `e`.`FirstName` AS `ManagerFirstName`, `sub`.`LastName` AS `EmployeeLastName`, `sub`.`FirstName` AS `EmployeeFirstName` 
FROM `employee` AS `e` 
FULL JOIN `employee` AS `sub` ON `e`.`EmployeeId` = `sub`.`ReportsTo`;
```

VERSION MySQL Workbench :
```sql
SELECT `e`.`LastName` AS `ManagerLastName`, `e`.`FirstName` AS `ManagerFirstName`, `sub`.`LastName` AS `EmployeeLastName`, `sub`.`FirstName` AS `EmployeeFirstName` 
FROM `employee` AS `e` 
LEFT JOIN `employee` AS `sub` ON `e`.`EmployeeId` = `sub`.`ReportsTo` 
UNION 
SELECT `e`.`FirstName` AS `ManagerFirstName`, `e`.`LastName` AS `ManagerLastName`, NULL AS `EmployeeLastName` , NULL AS `EmployeeFirstName`
FROM `employee` AS `e` 
RIGHT JOIN `employee` AS `sub` ON `e`.`EmployeeId` = `sub`.`ReportsTo`;
```

24. Sélectionner les noms et prénoms des clients et les factures associées (FULL JOIN) 
```sql
SELECT `c`.`LastName`, `c`.`FirstName`, `i`.`InvoiceId` 
FROM `customer` AS `c` 
FULL JOIN `invoice` `i` ON `c`.`CustomerId` = `i`.`CustomerId`;
```

VERSION MySQL Workbench :
```sql
SELECT `c`.`LastName`, `c`.`FirstName`, `i`.`InvoiceId` 
FROM `customer` AS `c` 
LEFT JOIN `invoice` AS `i` ON `c`.`CustomerId` = `i`.`CustomerId` 
UNION 
SELECT `c`.`LastName`, `c`.`FirstName`, `i`.`InvoiceId` 
FROM `customer` AS `c` 
RIGHT JOIN `invoice` AS `i` ON `c`.`CustomerId` = `i`.`CustomerId`;
```
       
25. Sélectionner les artistes et les albums associés (FULL JOIN) 
```sql
SELECT `a`.`Name` AS `Artiste`, `al`.`Title` AS `Album` 
FROM `artist` `a` 
FULL JOIN `album` `al` ON `a`.`ArtistId` = `al`.`ArtistId`;
```

VERSION MySQL Workbench :
```sql
SELECT `a`.`Name` AS `Artiste`, `al`.`Title` AS `Album` 
FROM `artist` AS `a` 
LEFT JOIN `album` AS `al` ON `a`.`ArtistId` = `al`.`ArtistId` 
UNION 
SELECT `a`.`Name` AS `Artist`, `al`.`Title` AS `Album` 
FROM `artist` AS `a` 
RIGHT JOIN `album` AS `al` ON `a`.`ArtistId` = `al`.`ArtistId`;
```
       
26. Sélectionner les factures avec leurs lignes de factures et les chansons correspondantes (FULL JOIN) 
```sql
SELECT `i`.`InvoiceId`, `il`.`InvoiceLineId`, `t`.`Name`
FROM `invoice` AS `i` 
FULL JOIN `invoiceline` AS `il` ON `i`.`InvoiceId` = `il`.`InvoiceId` 
LEFT JOIN `track` AS `t` ON `il`.`TrackId` = `t`.`TrackId`;
```

VERSION MySQL Workbench :
```sql
SELECT `i`.`InvoiceId`, `il`.`InvoiceLineId`, `t`.`Name` 
FROM `invoice` AS `i` 
LEFT JOIN `invoiceline` AS `il` ON `i`.`InvoiceId` = `il`.`InvoiceId` 
LEFT JOIN `track` AS `t` ON `il`.`TrackId` = `t`.`TrackId` 
UNION 
SELECT `i`.`InvoiceId`, `il`.`InvoiceLineId`, `t`.`Name` 
FROM `invoice` AS `i` 
RIGHT JOIN `invoiceline` AS `il` ON `i`.`InvoiceId` = `il`.`InvoiceId` 
RIGHT JOIN `track` AS `t` ON `il`.`TrackId` = `t`.`TrackId`;
```

27. Sélectionner les noms et prénoms des employés et leur manager associé (SELF JOIN)
```sql
SELECT `e1`.`LastName`, `e1`.`FirstName`, `e2`.`LastName` AS `ManagerLastName`, `e2`.`FirstName` AS `ManagerFirstName` 
FROM `employee` AS `e1` 
INNER JOIN `employee` AS `e2` ON `e1`.`ReportsTo` = `e2`.`EmployeeId`;
```
       
28. Sélectionner les noms et prénoms des clients ayant le même prénom (SELF JOIN)
```sql
SELECT `c1`.`LastName` AS `LastName1`, `c1`.`FirstName` AS `FirstName1`, `c2`.`LastName` AS `LastName2`, `c2`.`FirstName` AS `FirstName2` 
FROM `customer` AS `c1` 
JOIN `customer` AS `c2` ON `c1`.`FirstName` = `c2`.`FirstName` 
AND `c1`.`CustomerId` != `c2`.`CustomerId`;
```
       
29. Sélectionner les identifiants et les titres des albums partageant le même artiste (SELF JOIN)
```sql
SELECT `a1`.`AlbumId` AS `AlbumId1`, `a2`.`AlbumId` AS `AlbumId2`, `a1`.`Title` AS `Album` 
FROM `album` AS `a1` 
JOIN `album` AS `a2` ON `a1`.`ArtistId` = `a2`.`ArtistId` 
AND `a1`.`AlbumId` != `a2`.`AlbumId`;
```
       
30. Sélectionner les identifiants et les titres des chansons partageant la même durée (SELF JOIN)
```sql
SELECT `t1`.`TrackId` AS `TrackId1`, `t2`.`TrackId` AS `TrackId2`, `t1`.`Name` AS `Chanson`
 FROM `track` AS `t1` 
 JOIN `track` AS `t2` ON `t1`.`Milliseconds` = `t2`.`Milliseconds` 
 AND `t1`.`TrackId` != `t2`.`TrackId`;
```

31. Sélectionner les identifiants des factures et des lignes de factures associées (NATURAL JOIN)
```sql
SELECT `i`.`InvoiceId`, `il`.`InvoiceLineId` 
FROM `invoice` AS `i` 
NATURAL JOIN `invoiceline` AS `il`;
```
       
32. Sélectionner les albums avec leurs genres (NATURAL JOIN)
```sql
SELECT `al`.`Title` AS `Album`, `g`.`Name` AS `Genre` 
FROM `album` AS `al` 
NATURAL JOIN `genre` AS `g`;
```
       
33. Sélectionner les noms et prénoms des clients et les identifiants des factures associées (NATURAL JOIN)
```sql
SELECT `c`.`LastName`, `c`.`FirstName`, `i`.`InvoiceId` 
FROM `customer` AS `c` 
NATURAL JOIN `invoice` AS `i`;
```
       
34. Sélectionner les noms des artistes et les titres de leurs albums (NATURAL JOIN)
```sql
SELECT `a`.`Name` AS `ArtistName`, `al`.`Title` AS `Album` 
FROM `artist` AS `a` 
NATURAL JOIN `album` AS `al`;
```
       
35. Sélectionner les identifiants des factures et des lignes de factures ainsi que les titres des chansons correspondantes (NATURAL JOIN)
```sql
SELECT `i`.`InvoiceId`, `il`.`InvoiceLineId`, `t`.`Name` AS `Chanson` 
FROM `invoice` AS `i` 
NATURAL JOIN `invoiceline` AS `il` 
NATURAL JOIN `track` AS `t`;
```
       