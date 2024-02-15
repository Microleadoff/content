## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre


1. Sélectionner les noms des pays et leurs sous-continents associés, triés par ordre alphabétique des sous-continents (INNER JOIN)
```sql
SELECT `c`.`name` AS `Pays`, `s`.`name` AS `Sous_continents` 
FROM `countries` AS `c` 
INNER JOIN `subregions` AS `s` ON `c`.`subregion_id` = `s`.`id` 
ORDER BY `s`.`name`;
```
       
2. Sélectionner les noms des continents et leurs sous-continents correspondants (INNER JOIN)
```sql
SELECT `r`.`name` AS `Continents`, `s`.`name` AS `Sous_continents` 
FROM `regions` AS `r` 
INNER JOIN `subregions` AS `s` ON `r`.`id` = `s`.`region_id`;
```
       
3. Sélectionner les noms des pays et leurs capitales (INNER JOIN)
```sql
SELECT `c`.`name` AS `Pays`, `c`.`capital` AS `Capitales` 
FROM `countries` AS `c` 
INNER JOIN `cities` AS `ci` ON `c`.`capital` = `ci`.`name`;
```
       
4. Sélectionner les noms des États et leurs pays correspondants (INNER JOIN)
```sql
SELECT `s`.`name` AS `États`, `c`.`name` AS `Pays` 
FROM `states` AS `s` 
INNER JOIN `countries` AS `c` ON `s`.`country_id` = `c`.`id`;
```
       
5. Sélectionner le nombre de pays par continent (INNER JOIN)
```sql
SELECT `r`.`name` AS `Continents`, COUNT(`c`.`id`) AS `Nombre de Pays` 
FROM `regions` AS `r` 
INNER JOIN `countries` AS `c` ON `r`.`id` = `c`.`region_id` 
GROUP BY `r`.`name`;
```
       
6. Sélectionner les noms des sous-régions, des villes et leurs latitudes associées (INNER JOIN)
```sql
SELECT `s`.`name` AS `Sous_continents`, `c`.`name` AS `Villes`, `c`.`latitude` 
FROM `subregions` AS `s` 
INNER JOIN `states` AS `st` ON `s`.`id` = `st`.`id` 
INNER JOIN `cities` AS `c` ON `st`.`id` = `c`.`state_id`;
```
       
7. Sélectionner les noms des pays ayant au moins une ville répertoriée dans un sous-continent ayant plus de 10 villes (INNER JOIN et Sous-requête)
```sql
SELECT DISTINCT `c`.`name` AS `Pays` 
FROM `countries` AS `c` 
INNER JOIN `subregions` AS `s` ON `c`.`subregion_id` = `s`.`id` 
WHERE `c`.`subregion_id` IN (
    SELECT `subregion_id` 
    FROM `cities` 
    GROUP BY `subregion_id` 
    HAVING COUNT(`id`) > 10
    );
```
       
8. Sélectionner les pays et les États (CROSS JOIN)
```sql
SELECT `c`.`name` AS `Pays`, `s`.`name` AS `États` 
FROM `countries` AS `c` 
CROSS JOIN `states` AS `s`;
```
       
9. Sélectionner les pays et les capitales (CROSS JOIN)
```sql
SELECT `c`.`name` AS `Pays`, `ci`.`name` AS `Capitales` 
FROM `countries` AS `c` 
CROSS JOIN `cities` AS `ci` 
WHERE `c`.`capital` = `ci`.`name`;
```
       
10. Sélectionner les continents et les États (CROSS JOIN)
```sql
SELECT `r`.`name` AS `Continents`, `s`.`name` AS `États` 
FROM `regions` AS `r` 
CROSS JOIN `states` AS `s`;
```
       
11. Sélectionner les continents et les États (CROSS JOIN)
```sql
SELECT `r`.`name` AS `Continents`,`ci`.`name` AS `Villes` 
FROM `regions` AS `r` 
CROSS JOIN `cities` AS `ci`;
```
       
12. Sélectionner les pays associés à leurs capitales (LEFT JOIN)
```sql
SELECT `c`.`name` AS `Pays`, `c`.`capital` AS `Capitales` 
FROM `countries` AS `c` 
LEFT JOIN `cities` AS `ci` ON `c`.`capital` = `ci`.`name`;
```
       
