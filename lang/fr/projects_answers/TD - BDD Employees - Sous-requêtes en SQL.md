## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre


1. Sélectionner les prénoms et noms des employés qui ne sont pas ou n’ont pas été managers, utiliser des alias 
```sql
SELECT `first_name` AS `Prénom`, `last_name` AS `Nom` 
FROM `employees` 
WHERE `emp_no` NOT IN (
    SELECT `emp_no` 
    FROM `dept_manager`
    );
```
       
2. Sélectionner les prénoms et noms  des employés qui ont eu plus de 2 titres professionnels différents
```sql
SELECT `first_name` , `last_name` 
FROM `employees` 
WHERE `emp_no` IN (
    SELECT `emp_no` 
    FROM `titles` 
    GROUP BY `emp_no` 
    HAVING COUNT(DISTINCT `title`) > 2
    );
```
       
3. Sélectionner les numéros, prénoms et noms des employés qui ont eu un salaire compris entre 100000 et 150000
```sql
SELECT `emp_no`, `first_name`, `last_name` 
FROM `employees` 
WHERE `emp_no` IN (
    SELECT `emp_no` 
    FROM `salaries` 
    WHERE `salary` BETWEEN 100000 AND 150000
    );
```
       
4. Sélectionner les numéros, prénoms et noms des employés qui ont eu un salaire supérieur à 150000 et qui ne sont pas  ou n’ont pas été managers 
```sql
SELECT `emp_no`, `first_name`, `last_name` 
FROM `employees` 
WHERE `emp_no` IN (
    SELECT `emp_no` 
    FROM `salaries` 
    WHERE `salary` > 150000 
    )
AND `emp_no` NOT IN (
    SELECT `emp_no` 
    FROM `dept_manager`
    );
```
       
5. Sélectionner les numéros des employés managers qui ont un salaire inférieur à 100000 et qui ont eu plus de 2 titres professionnels 
```sql
SELECT `emp_no` 
FROM `dept_manager` 
WHERE `emp_no` IN (
    SELECT `emp_no` 
    FROM `salaries` 
    WHERE `salary` < 100000
    ) 
AND `emp_no` IN (
    SELECT `emp_no` 
    FROM `titles` 
    GROUP BY `emp_no` 
    HAVING COUNT(DISTINCT `title`) > 2
    );
```
       
6. Sélectionner les noms des employés ayant été managers d'un département, utiliser des alias pour les résultats et l’appel des tables (EXISTS)
```sql
SELECT `e`.`last_name` AS `Nom` 
FROM `employees` AS `e` 
WHERE EXISTS (
    SELECT `dm`.`emp_no` 
    FROM `dept_manager` AS `dm` 
    WHERE `e`.`emp_no` = `dm`.`emp_no`
    );
```
       
7. Sélectionner les noms des employés pour qui il existe un salaire supérieur à 100000, utiliser des alias pour les résultats et l’appel des tables (EXISTS)
```sql
SELECT `e`.`last_name` AS `Nom`, `e`.`first_name` AS `Prénom` 
FROM `employees` AS `e`
WHERE EXISTS (
    SELECT `s`.`emp_no` 
    FROM `salaries` AS `s` 
    WHERE `e`.`emp_no` = `s`.`emp_no` 
    AND `s`.`salary` > 100000
    );
```
       
8. Sélectionner les noms des employés féminins ayant occupé un poste de manager, utiliser des alias (EXISTS)
```sql
SELECT `e`.`last_name` AS `Nom`, `e`.`first_name` AS `Prénom` 
FROM `employees` AS e 
WHERE `gender` = 'F' 
AND EXISTS (
    SELECT `dm`.`emp_no` 
    FROM `dept_manager` AS `dm` 
    WHERE `e`.`emp_no` = `dm`.`emp_no`
    );
```
       
9. Sélectionner les noms et prénoms des employés ayant eu un salaire supérieur à 100000, utiliser des alias (EXISTS)
```sql
SELECT `e`.`first_name`, `e`.`last_name` 
FROM `employees` AS `e` 
WHERE EXISTS (
    SELECT `s`.`emp_no` 
    FROM `salaries` AS `s` 
    WHERE `s`.`emp_no` = `e`.`emp_no` 
    AND `s`.`salary` > 150000
    );
```
       
