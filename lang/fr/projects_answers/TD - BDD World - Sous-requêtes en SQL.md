## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre


1. Sélectionner les noms des continents (regions) qui ont plus de 2 sous-continents (subregions), utiliser des alias
```sql
SELECT `name` AS `Continent` 
FROM `regions` 
WHERE `id` IN (
    SELECT `region_id`
    FROM `subregions` 
    GROUP BY `region_id` 
    HAVING COUNT(*) > 2
    );
```
       
2. Sélectionner les noms des pays qui ont des États avec des coordonnées de latitude supérieures à 40, utiliser des alias
```sql
SELECT `name` AS `Nom du pays` 
FROM `countries` 
WHERE `id` IN (
    SELECT `country_id` 
    FROM `states` 
    WHERE `latitude` > 40
    );
```
       
3. Sélectionner les noms des États qui ont des villes avec des noms commençant par « New »
```sql
SELECT `name` 
FROM `states` 
WHERE `id` IN (
    SELECT `state_id` 
    FROM `cities` 
    WHERE `name` LIKE 'New%'
    );
```
       
4. Sélectionner les noms des continents (regions) ayant au moins un sous-continents(subregion), utiliser des alias pour les résultats et l’appel des tables
```sql
SELECT `r`.`name` AS `Continent` 
FROM `regions` AS `r` 
WHERE `r`.`id` IN (
    SELECT `region_id` 
    FROM `subregions`
    );
```
       
5. Sélectionner les noms des continents (regions) comprenant des pays ayant une latitude inférieure à 35
```sql
SELECT `name` 
FROM `regions` 
WHERE `id` IN (
    SELECT `region_id` 
    FROM `countries` 
    WHERE `latitude` < 35
    );
```
       
6. Sélectionner les noms des continents (regions) pour qui il existe des sous-continents (subregions) existants, utiliser des alias pour les résultats et l’appel des tables (EXISTS)
```sql
SELECT `r`.`name`  AS `Continent` 
FROM `regions` AS `r` 
WHERE EXISTS (
    SELECT `s`.`name` 
    FROM `subregions` AS `s`
    WHERE `r`.`id` = `s`.`region_id`
    );
```
       
7. Sélectionner les noms des pays pour qui il existe des États avec une latitude supérieure à 50 existants, utiliser des alias (EXISTS)
```sql
SELECT `c`.`name` AS `Pays` 
FROM `countries` AS `c` 
WHERE EXISTS (
    SELECT `s`.`name` 
    FROM `states` AS `s` 
    WHERE `c`.`id` = `s`.`country_id` 
    AND `s`.`latitude` > 50
    );
```
       
8. Sélectionner les noms des États pour lesquels il existe au moins une ville avec un nom commençant par "New", utiliser des alias (EXISTS)
```sql
SELECT `s`.`name` 
FROM `states` AS `s` 
WHERE EXISTS (
    SELECT `c`.`id` 
    FROM `cities` AS `c` 
    WHERE `c`.`state_id` = `s`.`id` 
    AND `c`.`name` LIKE 'New%'
    );
```
       
9. Sélectionner les noms des continents (regions) pour lesquels il existe plus de deux sous-continents (subregions), utiliser des alias (EXISTS)
```sql
SELECT `r`.`name` 
FROM `regions` AS `r` 
WHERE EXISTS (
    SELECT `s`.`region_id` 
    FROM `subregions` AS `s` 
    WHERE `r`.`id` = `s`.`region_id` 
    GROUP BY `s`.`region_id` 
    HAVING COUNT(*) > 2
    );
```
       
10. Sélectionner les pays pour lesquels il n’existe aucun État, utiliser des alias (EXISTS)
```sql
SELECT `c`.`name` AS `Pays` 
FROM `countries` AS `c` 
WHERE NOT EXISTS (
    SELECT `st`.`country_id` 
    FROM `states` AS `st` 
    WHERE `st`.`country_id` = `c`.`id`
    );
```
       
11. Sélectionner les villes qui ont été créées après la création du dernier pays (ALL)
```sql
SELECT `name` 
FROM `cities` 
WHERE `created_at` > ALL (
    SELECT MAX(`created_at`) 
    FROM `countries`
    );
```
       
12. Sélectionner les continents avec le plus grand nombre de sous-continents (ALL)
```sql
SELECT `region_id` 
FROM `subregions` 
GROUP BY `region_id` 
HAVING COUNT(*) >= ALL (
    SELECT COUNT(*) 
    FROM `subregions` 
    GROUP BY `region_id`
    );
```
       
13. Sélectionner les pays avec le plus grand nombre de villes (ALL)
```sql
SELECT `country_id` 
FROM `cities` 
GROUP BY `country_id` 
HAVING COUNT(*) >= ALL (
    SELECT COUNT(*) 
    FROM `cities` 
    GROUP BY `country_id`
    );
```
       
14. Sélectionner le pays avec la latitude la plus élevée (ALL)
```sql
SELECT `name` 
FROM `countries` 
WHERE `id` = ALL (
    SELECT `country_id` 
    FROM `states` 
    WHERE `latitude` >= ALL (
        SELECT MAX(`latitude`) 
        FROM `states`
        )
    );
```
       
15. Sélectionner la région avec le moins de pays  (ALL)
```sql
SELECT `name` 
FROM `regions` 
WHERE `id` = ALL (
    SELECT `region_id` 
    FROM `countries` 
    GROUP BY `region_id` 
    HAVING COUNT(*) <= ALL (
        SELECT COUNT(*) 
        FROM `countries` 
        GROUP BY `region_id`
        )
    );
```
       
16. Sélectionner l’identifiant du pays à qui est associée la ville avec la plus grande latitude (ANY)
```sql
SELECT `ci`.`country_id` 
FROM `cities` AS `ci` 
WHERE ci.`latitude` = ANY (
    SELECT MAX(`latitude`) 
    FROM `cities`
    );
```
       
17. Séléctionner les noms des continents qui possèdent au moins un sous-sontinent associé (ANY)
```sql
SELECT `name` 
FROM `regions` 
WHERE `id` = ANY (
    SELECT `region_id` 
    FROM `subregions`
    );
```
       
18. Sélectionner les noms des villes associées à la « France » (ANY)
```sql
SELECT `name` 
FROM `cities` 
WHERE `country_id` = ANY (
    SELECT `id` 
    FROM `countries` 
    WHERE `name` = 'France'
    );
```

19. Sélectionner le nom du pays à qui est associée la ville avec la latitude la plus basse (ANY)
```sql
SELECT `c`.`name` AS `Nom_du_pays` 
FROM `countries` AS `c` 
WHERE `c`.`id` = ANY (
    SELECT `ci`.`country_id` 
    FROM `cities` AS `ci` 
    WHERE `ci`.`latitude` = ANY (
        SELECT MIN(`latitude`) 
        FROM `cities`
        )
    );
```
       
20. Sélectionner les continents qui possèdent plus de 2 sous-continents associés (ANY)
```sql
SELECT * 
FROM `regions` 
WHERE `id` = ANY (
    SELECT `region_id` 
    FROM `subregions` 
    GROUP BY  `region_id` 
    HAVING COUNT(*) > 2
    );
```