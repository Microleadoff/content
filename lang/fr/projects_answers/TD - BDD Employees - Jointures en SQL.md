## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

1. Sélectionner les prénoms et les noms des départements auxquels les employés sont affectés :
```sql
SELECT e.first_name, d.dept_name
FROM employees AS e
INNER JOIN departments AS d ON e.department_id = d.dept_no;
```

2. Sélectionner les noms de famille et les noms des départements auxquels les employés sont affectés :
```sql
SELECT e.last_name, d.dept_name
FROM employees AS e
INNER JOIN departments AS d ON e.department_id = d.dept_no;
```

3. Sélectionner les prénoms et les noms de départements pour les employés masculins :
```sql
SELECT e.first_name, d.dept_name
FROM employees AS e
INNER JOIN departments AS d ON e.department_id = d.dept_no
WHERE e.gender = 'M';
```

4. Sélectionner les noms de famille et les noms de départements pour les employés féminins :
```sql
SELECT e.last_name, d.dept_name
FROM employees AS e
INNER JOIN departments AS d ON e.department_id = d.dept_no
WHERE e.gender = 'F';
```

5. Sélectionner les prénoms et les noms de départements pour les employés embauchés en 2022
```sql
SELECT e.first_name, d.dept_name
FROM employees AS e
INNER JOIN departments AS d ON e.department_id = d.dept_no
WHERE e.hire_date >= '2022-01-01' AND e.hire_date < '2023-01-01';
```

6. Sélectionner les prénoms et les noms des départements auxquels les employés sont affectés (avec éventuelles affectations manquantes) :
```sql
SELECT e.first_name, d.dept_name
FROM employees AS e
LEFT JOIN departments AS d ON e.department_id = d.dept_no;
```

7. Sélectionner les noms de famille et les noms des départements auxquels les employés sont affectés (avec éventuelles affectations manquantes) :
```sql
SELECT e.last_name, d.dept_name
FROM employees AS e
LEFT JOIN departments AS d ON e.department_id = d.dept_no;
```

8. Sélectionner les prénoms et les noms de départements pour les employés masculins (avec éventuelles affectations manquantes) :
```sql
SELECT e.first_name, d.dept_name
FROM employees AS e
LEFT JOIN departments AS d ON e.department_id = d.dept_no
WHERE e.gender = 'M';
```

9. Sélectionner les noms de famille et les noms de départements pour les employés féminins (avec éventuelles affectations manquantes) :
```sql
SELECT e.last_name, d.dept_name
FROM employees AS e
LEFT JOIN departments AS d ON e.department_id = d.dept_no
WHERE e.gender = 'F';
```

10. Sélectionner les prénoms et les noms de départements pour les employés embauchés en 2022 (avec éventuelles affectations manquantes) :
```sql
SELECT e.first_name, d.dept_name
FROM employees AS e
LEFT JOIN departments AS d ON e.department_id = d.dept_no
WHERE e.hire_date >= '2022-01-01' AND e.hire_date < '2023-01-01';
```

11. Sélectionner les prénoms et les noms des départements auxquels les employés sont affectés (avec éventuelles affectations manquantes) :
```sql
SELECT e.first_name, d.dept_name
FROM employees AS e
FULL JOIN departments AS d ON e.department_id = d.dept_no;
```

12. Sélectionner les noms de famille et les noms des départements auxquels les employés sont affectés (avec éventuelles affectations manquantes) :
```sql
SELECT e.last_name, d.dept_name
FROM employees AS e
FULL JOIN departments AS d ON e.department_id = d.dept_no;
```

13. Sélectionner les prénoms et les noms de départements pour les employés masculins (avec éventuelles affectations manquantes) :
```sql
SELECT e.first_name, d.dept_name
FROM employees AS e
FULL JOIN departments AS d ON e.department_id = d.dept_no
WHERE e.gender = 'M';
```

14. Sélectionner les noms de famille et les noms de départements pour les employés féminins (avec éventuelles affectations manquantes) :
```sql
SELECT e.last_name, d.dept_name
FROM employees AS e
FULL JOIN departments AS d ON e.department_id = d.dept_no
WHERE e.gender = 'F';
```

15. Sélectionner les prénoms et les noms de départements pour les employés embauchés en 2022 (avec éventuelles affectations manquantes) :
```sql
SELECT e.first_name, d.dept_name
FROM employees AS e
FULL JOIN departments AS d ON e.department_id = d.dept_no
WHERE e.hire_date >= '2022-01-01' AND e.hire_date < '2023-01-01';
```

16. Sélectionner les prénoms et les noms de départements pour chaque combinaison employé-département
```sql
SELECT e.first_name, d.dept_name
FROM employees AS e
CROSS JOIN departments AS d;
```

17. Sélectionner les noms de famille et les noms de départements pour chaque combinaison employé-département :
```sql
SELECT e.last_name, d.dept_name
FROM employees AS e
CROSS JOIN departments AS d;
```

18. Sélectionner les prénoms et les noms de départements pour chaque combinaison employé-département, pour les employés masculins :
```sql
SELECT e.first_name, d.dept_name
FROM employees AS e
CROSS JOIN departments AS d
WHERE e.gender = 'M';
```

19. Sélectionner les noms de famille et les noms de départements pour chaque combinaison employé-département, pour les employés féminins :
```sql
SELECT e.last_name, d.dept_name
FROM employees AS e
CROSS JOIN departments AS d
WHERE e.gender = 'F';
```

20. Sélectionner les prénoms et les noms de départements pour chaque combinaison employé-département, pour les employés embauchés en 2022 :
```sql
SELECT e.first_name, d.dept_name
FROM employees AS e
CROSS JOIN departments AS d
WHERE e.hire_date >= '2022-01-01' AND e.hire_date < '2023-01-01';
```

21. Sélectionner les prénoms des employés et les prénoms de leurs gestionnaires (avec gestionnaires optionnels) :
```sql
SELECT e1.first_name, e2.first_name AS manager_name
FROM employees AS e1
LEFT JOIN employees AS e2 ON e1.manager_id = e2.emp_no;
```

22. Sélectionner les noms de famille des employés et les noms de famille de leurs gestionnaires (avec gestionnaires optionnels) :
```sql
SELECT e1.last_name, e2.last_name AS manager_name
FROM employees AS e1
LEFT JOIN employees AS e2 ON e1.manager_id = e2.emp_no;
```

23. Sélectionner les prénoms des employés masculins et les prénoms de leurs gestionnaires masculins (avec gestionnaires optionnels) :
```sql
SELECT e1.first_name, e2.first_name AS manager_name
FROM employees AS e1
LEFT JOIN employees AS e2 ON e1.manager_id = e2.emp_no
WHERE e1.gender = 'M' AND e2.gender = 'M';
```

24. Sélectionner les noms de famille des employés féminins et les noms de famille de leurs gestionnaires féminins (avec gestionnaires optionnels) :
```sql
SELECT e1.last_name, e2.last_name AS manager_name
FROM employees AS e1
LEFT JOIN employees AS e2 ON e1.manager_id = e2.emp_no
WHERE e1.gender = 'F' AND e2.gender = 'F';
```

25. Sélectionner les prénoms des employés embauchés en 2022 et les prénoms de leurs gestionnaires (avec gestionnaires optionnels) :
```sql
SELECT e1.first_name, e2.first_name AS manager_name
FROM employees AS e1
LEFT JOIN employees AS e2 ON e1.manager_id = e2.emp_no
WHERE e1.hire_date >= '2022-01-01' AND e1.hire_date < '2023-01-01';
```