13. Sélectionner le nombre de pays par continent (LEFT JOIN)
```sql
SELECT `r`.`name` AS `Continents`, COUNT(`c`.`id`) AS `Nombre de Pays` 
FROM `regions` AS `r` 
LEFT JOIN `countries` AS `c` ON `r`.`id` = `c`.`region_id` 
GROUP BY `r`.`name`;
```
       
14. Sélectionner les noms des capitales avec les noms de ville pour les pays associés(LEFT JOIN)
```sql
SELECT `ci`.`name` AS `Capitales`, `c`.`name` AS `Pays`, `ci`.`name` AS `Villes` 
FROM `cities` AS `ci` 
LEFT JOIN `countries` AS `c` ON `c`.`capital` = `ci`.`name`;
```
       
15. Sélectionner les noms des pays avec leurs villes associées dont la latitude est supérieure à 45 degrés (LEFT JOIN)
```sql
SELECT `c`.`name` AS `Pays`, `ci`.`name` AS `Villes`, `ci`.`latitude` 
FROM `countries` AS `c` 
LEFT JOIN `cities` AS `ci` ON `c`.`id` = `ci`.`country_id` 
AND `ci`.`latitude` > 45;
```
       
16. Sélectionner les sous-continents et les noms de pays associés dont la latitude est inférieure à 30 degrés (LEFT JOIN)
```sql
SELECT `sr`.`name` AS `Sous_Continents`, `c`.`name` AS `Pays`, `ci`.`latitude` 
FROM `subregions` AS `sr` 
LEFT JOIN `countries` AS `c` ON `sr`.`id` = `c`.`subregion_id` 
LEFT JOIN `cities` AS `ci` ON `c`.`id` = `ci`.`country_id` 
AND `ci`.`latitude` < 30;
```
       
17. Sélectionner les noms des villes avec leurs pays associés (RIGHT JOIN)
```sql
SELECT `ci`.`name` AS `Villes`, `c`.`name` AS `Pays` 
FROM `cities` AS `ci` 
RIGHT JOIN `countries` AS `c` ON `ci`.`country_id` = `c`.`id`;
```
       
18. Sélectionner les noms des sous-continents avec les noms de ville pour les pays associés (RIGHT JOIN)
```sql
SELECT `sr`.`name` AS `Sous_continents`, `c`.`name` AS `Pays`, `ci`.`name` AS `Villes` 
FROM `subregions` AS `sr` 
RIGHT JOIN `countries` AS `c` ON `sr`.`id` = `c`.`subregion_id`;
```
       
19. Sélectionner les noms des sous-continents et des villes pour les pays associés dont la latitude est inférieure à 30 degrés (RIGHT JOIN)
```sql
SELECT `sr`.`name` AS `Sous_continents`, `c`.`name` AS `Pays`, `ci`.`name` AS `Villes`, `ci`.`latitude` 
FROM `subregions` AS `sr` 
RIGHT JOIN `countries` AS `c` ON `sr`.`id` = `c`.`subregion_id` 
RIGHT JOIN `cities` AS `ci` ON `c`.`id` = `ci`.`country_id` 
AND `ci`.`latitude` < 30;
```
       
20. Sélectionner les noms des pays avec leurs villes associées ayant une latitude supérieure à 45 degrés (RIGHT JOIN)
```sql
SELECT `c`.`name` AS `Pays`, `ci`.`name` AS `Villes`, `ci`.`latitude` 
FROM `countries` AS `c` 
RIGHT JOIN `cities` AS `ci` ON `c`.`id` = `ci`.`country_id` 
AND `ci`.`latitude` > 45;
```
       
21. Sélectionner les noms des pays et leurs capitales (FULL JOIN)
```sql
SELECT `c`.`name` AS `Pays`, `c`.`capital` AS `Capitales` 
FROM `countries` AS `c` 
FULL JOIN `cities` AS `ci` ON `c`.`capital` = `ci`.`name`;
```

VERSION MySQL Workbench :
```sql
SELECT `c`.`name` AS `Pays`, `c`.`capital` AS `Capitales` 
FROM `countries` AS `c` 
LEFT JOIN `cities` AS `ci` ON `c`.`capital` = `ci`.`name` 
UNION 
SELECT `c`.`name` AS `Pays`, `ci`.`name` AS `Capitales` 
FROM `cities` AS `ci` 
LEFT JOIN `countries` AS `c` ON `c`.`capital` = `ci`.`name`;
```
       
