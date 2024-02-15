## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre


1. Sélectionner les identifiants et codes de pays des villes et des états sans doublon
```sql
SELECT `country_id`, `country_code` 
FROM `cities`
UNION 
SELECT `country_id`, `country_code` 
FROM `states`;
```
 
2. Sélectionner les identifiants, noms et dates de créations des continents des tables : continent (regions) et pays (countries) si l’identifiant du continent est compris entre 1 et 3 sans doublon
```sql
SELECT `id`, `name`, `created_at` 
FROM `regions` 
WHERE `id` BETWEEN 1 AND 3
UNION
SELECT `region_id`, `region`, `created_at` 
FROM `countries` 
WHERE `region_id` BETWEEN 1 AND 3;
```
 
3. Sélectionner les identifiants et codes de pays des villes et des états si les codes de pays contiennent la lettre « A » sans doublon
```sql
SELECT `country_id`, `country_code` F
ROM `cities` 
WHERE `country_code` LIKE '%A%'
UNION
SELECT `country_id`, `country_code` 
FROM `states` 
WHERE `country_code` LIKE '%A%';
```
 
4. Sélectionner les identifiants et dates de création des continents et sous-continents si les identifiants sont compris entre 1 et 10 sans doublon
```sql
SELECT `id`, `created_at` 
FROM `regions` 
WHERE `id`BETWEEN 1 AND 10
UNION
SELECT `id`, `created_at` 
FROM `subregions` 
WHERE `id`BETWEEN 1 AND 10;
```
 
5. Sélectionner les identifiants et codes de pays des villes et des états si les codes de pays sont compris entre 1 et 10 
```sql 
SELECT `country_code`, COUNT( `country_id`) 
FROM `cities` 
WHERE `country_id` BETWEEN 1 AND 10 
GROUP BY `country_code`
UNION 
SELECT `country_code`, COUNT( `country_id`) 
FROM `states` 
WHERE `country_id` BETWEEN 1 AND 10 
GROUP BY `country_code`;
```
 
6. Sélectionner les identifiants et codes de pays des villes et des états avec possibles doublons
```sql
SELECT `country_id`, `country_code` 
FROM `cities`
UNION ALL
SELECT `country_id`, `country_code` 
FROM `states`;
```

7. Sélectionner les identifiants, noms et dates de créations des continents tables : continent (regions) et pays (countries) si l’identifiant du continent est compris entre 1 et 3 avec possibles doublons
```sql
SELECT `id`, `name`, `created_at` 
FROM `regions` 
WHERE `id`BETWEEN 1 AND 3
UNION ALL
SELECT `region_id`, `region`, `created_at` 
FROM `countries` 
WHERE `region_id` BETWEEN 1 AND 3;
```

8. Sélectionner les identifiants et codes de pays des villes et des états si les codes de pays contiennent la lettre « A » avec possibles doublon
```sql
SELECT `country_id`, `country_code` 
FROM `cities` 
WHERE `country_code` LIKE '%A%'
UNION ALL
SELECT `country_id`, `country_code` 
FROM `states` 
WHERE `country_code` LIKE '%A%';
```

9. Sélectionner les identifiants et dates de création des continents et sous-continents si les identifiants sont compris entre 1 et 10 avec possibles doublons
```sql
SELECT `id`, `created_at` 
FROM `regions` 
WHERE `id` BETWEEN 1 AND 10
UNION ALL
SELECT `id`, `created_at` 
FROM `subregions` 
WHERE `id` BETWEEN 1 AND 10;
```
 
10. Sélectionner les pays dont les identifiants correspondent à ceux référencés dans la table des villes (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT * 
FROM `countries`
WHERE `id` IN (
	SELECT `country_id`
 	FROM `cities`
);
```

11. Sélectionner les pays dont les identifiants correspondent à ceux référencés dans la table des villes si le code ISO2 du pays termine par un « E » (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT * 
FROM `countries`
WHERE `id` IN (
 	SELECT `country_id`
 	FROM `cities`
)
AND `iso2` LIKE "%E";
```

12. Sélectionner les États dont les identifiants correspondent à ceux référencés dans la table des villes (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT * 
FROM `states`
WHERE `id` IN (
 	SELECT `country_id`
 	FROM `cities`
);
```
 
13. Sélectionner les états dont les identifiants correspondent à ceux des pays référencés dans les 200 premières entrées de la table des villes (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT * 
FROM `states`
WHERE `id` IN (
 	SELECT `country_id`
 	FROM `cities`
 WHERE `id` BETWEEN 1 AND 200
);
```

14. Sélectionner les identifiants et les codes ISO2 des pays en excluant ceux qui sont dans la table des villes (EXCEPT)
```sql
SELECT `id`, `iso2` 
FROM `countries`
EXCEPT
SELECT `country_id`, `country_code` 
FROM `cities`;
```

15. Sélectionner les identifiants et les codes des pays de la table des États en excluant ceux qui sont dans la table des villes (EXCEPT)
```sql
SELECT `country_id`, `country_code` 
FROM `states`
EXCEPT
SELECT `country_id`, `country_code` 
FROM `cities`;
```