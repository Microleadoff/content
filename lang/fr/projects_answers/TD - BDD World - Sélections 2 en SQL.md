## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

Les retours à la ligne sont faits pour une meilleure lisibilité

1. Sélectionner le nombre de pays par monnaies
```sql
SELECT `currency`, COUNT(*) 
FROM `countries` 
GROUP BY `currency`;
```
 
2. Sélectionner la latitude maximum et minimum des villes
```sql
SELECT MAX(`latitude`), MIN(`latitude`) 
FROM `countries`;
```
 
3. Sélectionner la latitude maximum et minimum des villes par pays
```sql
SELECT `country_code`, MAX(`latitude`), MIN(`latitude`) 
FROM `cities` 
GROUP BY `country_code`;
```
 
4. Sélectionner la moyenne de latitude des villes par pays
```sql
SELECT `country_code`, AVG(`latitude`) 
FROM `cities` 
GROUP BY `country_code`;
```
 
5. Sélectionner la moyenne de latitude des villes par pays si leur code contient un « A »
```sql
SELECT `country_code`, AVG(`latitude`) 
FROM `cities` 
WHERE `country_code` LIKE '%A%' 
GROUP BY `country_code`;
```

6. Sélectionner le nombre de villes par pays avec un résumé général
```sql
SELECT `country_code`, COUNT(*) 
FROM `cities` 
GROUP BY `country_code` WITH ROLLUP;
```

7. Sélectionner le nombre de villes par pays si leur identifiant d’État est compris entre 10 et 150
```sql
SELECT `country_code`, COUNT(*) 
FROM `cities` 
WHERE `state_id` BETWEEN 10 AND 150 
GROUP BY `country_code`;
```
 
8. Sélectionner la moyenne, le maximum et le minimum des latitudes des villes par pays si leur identifiant d’État est compris entre 10 et 150 avec un résumé général
```sql
SELECT `country_code`, AVG(`latitude`), MAX(`latitude`) , MIN(`latitude`) 
FROM `cities` 
WHERE `state_id` BETWEEN 10 AND 150 
GROUP BY `country_code` WITH ROLLUP;
```
 
9. Sélectionner le nombre de villes pour les pays ayant les codes « ES » et « FR »
```sql
SELECT `country_code`, COUNT(*) 
FROM `cities` 
WHERE `country_code` IN ('ES', 'FR') 
GROUP BY `country_code`;
```
 
10. Sélectionner le nombre de villes par pays s’il est supérieur à 50000
```sql
SELECT `country_code`, COUNT(*) 
FROM `cities` 
GROUP BY `country_code` 
HAVING COUNT(*) > 5000;
```
 
11. Sélectionner la moyenne de latitude des villes par pays si elle est comprise entre 20 et 25
```sql
SELECT `country_code`, AVG(`latitude`) 
FROM `cities` 
GROUP BY `country_code` 
HAVING AVG(`latitude`) > 20 
AND AVG(`latitude`) < 25;
```

12. Sélectionner la liste des pays en ordre alphabétique inversé de nom
```sql
SELECT * 
FROM `countries` 
ORDER BY `name` DESC;
```
 
13. Sélectionner la liste des villes en ordre alphabétique inversé de code de pays et en ordre alphabétique par code d’État
```sql
SELECT * 
FROM `cities` 
ORDER BY `country_code` DESC, `state_code` ASC;
```
 
14. Sélectionner le nombre de villes par pays du plus petit au plus grand
```sql
SELECT `country_code`, COUNT(*) 
FROM `cities` 
GROUP BY `country_code` 
ORDER BY COUNT(*) ASC;
```
 
15. Sélectionner la latitude moyenne, maximum et minimum des villes par pays, utiliser des alias
```sql
SELECT `country_code`, AVG(`latitude`) AS `Latitude Moyenne`, MAX(`latitude`) AS `Latitude Max`, MIN(`latitude`) AS `Latitude Min` 
FROM `cities` 
GROUP BY `country_code`;
```
 
16. Sélectionner les 10 premiers pays
```sql
SELECT * 
FROM `countries` 
LIMIT 10;
```
 
17. Sélectionner les noms des 10 premiers pays, utiliser des alias
```sql
SELECT `name` AS `Pays` 
FROM `countries` 
LIMIT 10;
```
 
18. Sélectionner 10 pays à partir du 5ème
```sql
SELECT * 
FROM `countries` 
LIMIT 5, 10;
```
 
19. Sélectionner les noms des 10 premiers pays en ordre alphabétique inversé de nom
```sql
SELECT `name` 
FROM `countries` 
ORDER BY `name` DESC 
LIMIT 10;
```
 
20. Sélectionner le nombre de pays par monnaie pour les 10 premières monnaies si leur nombre est supérieur à 2, utiliser des alias
```sql
SELECT `currency` AS `Monnaie`, COUNT(`name`) AS `Nombre de Pays` 
FROM `countries` 
GROUP BY `currency` 
HAVING COUNT(`name`) > 2 
LIMIT 10;
```
 
21. Sélectionner le nombre de villes par pays si leur latitude est comprise entre 10 et 50 et le nombre est supérieur à 1000
```sql
SELECT `country_code`, COUNT(*) 
FROM `cities` 
WHERE `latitude` BETWEEN 10 AND 50 
GROUP BY `country_code` 
HAVING COUNT(*) > 1000;
```
 
22. Sélectionner le nombre de villes par pays si leur code d’État contient un « Z » et le nombre est inférieur à 1000
```sql
SELECT `country_code`, COUNT(*) 
FROM `cities` 
WHERE `state_code` LIKE '%Z%' 
GROUP BY `country_code` 
HAVING COUNT(*) < 1000;
```

23. Sélectionner les noms des pays et afficher les catégories de monnaie EUR = « Euro », USD = « Dollars », Les autres = « Autre monnaie »
```sql
SELECT `name`,
CASE `currency`
 	WHEN 'EUR' THEN 'Euro'
	WHEN 'USD' THEN 'Dollars'
	ELSE 'Autres monnaies'
END 
FROM `countries`;
```
 
24. Sélectionner le nombre de pays par monnaie ayant un résultat supérieur ou égal à 2 et afficher les catégories : supérieur à 5 = « Très élevé », supérieur à 3 = « Élevé », inférieur à 3 = « Moyen », utiliser des alias
```sql
SELECT `currency`, COUNT(*),
CASE
	WHEN COUNT(*) > 5 THEN 'Très élevé'
	WHEN COUNT(*) >= 3 THEN 'Élevé'
	WHEN COUNT(*) < 3 THEN 'Moyen'
END AS `Nombre de Pays`
FROM `countries` 
GROUP BY `currency` 
HAVING COUNT(*) >= 2;
```
 
25. Sélectionner les moyennes des latitudes des villes par pays si le code pays contient un « A » comme deuxième lettre et afficher les catégories : supérieur à 10 = « Nord », inférieur à -10 = « Sud », compris entre 10 et -10 = « Équateur », utiliser des alias
```sql
SELECT `country_code`, AVG(`latitude`),
CASE
	WHEN AVG(`latitude`) > 10 THEN 'Nord'
	WHEN AVG(`latitude`) < -10 THEN 'Sud'
	WHEN 10 >= AVG(`latitude`) >= -10 THEN 'Équateur'
END AS `Latitude`
FROM `cities` 
WHERE `country_code` LIKE '_A%' 
GROUP BY `country_code`;
```