## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

1. Sélectionner le nombre d’employés par département
```sql
SELECT `dept_no`, COUNT(`emp_no`) 
FROM `dept_emp` 
GROUP BY `dept_no`;
```
 
2. Sélectionner le salaire maximum et minimum des employés
```sql
SELECT MAX(`salary`), MIN(`salary`) 
FROM `salaries`;
```
 
3. Sélectionner le salaire maximum et minimum par employés
```sql
SELECT `emp_no`, MAX(`salary`), MIN(`salary`) 
FROM `salaries`;
```
 
4. Sélectionner la moyenne de salaire par employés
```sql
SELECT `emp_no`, AVG(`salary`) 
FROM `salaries` 
GROUP BY `emp_no`;
```
 
5. Sélectionner la moyenne de salaire par employés si leur numéro contient « 150 »
```sql
SELECT `emp_no`, AVG(`salary`) 
FROM `salaries` 
WHERE `emp_no` LIKE '%150%' 
GROUP BY `emp_no`;
```

6. Sélectionner le nombre d’employés par département avec un résumé général
```sql
SELECT `dept_no`, COUNT(`emp_no`) 
FROM `dept_emp` 
GROUP BY `dept_no` WITH ROLLUP;
```
 
7. Sélectionner le nombre d’employés par département si leur numéro d’employé est compris entre 10000 et 50000
```sql
SELECT `dept_no`, COUNT(`emp_no`) 
FROM `dept_emp` 
WHERE `emp_no` BETWEEN 10000 AND 50000 
GROUP BY `dept_no` ;
```
 
8. Sélectionner la moyenne, le minimum et le maximum des salaires par employé si leur numéro est compris entre 10005 et 10105 avec un résumé général
```sql
SELECT `emp_no`, AVG(`salary`), MIN(`salary`), MAX(`salary`) 
FROM `salaries` 
WHERE `emp_no` BETWEEN 10005 AND 10105 
GROUP BY `emp_no` WITH ROLLUP;
```
 
9. Sélectionner le nombre d’employés par département pour les départements « d005 » et « d006 »
```sql
SELECT `dept_no`, COUNT(`emp_no`) 
FROM `dept_emp` 
WHERE `dept_no` IN ('d005', 'd006') 
GROUP BY `dept_no`;
```
 
10. Sélectionner le nombre d’employés par département s’il est inférieur à 50000
```sql
SELECT `dept_no`, COUNT(`emp_no`) 
FROM `dept_emp` 
GROUP BY `dept_no` 
HAVING COUNT(`emp_no`) < 50000 ;
```
 
11. Sélectionner la moyenne des salaires par employé si elle est comprise entre 40000 et 50000
```sql
SELECT `emp_no`, AVG(`salary`) 
FROM `salaries` 
GROUP BY `emp_no` 
HAVING AVG(`salary`) > 40000 
AND AVG(`salary`) < 50000;
```
 
12. Sélectionner la liste des employées en ordre alphabétique inversé de nom
```sql
SELECT * 
FROM `employees` 
ORDER BY `first_name` DESC;
```
 
13. Sélectionner la liste des employés en ordre alphabétique inversé de nom et en ordre alphabétique par prénom
```sql
SELECT * 
FROM `employees` 
ORDER BY `first_name` DESC, `Last_name` ASC ;
```
 
14. Sélectionner le nombre d’employés par département du plus petit au plus grand
```sql
SELECT `dept_no`, COUNT(`emp_no`) 
FROM `dept_emp` 
GROUP BY `dept_no` 
ORDER BY COUNT(`emp_no`);
```
 
15. Sélectionner le salaire maximum et minimum des employés, utiliser des alias
```sql
SELECT MAX(`salary`) AS `Salaire Maximum`, MIN(`salary`) AS `Salaire Minimum` 
FROM `salaries`;
```
 
16. Sélectionner les 10 premiers employés
```sql
SELECT * 
FROM `employees` 
LIMIT 10;
```
 