22. Sélectionner les noms des villes et des pays associés (FULL JOIN)
```sql
SELECT `ci`.`name` AS `Villes`, `c`.`name` AS `Pays` 
FROM `cities` AS `ci` 
FULL JOIN `countries` AS `c` ON `ci`.`country_id` = `c`.`id`;
```

VERSION MySQL Workbench :
```sql
SELECT `ci`.`name` AS `Villes`, `c`.`name` AS `Pays` 
FROM `cities` AS `ci` 
LEFT JOIN `countries` AS `c` ON `ci`.`country_id` = `c`.`id` 
UNION 
SELECT `ci`.`name` AS `Villes`, `c`.`name` AS `Pays` 
FROM `countries` AS `c` 
LEFT JOIN `cities` AS `ci` ON `ci`.`country_id` = `c`.`id`;
```
       
23. Sélectionner les noms des continents et les pays associés (FULL JOIN)
```sql
SELECT `r`.`name` AS `Continents`, `c`.`name` AS `Pays` 
FROM `regions` AS `r` 
FULL JOIN `countries` AS `c` ON `r`.`id` = `c`.`region_id`;
```

VERSION MySQL Workbench : 
```sql
SELECT `r`.`name` AS `Continents`, `c`.`name` AS `Pays` 
FROM `regions` AS `r` 
LEFT JOIN `countries` AS `c` ON `r`.`id` = `c`.`region_id` 
UNION 
SELECT `r`.`name` AS `Continents`, `c`.`name` AS `Pays` 
FROM `countries` AS `c` 
RIGHT JOIN `regions` AS `r` ON `r`.`id` = `c`.`region_id`;
```
       
24. Sélectionner les noms des villes et leurs pays associés avec une latitude supérieure à 40 degrés (FULL JOIN)
```sql
SELECT `ci`.`name` AS `Villes`, `c`.`name` AS `Pays` 
FROM `cities` AS `ci` 
FULL JOIN `countries` AS `c` ON `ci`.`country_id` = `c`.`id` 
WHERE `ci`.`latitude` > 40 
OR `c`.`latitude` > 40;
```

VERSION MySQL Workbench :
```sql
SELECT `ci`.`name` AS `Villes`, `c`.`name` AS `Pays` 
FROM `cities` AS `ci` 
LEFT JOIN `countries` AS `c` ON `ci`.`country_id` = `c`.`id` 
AND (
    `ci`.`latitude` > 40 
    OR `c`.`latitude` > 40
    ) 
UNION 
SELECT `ci`.`name` AS `Villes`, `c`.`name` AS `Pays` 
FROM `countries` AS `c` 
LEFT JOIN `cities` AS `ci` ON `ci`.`country_id` = `c`.`id` 
AND (
    `ci`.`latitude` > 40 
    OR `c`.`latitude` > 40
    );
```
       
25. Sélectionner les pays ayant la même latitude que d'autres pays (SELF JOIN)
```sql
SELECT `c1`.`id` AS `Pays_id_1`, `c2`.`id` AS `Pays_id_2`, `c1`.`name` AS `Pays` 
FROM `countries` AS `c1` 
LEFT OUTER JOIN `countries` AS `c2` ON `c1`.`latitude` = `c2`.`latitude` 
AND `c1`.`id` != `c2`.`id`;
```
       
26. Sélectionner les États partageant le même pays avec d'autres États (SELF JOIN)
```sql
SELECT `s1`.`id` AS `Etat_id_1`, `s2`.`id` AS `Etat_id_2`, `s1`.`name` AS `États` 
FROM `states` AS `s1` 
RIGHT JOIN `states` AS `s2` ON `s1`.`country_id` = `s2`.`country_id` 
AND `s1`.`id` != `s2`.`id`;
```
       
27. Sélectionner les villes partageant le même nom avec d'autres villes (SELF JOIN)
```sql
SELECT `ct1`.`id` AS `Ville_id_1`, `ct2`.`id` AS `Ville_id_2`, `ct1`.`name` AS `Villes` 
FROM `cities` AS `ct1` 
LEFT JOIN `cities` AS `ct2` ON `ct1`.`name` = `ct2`.`name` 
AND `ct1`.`id` != `ct2`.`id`;
```
       