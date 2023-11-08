## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

1. Sélectionner tous les États distincts :
```sql
SELECT DISTINCT state_id FROM cities;
```

2. Sélectionner tous les codes d'État distincts :
```sql
SELECT DISTINCT state_code FROM cities;
```

3. Sélectionner tous les pays distincts :
```sql
SELECT DISTINCT country_id FROM cities;
```

4. Sélectionner tous les codes de pays distincts :
```sql
SELECT DISTINCT country_code FROM cities;
```

5. Sélectionner toutes les valeurs distinctes de latitude et longitude :
```sql
SELECT DISTINCT latitude, longitude FROM cities;
```

6. Sélectionner toutes les villes dont l'État est "California" ou "Texas" en utilisant "WHERE" et "OR" :
```sql
SELECT * FROM cities WHERE state_id = 'California' OR state_id = 'Texas';
```

7. Sélectionner toutes les villes dont le code d'État est "CA" ou "TX" en utilisant "WHERE" et "OR" :
```sql
SELECT * FROM cities WHERE state_code = 'CA' OR state_code = 'TX';
```

8. Sélectionner toutes les villes dont le pays est "USA" ou "Canada" en utilisant "WHERE" et "OR" :
```sql
SELECT * FROM cities WHERE country_id = 'USA' OR country_id = 'Canada';
```

9. Sélectionner toutes les villes dont le code de pays est "US" ou "CA" en utilisant "WHERE" et "OR" :
```sql
SELECT * FROM cities WHERE country_code = 'US' OR country_code = 'CA';
```

10. Sélectionner toutes les villes dont la latitude est supérieure à 40 ou la longitude est inférieure à -100 en utilisant "WHERE" et "OR" :
```sql
SELECT * FROM cities WHERE latitude > 40 OR longitude < -100;
```

11. Sélectionner toutes les villes dont l'État est "California" ou "Texas" en utilisant "IN" :
```sql
SELECT * FROM cities WHERE state_id IN ('California', 'Texas');
```

12. Sélectionner toutes les villes dont le code d'État est "CA" ou "TX" en utilisant "IN" :
```sql
SELECT * FROM cities WHERE state_code IN ('CA', 'TX');
```

13. Sélectionner toutes les villes dont le pays est "USA" ou "Canada" en utilisant "IN" :
```sql
SELECT * FROM cities WHERE country_id IN ('USA', 'Canada');
```

14. Sélectionner toutes les villes dont le code de pays est "US" ou "CA" en utilisant "IN" :
```sql
SELECT * FROM cities WHERE country_code IN ('US', 'CA');
```

15. Sélectionner toutes les villes dont la latitude est supérieure à 40 ou la longitude est inférieure à -100 en utilisant "IN" :
```sql
SELECT * FROM cities WHERE latitude > 40 OR longitude < -100;
```

16. Sélectionner toutes les villes dont la latitude est entre 40 et 45 en utilisant "WHERE" et "BETWEEN" :
```sql
SELECT * FROM cities WHERE latitude BETWEEN 40 AND 45;
```

17. Sélectionner toutes les villes dont la longitude est entre -100 et -90 en utilisant "WHERE" et "BETWEEN" :
```sql
SELECT * FROM cities WHERE longitude BETWEEN -100 AND -90;
```

18. Sélectionner toutes les villes dont l'ID est entre 100 et 200 en utilisant "WHERE" et "BETWEEN" :
```sql
SELECT * FROM cities WHERE id BETWEEN 100 AND 200;
```

19. Sélectionner toutes les villes dont la création a eu lieu entre deux dates en utilisant "WHERE" et "BETWEEN" :
```sql
SELECT * FROM cities WHERE created_at BETWEEN '2023-01-01' AND '2023-12-31';
```

20. Sélectionner toutes les villes dont le code postal est entre 90000 et 90999 en utilisant "WHERE" et "BETWEEN" :
```sql
SELECT * FROM cities WHERE postal_code BETWEEN 90000 AND 90999;
```

21. Sélectionner toutes les villes dont le nom commence par 'Los' en utilisant "LIKE" :
```sql
SELECT * FROM cities WHERE city_name LIKE 'Los%';
```

22. Sélectionner toutes les villes dont le nom se termine par 'ville' en utilisant "LIKE" :
```sql
SELECT * FROM cities WHERE city_name LIKE '%ville';
```

23. Sélectionner toutes les villes dont le nom contient 'New' en utilisant "LIKE" :
```sql
SELECT * FROM cities WHERE city_name LIKE '%New%';
```

24. Sélectionner toutes les villes dont le code postal commence par '90' en utilisant "LIKE" :
```sql
SELECT * FROM cities WHERE postal_code LIKE '90%';
```

25. Sélectionner toutes les villes dont le pays se termine par 'land' en utilisant "LIKE" :
```sql
SELECT * FROM cities WHERE country_id LIKE '%land';
```