10. Sélectionner les numéros, noms et prénoms des employés nés le 1er janvier 1960 pour qui il existe exactement deux titres professionnels différents au cours de leur carrière, utiliser des alias (EXISTS)
```sql
SELECT `e`.`emp_no`, `e`.`first_name`, `e`.`last_name` 
FROM `employees` AS `e` 
WHERE `e`.`birth_date` LIKE '1960-01-01%' 
AND EXISTS (
    SELECT `t`.`emp_no` 
    FROM `titles` AS `t` 
    WHERE `e`.`emp_no` = `t`.`emp_no` 
    GROUP BY t.`emp_no` 
    HAVING COUNT(DISTINCT `t`.`title`) = 2
    );
```
       
11. Sélectionner les employés dont la date d'embauche est supérieure ou égale à la dernière prise de poste de manager, utiliser des alias (ALL)
```sql
SELECT `e`.* 
FROM `employees` AS `e` 
WHERE `hire_date` >= ALL (
    SELECT MAX(`d`.`from_date`) 
    FROM `dept_manager` AS `d` 
    WHERE `d`.`emp_no` = `e`.`emp_no`
    );
```
       
12. Sélectionner l’identifiant de l’employé dont le salaire est le plus élevé, utiliser des alias (ALL)
```sql
SELECT `emp_no` 
FROM `salaries` 
GROUP BY `emp_no` 
HAVING MAX(`salary`) >= ALL (
    SELECT MAX(`salary`) 
    FROM `salaries` 
    GROUP BY `emp_no`
    );
```
       
13. Sélectionner le titre le plus donné aux employés (ALL)
```sql
SELECT `title`, COUNT(*) 
FROM `titles` 
GROUP BY `title` 
HAVING COUNT(*) >= ALL (
    SELECT COUNT(*) 
    FROM `titles` 
    GROUP BY `title`
    );
```
       
14. Sélectionner les identifiants des employés dont la période d'emploi est plus longue que celle des autres employés (ALL)
```sql
SELECT `emp_no` 
FROM `dept_emp` 
GROUP BY `emp_no` 
HAVING DATEDIFF(MAX(`to_date`), MIN(`from_date`)) >= ALL (
    SELECT DATEDIFF(MAX(`to_date`), MIN(`from_date`)) 
    FROM `dept_emp` 
    GROUP BY `emp_no`
    );
```
       
15. Sélectionner les employés qui ont le titre le plus fréquemment donné (ALL)
```sql
SELECT * 
FROM `employees` 
WHERE `emp_no` IN (
    SELECT `emp_no` 
    FROM `titles` 
    GROUP BY `emp_no` 
    HAVING COUNT(*) >= ALL (
        SELECT COUNT(*) 
        FROM `titles` 
        GROUP BY `emp_no`
        )
    );
```
       
16. Sélectionner les titres des employés ayant au moins un salaire supérieur à 150000$, utiliser des alias (ANY)
```sql
SELECT DISTINCT `t`.`title` AS `Titre_de_l_employé` 
FROM `titles` AS `t` 
WHERE `t`.`emp_no` = ANY (
    SELECT `s`.`emp_no` 
    FROM `salaries` AS `s` 
    WHERE `s`.`salary` > 150000
    );
```
       
17. Sélectionner le nombre d’employés managers (ANY)
```sql
SELECT COUNT(*) 
FROM `employees` 
WHERE `emp_no` = ANY (
    SELECT `emp_no` 
    FROM `dept_manager`
    );
```
       
18. Sélectionner les noms des employés ayant été dans au moins un département et ayant eu un salaire supérieur à 150 000$, utiliser des alias (ANY)
```sql
SELECT * 
FROM `employees` AS `e` 
WHERE `e`.`emp_no` = ANY (
    SELECT `de`.`emp_no` 
    FROM `dept_emp` AS `de` 
    WHERE `de`.`emp_no` = ANY (
        SELECT `s`.`emp_no` 
        FROM `salaries` AS `s` 
        WHERE `s`.`salary` > 150000
        )
    );
```
       
19. Sélectionner les prénoms des employés ayant le titre « Senior Engineer » (ANY)
```sql
SELECT `first_name` 
FROM `employees` 
WHERE `emp_no` = ANY (
    SELECT `emp_no` 
    FROM `titles` 
    WHERE `title` = 'Senior Engineer'
    );
```
       
20. Sélectionner le nombre de salariés ayant un salaire supérieur à la moyenne (ANY)
```sql
SELECT COUNT(*) AS `Nombre_employés` 
FROM `employees` 
WHERE `emp_no` = ANY (
    SELECT `emp_no` 
    FROM `salaries` 
    WHERE `salary` > (
        SELECT AVG(`salary`) 
        FROM `salaries`
        )
    );
```