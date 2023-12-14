## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre


1. Sélectionner les noms des artistes qui ont plus de 10 albums, utiliser des alias pour les résultats et les appels des tables
```sql
SELECT `ar`.`Name` AS `Nom de l'artiste` 
FROM `artist` AS `ar` 
WHERE `ar`.`ArtistId` IN (
    SELECT `ab`.`ArtistId` 
    FROM `album` AS `ab` 
    GROUP BY `ab`.`ArtistId` 
    HAVING COUNT(*) > 10
    );
```
       
2. Sélectionner les noms des genres musicaux ayant moins de 100 chansons associées, utiliser des alias pour les résultats et les appels des tables
```sql
SELECT `g`.`Name` AS `Nom du genre` 
FROM `genre` AS `g` 
WHERE `g`.`GenreId` IN (
    SELECT `t`.`GenreId` 
    FROM `track` AS `t`  
    GROUP BY `t`.`GenreId` 
    HAVING COUNT(*) < 100
    );
```
       
3. Sélectionner les noms et prénoms des clients qui ont un montant total de dépenses supérieur à 40$, utiliser des alias pour l’appel des tables
```sql
SELECT `c`.`FirstName`, `c`.`LastName` 
FROM `customer` AS `c` 
WHERE `c`.`CustomerId` IN (
    SELECT `i`.`CustomerId` 
    FROM `invoice` AS `i`  
    GROUP BY `i`.`CustomerId` 
    HAVING SUM(`i`.`Total`) > 40
    );
```
       
4. Sélectionner les noms des playlists contenant plus de 50 chansons, utiliser des alias
```sql
SELECT `p`.`Name` AS `Nom de la playlist` 
FROM `playlist` AS `p` 
WHERE `p`.`PlaylistId` IN(
    SELECT `pt`.`PlaylistId` 
    FROM `playlisttrack` AS `pt` 
    GROUP BY `pt`.`PlaylistId` 
    HAVING COUNT(*) > 50
    );
```
       
5. Sélectionner les noms des albums dont le genre est 'Rock', utiliser des alias
```sql
SELECT `al`.`Title` 
FROM `album` AS `al` 
WHERE `al`.`AlbumId` IN (
    SELECT `t`.`AlbumId` 
    FROM `track` AS `t` 
    WHERE `t`.`GenreId` IN (
        SELECT `GenreId` 
        FROM `genre` 
        WHERE `Name` = 'Rock'  
        )
    );
```
       
6. Sélectionner les noms des chansons avec leur durée (millisecondes à convertir en minutes en divisant par 60000) pour l’artiste « Black Sabbath »
```sql
SELECT `t`.`Name` AS `Nom de la chanson`, `t`.`Milliseconds` / 60000 AS `Durée (Minutes)` 
FROM `track` AS `t` 
WHERE `t`.`AlbumId` IN (
    SELECT `al`.`AlbumId` 
    FROM `album` AS `al` 
    WHERE `al`.`ArtistId` IN (
        SELECT `ArtistId` 
        FROM `artist` 
        WHERE `Name` = 'Black Sabbath'
        )
    );
```
       
7. Sélectionner les noms des artistes qui ont au moins une chanson associée ordonée par nom, utiliser des alias pour les résultats et les appels des tables (EXISTS)
```sql
SELECT `ar`.`Name` AS `Nom_Artiste` 
FROM `artist` AS `ar` 
WHERE EXISTS (
    SELECT `ArtistId` 
    FROM `album` AS `al` 
    WHERE `al`.`ArtistId` = `ar`.`ArtistId`
    ) 
ORDER BY `Nom_Artiste`;
```
       
8. Sélectionner les chansons qui ont été facturées au moins une fois (EXISTS)
```sql
SELECT `t`.`Name` AS `Nom_Chanson` 
FROM `track` AS `t` WHERE EXISTS (
    SELECT `TrackId` 
    FROM `invoiceline` AS `i` 
    WHERE `i`.`TrackId` = `t`.`TrackId` 
    );
```
       
9. Sélectionner les chansons qui sont associées à au moins une playlist, utiliser des alias pour les résultats et les appels des tables (EXISTS)
```sql
SELECT `t`.`Name` AS `Nom_Chanson` 
FROM `track` AS `t` 
WHERE EXISTS (
    SELECT `TrackId` 
    FROM `playlisttrack` AS `pt` 
    WHERE `pt`.`TrackId` = `t`.`TrackId` 
    );
```
       
10. Sélectionner les noms des artistes pour qui aucun album n'est répertorié, utiliser des alias (EXISTS)
```sql
SELECT `ar`.`Name` AS `Nom_Artiste` 
FROM `artist` AS `ar` 
WHERE NOT EXISTS (
    SELECT `ArtistId` 
    FROM `album` AS `al` 
    WHERE `al`.`ArtistId` = `ar`.`ArtistId`
    );
