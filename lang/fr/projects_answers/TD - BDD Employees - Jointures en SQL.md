## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre


1. Sélectionner les noms, prénoms et numéros des employés et leur département actuel (INNER JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `e`.`emp_no`, `d`.`dept_name` 
FROM `employees` AS `e` 
INNER JOIN `dept_emp` AS `de` ON `e`.`emp_no` = `de`.`emp_no` 
INNER JOIN `departments` AS `d` ON `de`.`dept_no` = `d`.`dept_no`;
```
       
2. Sélectionner les prénoms, noms et titres actuels des employés (INNER JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `t`.`title` 
FROM `employees` AS `e` 
INNER JOIN `titles` AS `t` ON `e`.`emp_no` = `t`.`emp_no`;
```
       
4. Sélectionner les noms, prénoms et salaires des employés en Juin 1989 (INNER JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `s`.`salary` 
FROM `employees` AS `e` 
INNER JOIN `salaries` AS `s` ON `e`.`emp_no` = `s`.`emp_no` 
AND (
    `s`.`from_date` LIKE '1989%' 
    AND `s`.`to_date` LIKE '1989%'
    );
```
       
5. Sélectionner les noms, prénoms et départements actuels des managers (INNER JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `d`.`dept_name` 
FROM `employees` AS `e` 
INNER JOIN `dept_manager` AS `dm` ON `e`.`emp_no` = `dm`.`emp_no` 
INNER JOIN `departments` AS `d` ON `dm`.`dept_no` = `d`.`dept_no`;
```
       
6. Sélectionner les noms, prénoms et dates de début d'emploi des employés avec leur département (INNER JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `e`.`hire_date`, `d`.`dept_name` 
FROM `employees` AS `e` 
INNER JOIN `dept_emp` AS `de` ON `e`.`emp_no` = `de`.`emp_no` 
INNER JOIN `departments` AS `d` ON `de`.`dept_no` = `d`.`dept_no`;
```
       
7. Sélectionner les noms et départements des employés ayant le même département que les managers ayant été embauchés après le 1er Janvier 1996 (INNER JOIN et Sous-requêtes)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `d`.`dept_name` 
FROM `employees` AS `e` 
INNER JOIN `dept_emp` AS `de` ON `e`.`emp_no` = `de`.`emp_no` 
JOIN `departments` AS `d` ON `de`.`dept_no` = `d`.`dept_no` 
WHERE `de`.`dept_no` IN (
    SELECT `dept_no` 
    FROM `dept_manager` 
    WHERE `from_date` > '1996-01-01'
    );
```
       
8. Sélectionner les employés et leur date d'embauche dans les départements où le salaire moyen est supérieur à 80000 (INNER JOIN et Sous-requêtes)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `e`.`hire_date` 
FROM `employees` AS `e` 
INNER JOIN `dept_emp` AS `de` ON `e`.`emp_no` = `de`.`emp_no` 
WHERE `de`.`dept_no` IN (
    SELECT `de`.`dept_no` 
    FROM `dept_emp` AS `de` 
    JOIN `salaries` AS `s` ON `de`.`emp_no` = `s`.`emp_no` 
    GROUP BY `de`.`dept_no` 
    HAVING AVG(`s`.`salary`) > 80000
    );
```
       
9. Sélectionner les employés et les départements (CROSS JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `d`.`dept_name` 
FROM `employees` AS `e` 
CROSS JOIN `departments` AS  `d`;
```
       
10. Sélectionner les postes actuels des employés avec les noms des départements (CROSS JOIN)
```sql
SELECT `e`.`emp_no`, `t`.`title`, `d`.`dept_name` 
FROM `employees` AS `e` 
CROSS JOIN `titles` AS `t` 
CROSS JOIN `departments` AS `d` 
WHERE `e`.`emp_no` = `t`.`emp_no`;
```
       
11. Sélectionner les dates d'emploi des employés et les noms des départements (JOIN et CROSS JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `de`.`from_date`, `de`.`to_date`, `d`.`dept_name`
FROM `employees` AS `e`
JOIN `dept_emp` AS `de` ON `e`.`emp_no` = `de`.`emp_no`
CROSS JOIN `departments` AS `d`;
```

12. Sélectionner les noms, prénoms, dates d’embauche et départements des employés même s’ils n’ont pas de département associé (LEFT JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `e`.`hire_date`, `d`.`dept_name` 
FROM `employees` AS `e` 
LEFT JOIN `dept_emp` AS `de` ON `e`.`emp_no` = `de`.`emp_no` 
LEFT JOIN `departments` AS `d` ON `de`.`dept_no` = `d`.`dept_no`;
```
       
13. Sélectionner les noms, prénoms et titres des employés même s’ils n’ont pas de titre associé (LEFT JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, IFNULL(`t`.`title`, 'Sans titre') AS `Titre` 
FROM `employees` AS `e` 
LEFT JOIN `titles` AS `t` ON `e`.`emp_no` = `t`.`emp_no`;
```
       
14. Sélectionner les noms, prénoms et salaires des employés depuis 1985 (LEFT JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `s`.`salary` 
FROM `employees` AS `e` 
LEFT JOIN `salaries` AS `s` ON `e`.`emp_no` = `s`.`emp_no` 
AND `s`.`from_date` LIKE '1985%';
```

15. Sélectionner les noms, prénoms et départements des employés même s’ils n’ont pas de département associé (RIGHT JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `d`.`dept_name` 
FROM `departments` AS `d` 
RIGHT JOIN `dept_emp` AS `de` ON `d`.`dept_no` = `de`.`dept_no` 
RIGHT JOIN `employees` AS `e` ON `de`.`emp_no` = `e`.`emp_no`;
```
       
16. Sélectionner les noms, prénoms et salaires des employés depuis 1985 (RIGHT JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `s`.`salary` 
FROM `salaries` AS `s` 
RIGHT JOIN `employees` AS `e` ON `s`.`emp_no` = `e`.`emp_no` 
AND `s`.`from_date` LIKE '1985%';
```
       
17. Sélectionner les noms, prénoms et titres des employés même s’ils n’ont pas de titre associé (RIGHT JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, IFNULL(`t`.`title`, 'Sans titre') AS `Titre` 
FROM `titles` AS `t` 
RIGHT JOIN `employees` AS `e` ON `t`.`emp_no` = `e`.`emp_no`;
```
       
18. Sélectionner les noms, prénoms et départements des employés même s’ils n’ont pas de département associé (FULL JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `d`.`dept_name` 
FROM `employees` AS `e` 
FULL JOIN `dept_emp` AS `de` ON `e`.`emp_no` = `de`.`emp_no` 
FULL JOIN `departments` AS `d` ON `de`.`dept_no` = `d`.`dept_no`;
```

VERSION MySQL Workbench :
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `d`.`dept_name` 
FROM `employees` AS `e` 
LEFT JOIN `dept_emp` AS `de` ON `e`.`emp_no` = `de`.`emp_no` 
LEFT JOIN `departments` AS `d` ON `de`.`dept_no` = `d`.`dept_no` 
UNION 
SELECT `e`.`first_name`, `e`.`last_name`, `d`.`dept_name` 
FROM `departments` AS `d` 
RIGHT JOIN `dept_emp` AS `de` ON `d`.`dept_no` = `de`.`dept_no` 
RIGHT JOIN `employees` AS `e` ON `de`.`emp_no` = `e`.`emp_no`;
```
       
19. Sélectionner les noms, prénoms et salaires des employés depuis 1985 (FULL JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `s`.`salary` 
FROM `employees` AS `e` 
FULL JOIN `salaries` AS `s` ON `e`.`emp_no` = `s`.`emp_no` 
AND `s`.`from_date` LIKE '1985%';
```

VERSION MySQL Workbench :
```sql
SELECT `e`.`first_name`, `e`.`last_name`, `s`.`salary` 
FROM `employees` AS `e` 
LEFT JOIN `salaries` AS `s` ON `e`.`emp_no` = `s`.`emp_no` 
AND `s`.`from_date` LIKE '1985%' 
UNION 
SELECT `e`.`first_name`, `e`.`last_name`, `s`.`salary` 
FROM `salaries` AS `s` 
RIGHT JOIN `employees` AS `e` ON `s`.`emp_no` = `e`.`emp_no` 
AND `s`.`from_date` LIKE '1985%';
```
       
20. Sélectionner les noms, prénoms et titres des employés même s’ils n’ont pas de titre associé (FULL JOIN)
```sql
SELECT `e`.`first_name`, `e`.`last_name`, IFNULL(`t`.`title`, 'Sans titre') AS `Titre` 
FROM `employees` AS `e` 
FULL JOIN `titles` AS `t` ON `e`.`emp_no` = `t`.`emp_no`;
```

VERSION MySQL Workbench :
```sql
SELECT `e`.`first_name`, `e`.`last_name`, IFNULL(`t`.`title`, 'Sans titre') AS `Titre` 
FROM `employees` AS `e` 
LEFT JOIN `titles` AS `t` ON `e`.`emp_no` = `t`.`emp_no` 
UNION 
SELECT `e`.`first_name`, `e`.`last_name`, IFNULL(`t`.`title`, 'Sans titre') AS `Titre` 
FROM `titles` AS `t` 
RIGHT JOIN `employees` AS `e` ON `t`.`emp_no` = `e`.`emp_no`;
```
       
21. Sélectionner les managers ayant le même département que d'autres managers (SELF JOIN)
```sql
SELECT `dm1`.`emp_no` AS `emp_id_1`, `dm2`.`emp_no` AS `emp_id_2`, `dm1`.`dept_no` 
FROM `dept_manager` AS `dm1` 
LEFT OUTER JOIN `dept_manager` AS `dm2` ON `dm1`.`dept_no` = `dm2`.`dept_no` 
AND `dm1`.`emp_no` != `dm2`.`emp_no`;
```
       
22. Sélectionner les managers ayant la même date d’embauche que d'autres managers (SELF JOIN)
```sql
SELECT `dm1`.`emp_no` AS `emp_id_1`, `dm2`.`emp_no` AS `emp_id_2`, `dm1`.`from_date` 
FROM `dept_manager` AS `dm1` 
LEFT OUTER JOIN `dept_manager` AS `dm2` ON `dm1`.`from_date` = `dm2`.`from_date` 
AND `dm1`.`emp_no` != `dm2`.`emp_no`;
```
       
23. Sélectionner les informations sur les employés et leurs salaires (NATURAL JOIN)
```sql
SELECT * 
FROM `employees` 
NATURAL JOIN `salaries`;
```
       
24. Sélectionner les informations sur les employés managers (NATURAL JOIN)
```sql
SELECT * 
FROM `employees` 
NATURAL JOIN `dept_manager`;
```
       
25. Sélectionner les informations sur les employés managers et leur département (NATURAL JOIN)
```sql
SELECT * 
FROM `employees` 
NATURAL JOIN `dept_manager` 
NATURAL JOIN `departments`;
```
       
26. Sélectionner les identifiants, noms et prénoms des employés et la somme de leur salaire par identifiant (NATURAL JOIN)
```sql
SELECT `e`.`emp_no`, `e`.`last_name`, `e`.`first_name`, SUM(`s`.`salary`) 
FROM `employees` AS `e` 
NATURAL JOIN `salaries` AS `s` 
GROUP BY `e`.`emp_no`;
```
       
27. Sélectionner la somme des salaires par département (NATURAL JOIN)
```sql
SELECT `d`.`dept_no`, SUM(`s`.`salary`) AS `Salaires` 
FROM `employees` AS `e` 
NATURAL JOIN `dept_emp` AS `de` 
NATURAL JOIN `salaries` AS `s` 
NATURAL JOIN `departments` AS `d` 
GROUP BY `d`.`dept_no`;
```
       