17. Sélectionner les noms et prénoms des 10 premiers employés, utiliser des alias
```sql
SELECT `Last_name` AS `Nom`, `first_name` AS `Prénom` 
FROM `employees` 
LIMIT 10;
```
 
18. Sélectionner 10 employés à partir du 5ème
```sql
SELECT * 
FROM `employees` 
LIMIT 5, 10;
```
 
19. Sélectionner les noms et prénoms des 10 premiers employés en ordre alphabétique par nom
```sql
SELECT `Last_name` , `first_name` 
FROM `employees` 
ORDER BY `Last_name` 
LIMIT 10;
```
 
20. Sélectionner la somme des salaires pour les 10 premiers employés si la somme est inférieure à 50000
```sql
SELECT `emp_no`, SUM(`salary`) 
FROM `salaries` 
GROUP BY `emp_no` 
HAVING SUM(`salary`) < 50000 
LIMIT 10;
```
 
21. Sélectionner la somme des salaires par employés si leur numéro est compris entre 10001 et 50000 et la somme est inférieure à 50000
```sql
SELECT `emp_no`, SUM(`salary`) 
FROM `salaries` 
WHERE `emp_no` BETWEEN 10001 AND 50000 
GROUP BY `emp_no` 
HAVING SUM(`salary`) < 50000;
```
 
22. Sélectionner la somme des salaires pour les 10 premiers employés si leur numéro est compris entre 10001 et 50000 et la somme est inférieure à 50000
```sql
SELECT `emp_no`, SUM(`salary`) 
FROM `salaries` 
WHERE `emp_no` BETWEEN 10001 AND 50000 
GROUP BY `emp_no` 
HAVING SUM(`salary`) < 50000 
LIMIT 10;
```

23. Sélectionner les employés et afficher les catégories de département (d001 = « Département n°1 », d002 = « Département n°2 », …, d009 = « Département n°9 » et s’il n’y a pas de département) si le numéro d’employé est compris entre 10150 et 10200
```sql
SELECT `emp_no`,
CASE `dept_no`
    WHEN 'd001' THEN 'Departement n°1'
    WHEN 'd002' THEN 'Departement n°2'
    WHEN 'd003' THEN 'Departement n°3'
    WHEN 'd004' THEN 'Departement n°4'
    WHEN 'd005' THEN 'Departement n°5'
    WHEN 'd006' THEN 'Departement n°6'
    WHEN 'd007' THEN 'Departement n°7'
    WHEN 'd008' THEN 'Departement n°8'
    WHEN 'd009' THEN 'Departement n°9'
    ELSE 'Pas de Département'
END 
FROM `dept_emp` 
WHERE `emp_no` BETWEEN 10150 AND 10200;
```
 
24. Sélectionner le nombre d’employés par département et afficher les catégories : supérieur à 50000 = « Élevé », supérieur ou égale à 20000 = « Correct », inférieur à 20000 = « Faible », utiliser des alias
```sql
SELECT `dept_no`, COUNT(`emp_no`),
CASE
    WHEN COUNT(`emp_no`) > 50000 THEN 'Élevé'
    WHEN COUNT(`emp_no`) >= 20000 THEN 'Correct'
    WHEN COUNT(`emp_no`) < 20000 THEN 'faible'
END AS `Nombre d'employés`
FROM `dept_emp` 
GROUP BY `dept_no`;
```

25. Sélectionner les moyennes des salaires par employés et afficher les catégories : supérieur à 100000 = « Très élevée », supérieur ou égale à 80000 = « Élevée », inférieur à 80000 = « Faible », utiliser des alias
```sql
SELECT `emp_no`,
CASE 
    WHEN AVG(`salary`) > 100000 THEN 'Très élevée'
    WHEN AVG(`salary`) >= 80000 THEN 'Élevée'
    WHEN AVG(`salary`) < 80000 THEN 'Faible'
END AS `Salaire Moyen`
FROM `salaries` 
GROUP BY `emp_no`;
```