```
       
11. Sélectionner les chansons qui n’ont jamais été facturées (EXISTS)
```sql
SELECT `t`.`Name` AS `Nom_Chanson` 
FROM `track` AS `t` 
WHERE NOT EXISTS (
    SELECT `TrackId` 
    FROM `invoiceline` AS `i` 
    WHERE `i`.`TrackId` = `t`.`TrackId` 
    );
```
       
12. Sélectionner les chansons avec le prix unitaire le plus élevé (ALL)
```sql
SELECT `Name` 
FROM `track` 
WHERE `UnitPrice` = ALL (
    SELECT MAX(`UnitPrice`) 
    FROM `track`
    );
```
       
13. Sélectionner l’identifiant de l’artiste qui a le plus grand nombre d’album associé (ALL)
```sql
SELECT `ArtistId` 
FROM `album` 
GROUP BY `ArtistId` 
HAVING COUNT(`AlbumId`) >= ALL (
    SELECT COUNT(`AlbumId`) 
    FROM `album` 
    GROUP BY `ArtistId`
    );
```
       
14. Sélectionner l’album avec la durée d’écoute la plus longue (ALL)
```sql
SELECT `AlbumId` 
FROM `track` 
GROUP BY `AlbumId` 
HAVING SUM(`Milliseconds`) >= ALL (
    SELECT SUM(`Milliseconds`) 
    FROM `track` 
    GROUP BY `AlbumId`
    );
```
       
15. Sélectionner le client dont le montant total des factures est supérieur à tous les autres (ALL)
```sql
SELECT `FirstName`, `LastName` 
FROM `customer` 
WHERE `CustomerId` = ALL (
    SELECT `CustomerId` 
    FROM `invoice` 
    GROUP BY `CustomerId` 
    HAVING SUM(`Total`) >= ALL (
        SELECT SUM(`Total`) 
        FROM `invoice` 
        GROUP BY `CustomerId`
        )
    );
```
       
16. Sélectionner l’employé qui a été embauché avant tous les autres (ALL)
```sql
SELECT `FirstName`, `LastName` 
FROM `employee` 
WHERE `EmployeeId` = ALL (
    SELECT `EmployeeId` 
    FROM `employee` 
    WHERE `HireDate` <= ALL (
        SELECT MIN(`HireDate`) 
        FROM `employee` 
        GROUP BY `HireDate`
        )
);
```
       
17. Sélectionner les titres des albums ayant au moins une chanson avec un prix unitaire supérieur à 0,99$, utiliser des alias (ANY)
```sql
SELECT `al`.`Title` 
FROM `album` AS `al` 
WHERE `al`.`AlbumId` = ANY (
    SELECT `t`.`AlbumId` 
    FROM `track` AS `t` 
    WHERE `t`.`UnitPrice` > 0.99
    );
```
       
18. Sélectionner les noms des genres musicaux ayant au moins une chanson avec une durée inférieure à 2 minutes (120 000 millisecondes), utiliser des alias (ANY)
```sql
SELECT `g`.`Name` AS `Nom_du_genre` 
FROM `genre` AS `g` 
WHERE `g`.`GenreId` = ANY (
    SELECT `t`.`GenreId` 
    FROM `track` AS `t` 
    WHERE `t`.`Milliseconds` < 120000
    );
```
       
19. Sélectionner les identifiants des artistes dont la somme des prix unitaires des chansons de l'album est supérieure à 20$, utiliser des alias (ANY)
```sql
SELECT `al`.`ArtistId` 
FROM `album` AS `al` 
WHERE `al`.`AlbumId` = ANY (
    SELECT `t`.`AlbumId` 
    FROM `track` AS `t` 
    GROUP BY `t`.`AlbumId` 
    HAVING SUM(`t`.`UnitPrice`) > 20
    ) 
GROUP BY `al`.`ArtistId`;
```
       
20. Sélectionner les noms des playlists contenant au moins une chanson avec un prix unitaire inférieur à 1$, utiliser des alias (ANY)
```sql
SELECT `p`.`Name` AS `Nom_de_la_playlist` 
FROM `playlist` AS `p` 
WHERE `p`.`PlaylistId` IN (
    SELECT `pt`.`PlaylistId` 
    FROM `playlisttrack` AS `pt` 
    WHERE `pt`.`TrackId` IN (
        SELECT `t`.`TrackId` 
        FROM `track` AS `t` 
        WHERE `t`.`UnitPrice` < 1
        )
    );
```
       
21. Sélectionner les noms des chansons qui ont été facturées pour un montant supérieur à la moyenne des prix unitaires des chansons, utiliser des alias (ANY)
```sql
SELECT `t`.`Name` 
FROM `track` AS `t` 
WHERE `t`.`TrackId` = ANY (
    SELECT `TrackId` 
    FROM `invoiceline` 
    WHERE `UnitPrice` > ANY (
        SELECT AVG(`UnitPrice`) 
        FROM `track`
        )
    );
```
       