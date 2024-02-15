## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre


1. Sélectionner tous les employés
```sql
SELECT * 
FROM `employees`;
```
 
2. Sélectionner tous les employés par leurs noms et prénoms
```sql
SELECT `last_name` , `first_name` 
FROM `employees`;
```
 
3. Sélectionner les noms distincts des employés 
```sql
SELECT DISTINCT `last_name` 
FROM `employees`;
```
 
4. Sélectionner les noms et prénoms distincts des employés 
```sql
SELECT DISTINCT `last_name`, `first_name` 
FROM `employees`;
```
 
5. Sélectionner les noms et prénoms des employés dont le nom est « alencar »
```sql
SELECT `first_name`, `last_name` 
FROM `employees` 
WHERE `last_name` = 'alencar';
```

6. Sélectionner les employés dont le nom est « alencar » et de sexe masculin 
```sql
SELECT * 
FROM `employees` 
WHERE `last_name` = 'alencar' 
AND `gender` = 'M';
```
 
7. Sélectionner les employés dont le prénom « Danai » ou « Leen » en utilisant « OR »
```sql
SELECT * 
FROM `employees` 
WHERE `first_name` = 'danai' 
OR `first_name` = 'leen';
```
 
8. Sélectionner les employés dont le prénom « Danai » ou « Leen » en utilisant « IN »
```sql
SELECT * 
FROM `employees` 
WHERE `first_name` IN ('danai', 'leen');
```
 
9. Sélectionner les employés dont le nom est « alencar » et le prénom « Danai » ou « Leen » en utilisant « OR »
```sql
SELECT * 
FROM `employees` 
WHERE `last_name` = 'alencar' 
AND (
    `first_name` = 'danai' 
    OR `first_name` = 'leen'
    );
```

10. Sélectionner les employés dont le nom est « alencar » et le prénom « Danai » ou « Leen » en utilisant « IN »
```sql
SELECT * 
FROM `employees` 
WHERE `last_name` = 'alencar' 
AND `first_name` IN ('danai', 'leen');
```
 
11. Sélectionner les employés dont le numéro d’employé est compris entre 50000 et 50150
```sql
SELECT * 
FROM `employees` 
WHERE `emp_no` BETWEEN 50000 AND 50150;
```
 
12. Sélectionner les employés dont le nom est « alencar » et le numéro d’employé est compris entre 50000 et 60000
```sql
SELECT * 
FROM `employees` 
WHERE `last_name` = 'alencar' 
AND `emp_no` BETWEEN 50000 AND 60000;
```
 
13. Sélectionner les employés dont le nom est « alencar » et le prénom est « danai » ou le numéro d’employé est compris entre 50000 et 60000 
```sql
SELECT * 
FROM `employees` 
WHERE `last_name` = 'alencar' 
AND (
    `first_name` = 'danai' 
    OR `emp_no` BETWEEN 50000 AND 60000
    );
```
 
14. Sélectionner les employés dont le nom est « alencar » ou, le prénom est « danai » ou « leen » et le numéro d’employé est compris entre 50000 et 60000
```sql
SELECT * 
FROM `employees` 
WHERE `last_name` = 'alencar' 
OR (
    `first_name` IN ('danai', 'leen') 
    AND `emp_no` BETWEEN 50000 AND 60000
    );
```
	
15. Sélectionner les employés dont le prénom commence par un « T » 
```sql
SELECT * 
FROM `employees` 
WHERE `first_name` LIKE 't%'; 
```
 
16. Sélectionner les employés masculin dont la deuxième lettre du prénom est un « T » 
```sql
SELECT * 
FROM `employees` 
WHERE `gender` = 'M' 
AND `first_name` LIKE '_t%' ;
```
 
17. Sélectionner les employés dont le nom est « alencar » et le prénom « danai » ou le numéro d’employé commence par un 5 
```sql
SELECT * 
FROM `employees` 
WHERE `last_name` = 'alencar' 
AND (
    `first_name` = 'danai' 
    OR `emp_no` LIKE '5%'
    );
```
 
18. Sélectionner les employés dont le prénom commence par un « T » et termine par un « B »
```sql
SELECT * 
FROM `employees` 
WHERE `first_name` LIKE 't%b'; 
```
 
19. Sélectionner les employés dont le prénom commence par un « T », la 3ème lettre est un « R »
```sql
SELECT * 
FROM `employees` 
WHERE `first_name` LIKE 't_r%';
```
 
20. Sélectionner les employés dont le prénom commence par un « T », la 3ème lettre est un « R » et le numéro d’employé est compris entre 50000 et 60000 
```sql
SELECT * 
FROM `employees` 
WHERE `first_name` LIKE 't_R%' 
AND `emp_no` BETWEEN 50000 AND 60000;
```
 
21. Sélectionner les employés dont le prénom contient « TZV » 
```sql
SELECT * 
FROM `employees` 
WHERE `first_name` LIKE '%tzv%' ;
```
 
22. Sélectionner les employés masculin ou dont le numéro d’employé est compris entre 50000 et 60000 et, le prénom contient « TZV »
```sql
SELECT * 
FROM `employees` 
WHERE `first_name` LIKE '%tzv%' 
AND (
    `gender` = 'M' 
    OR `emp_no` BETWEEN 50000 AND 60000
    );
```
 
23. Sélectionner les employés dont le prénom termine par « CAL»
```sql
SELECT * 
FROM `employees` 
WHERE `first_name` LIKE '%cal';
```
 
24. Sélectionner les employés dont le prénom termine par « CAL» de genre masculin et dont le numéro d’employé est compris entre 50000 et 60000 
```sql
SELECT * 
FROM `employees` 
WHERE `first_name` LIKE '%cal' 
AND `gender` = 'M' 
AND `emp_no` BETWEEN 50000 AND 60000 ;
```
 
25. Sélectionner les employés dont le prénom est « danai » ou « leen » et le nom se termine par « TH» ou dont le numéro d’employé est compris entre 50000 et 100000
```sql
SELECT * 
FROM `employees` 
WHERE `first_name` IN ('danai', 'leen') 
AND (
    `last_name` LIKE '%th' 
    OR `emp_no` BETWEEN 50000 AND 100000
    );
```
 
26. Sélectionner les employés dont la date de naissance est null
```sql
SELECT * 
FROM `employees` 
WHERE `birth_date` IS NULL;
```