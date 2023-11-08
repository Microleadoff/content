## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

1. Sélectionner les prénoms des employés qui ont effectué des ventes (commandes) :
```sql
SELECT first_name
FROM employees AS e
WHERE EXISTS (SELECT 1 FROM orders AS o WHERE o.employee_id = e.emp_no);
```

2. Sélectionner les noms de famille des employés qui ont des ventes confirmées :
```sql
SELECT last_name
FROM employees AS e
WHERE EXISTS (SELECT 1 FROM orders AS o WHERE o.employee_id = e.emp_no AND o.status = 'Confirmé');
```

3. Sélectionner les prénoms des employés masculins ayant effectué des ventes :
```sql
SELECT first_name
FROM employees AS e
WHERE EXISTS (SELECT 1 FROM orders AS o WHERE o.employee_id = e.emp_no)
AND gender = 'M';
```

4. Sélectionner les noms de famille des employés féminins ayant effectué des ventes confirmées :
```sql
SELECT last_name
FROM employees AS e
WHERE EXISTS (SELECT 1 FROM orders AS o WHERE o.employee_id = e.emp_no AND o.status = 'Confirmé')
AND gender = 'F';
```

5. Sélectionner les prénoms des employés qui ont été embauchés en 2022 et ont effectué des ventes :
```sql
SELECT first_name
FROM employees AS e
WHERE EXISTS (SELECT 1 FROM orders AS o WHERE o.employee_id = e.emp_no)
AND hire_date >= '2022-01-01' AND hire_date < '2023-01-01';
```

6. Sélectionner les noms des employés dont le salaire est supérieur ou égal au salaire de tous les employés du département 'Sales' :
```sql
SELECT employee_name
FROM employees AS e
WHERE salary >= ALL (SELECT salary FROM employees WHERE department = 'Sales');
```

7. Sélectionner les prénoms des employés masculins dont le salaire est supérieur ou égal au salaire de tous les employés masculins du département 'Marketing' :
```sql
SELECT first_name
FROM employees AS e
WHERE gender = 'M' AND salary >= ALL (SELECT salary FROM employees WHERE department = 'Marketing' AND gender = 'M');
```

8. Sélectionner les noms de famille des employés dont le salaire est supérieur ou égal au salaire de tous les employés du département 'Ressources humaines' :
```sql
SELECT last_name
FROM employees AS e
WHERE salary >= ALL (SELECT salary FROM employees WHERE department = 'Ressources humaines');
```

9. Sélectionner les prénoms des employés féminins dont le salaire est supérieur ou égal au salaire de toutes les employées féminines du département 'Finance' :
```sql
SELECT first_name
FROM employees AS e
WHERE gender = 'F' AND salary >= ALL (SELECT salary FROM employees WHERE department = 'Finance' AND gender = 'F');
```

10. Sélectionner les noms de famille des employés dont le salaire est supérieur ou égal au salaire de tous les employés du département 'Développement' :
```sql
SELECT last_name
FROM employees AS e
WHERE salary >= ALL (SELECT salary FROM employees WHERE department = 'Développement');
```

11. Sélectionner les prénoms des employés dont au moins un enregistrement a un salaire supérieur à 50000 :
```sql
SELECT first_name
FROM employees AS e
WHERE emp_no = ANY (SELECT emp_no FROM salaries WHERE salary > 50000);
```

12. Sélectionner les noms de famille des employés dont au moins un enregistrement a un salaire égal à 60000 :
```sql
SELECT last_name
FROM employees AS e
WHERE emp_no = ANY (SELECT emp_no FROM salaries WHERE salary = 60000);
```

13. Sélectionner les prénoms des employés masculins dont au moins un enregistrement a un salaire supérieur à 55000 :
```sql
SELECT first_name
FROM employees AS e
WHERE gender = 'M' AND emp_no = ANY (SELECT emp_no FROM salaries WHERE salary > 55000);
```

14. Sélectionner les noms de famille des employés dont au moins un enregistrement a un salaire égal à 58000 :
```sql
SELECT last_name
FROM employees AS e
WHERE emp_no = ANY (SELECT emp_no FROM salaries WHERE salary = 58000);
```

15. Sélectionner les prénoms des employés féminins dont au moins un enregistrement a un salaire supérieur à 53000 :
```sql
SELECT first_name
FROM employees AS e
WHERE gender = 'F' AND emp_no = ANY (SELECT emp_no FROM salaries WHERE salary > 53000);
```
