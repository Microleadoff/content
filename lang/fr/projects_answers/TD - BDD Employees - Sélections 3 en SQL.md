## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre


1. Sélectionner les employés et managers des départements sans doublons
```sql
SELECT * 
FROM `dept_emp` 
UNION 
SELECT * 
FROM `dept_manager`;
```
 
2. Sélectionner les employés et managers du département d001 sans doublon
```sql
SELECT * 
FROM `dept_emp` 
WHERE `dept_no` = 'd001'
UNION
SELECT * 
FROM `dept_manager` 
WHERE `dept_no` = 'd001';
```
 
3. Sélectionner les numéros des employés et managers du département d001 dont l’embauche a été faite en Janvier 1985 sans doublon
```sql
SELECT * 
FROM `dept_emp` 
WHERE `dept_no` = 'd001' 
AND `from_date` LIKE '1985-01%'
UNION 
SELECT * 
FROM `dept_manager` 
WHERE `dept_no` = 'd001' 
AND `from_date` LIKE '1985-01%';
```
 
4. Sélectionner les employés et managers du département d001 dont le numéro d’employé est compris entre 110000 et 120000 sans doublon
```sql
SELECT * 
FROM `dept_emp` 
WHERE `dept_no` = 'd001' 
AND `emp_no` BETWEEN 110000 AND 120000
UNION
SELECT * 
FROM `dept_manager` 
WHERE `dept_no` = 'd001' 
AND `emp_no` BETWEEN 110000 AND 120000;
```
 
5. Sélectionner le nombre d’employés et de manager par départements
```sql
SELECT `dept_no`, COUNT(*) 
FROM `dept_emp` 
GROUP BY `dept_no`
UNION
SELECT `dept_no`, COUNT(*) 
FROM `dept_manager` 
GROUP BY `dept_no`;
```
 
6. Sélectionner les employés et managers du département d001 avec possibles doublons
```sql
SELECT * 
FROM `dept_emp` 
WHERE `dept_no` = 'd001'
UNION ALL
SELECT * 
FROM `dept_manager` 
WHERE `dept_no` = 'd001';
```
 
7. Sélectionner les employés et managers du département d001 dont le numéro d’employé est compris entre 110000 et 120000 avec possibles doublons
```sql
SELECT * 
FROM `dept_emp` 
WHERE `dept_no` = 'd001' 
AND `emp_no` BETWEEN 110000 AND 120000
UNION ALL
SELECT * 
FROM `dept_manager` 
WHERE `dept_no` = 'd001' 
AND `emp_no` BETWEEN 110000 AND 120000;
```
 
8. Sélectionner les numéros des employés et managers du département d001 dont l’embauche a été faite en Janvier 1985 avec possibles doublons
```sql
SELECT * 
FROM `dept_emp` 
WHERE `dept_no` = 'd001' 
AND `from_date` LIKE '1985-01%'
UNION ALL
SELECT * 
FROM `dept_manager` 
WHERE `dept_no` = 'd001' 
AND `from_date` LIKE '1985-01%';
```

9. Sélectionner les employés qui ont été ou sont managers de département (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT * 
FROM `dept_emp`
WHERE `emp_no` IN (
 	SELECT `emp_no`
 	FROM `dept_manager`
);
```

10. Sélectionner les employés qui ont été ou sont managers du département « d001 » (INTERSECT - VERSION MySQL Workbench)
```sql
SELECT DISTINCT * 
FROM `dept_emp`
WHERE `emp_no` IN (
 	SELECT `emp_no`
 	FROM `dept_manager`
	WHERE `dept_no` = 'd001'
);	
```

11. Sélectionner le nombre d’employés par département qui ont été ou sont managers, utiliser des alias (INTERSECT - VERSION MySQL Workbench)
```sql	
SELECT DISTINCT `dept_no` AS `Département`, COUNT( `emp_no`) AS `Nombre` 
FROM `dept_emp` 
WHERE `emp_no` IN (
    SELECT `emp_no`
    FROM `dept_manager`
)
GROUP BY `dept_no`;	
```
 
12. Sélectionner le nombre d’employés par département qui ont été ou sont managers en 1988, utiliser des alias (INTERSECT - VERSION MySQL Workbench)
```sql	
SELECT DISTINCT `dept_no` AS `Département`, COUNT( `emp_no`) AS `Nombre` 
FROM `dept_emp` 
WHERE `emp_no` IN (
    SELECT `emp_no`
    FROM `dept_manager`
    WHERE `from_date` LIKE '1988%'
)
GROUP BY `dept_no`;	
```

13. Sélectionner les employés des départements en excluant ceux qui ont été ou sont managers (EXCEPT)
```sql
SELECT * 
FROM `dept_emp`
EXCEPT
SELECT * 
FROM `dept_manager`;
```
 
14. Sélectionner les employés par département si leur numéro est compris entre 110000 et 120000 en excluant ceux qui ont été ou sont managers (EXCEPT)
```sql
SELECT `dept_no`, COUNT(*) 
FROM `dept_emp` 
WHERE `emp_no` BETWEEN 110000 AND 120000 
GROUP BY `dept_no`
EXCEPT
SELECT `dept_no`, COUNT(*) 
FROM `dept_manager` 
GROUP BY `dept_no`;
```
 
15. Sélectionner les départements et les employés qui ont été ou sont managers en excluant les employés du département « d004 » (EXCEPT)
```sql
SELECT `dept_no`, `emp_no` 
FROM `dept_manager`
EXCEPT 
SELECT `dept_no`, `emp_no` 
FROM `dept_emp` 
WHERE `dept_no` = 'd004';
```