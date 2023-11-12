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

8. Sélectionner toutes les villes dont le pays à l'id numéro 6 ou 231 en utilisant "WHERE" et "OR" :
```sql
SELECT * FROM cities WHERE country_id = 6 OR country_id = 231;
```

9. Sélectionner toutes les villes dont le code de pays est "US" ou "CA" en utilisant "WHERE" et "OR" :
```sql
SELECT * FROM cities WHERE country_code = 'US' OR country_code = 'CA';
```

10. Sélectionner toutes les villes dont la latitude est supérieure à 40 ou la longitude est inférieure à -100 en utilisant "WHERE" et "OR" :
```sql
SELECT * FROM cities WHERE latitude > 40 OR longitude < -100;
```

11. Sélectionner toutes les villes dont l'id de l'état est 3395 ou 3396 en utilisant "IN" :
```sql
SELECT * FROM cities WHERE state_id IN (3395, 3396);
```

12. Sélectionner toutes les villes dont le code d'État est "CA" ou "TX" en utilisant "IN" :
```sql
SELECT * FROM cities WHERE state_code IN ('CA', 'TX');
```

13. Sélectionner toutes les villes dont l'id du pays est 3 ou 12 en utilisant "IN" :
```sql
SELECT * FROM cities WHERE country_id IN (3, 12);
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

20. Sélectionner toutes les villes dont la latitude est entre 25 et 26 en utilisant "WHERE" et "BETWEEN" :
```sql
SELECT * FROM cities WHERE latitude BETWEEN 25 AND 26;
```

21. Sélectionner toutes les villes dont le nom commence par 'Los' en utilisant "LIKE" :
```sql
SELECT * FROM cities WHERE name LIKE 'Los%';
```

22. Sélectionner toutes les villes dont le nom se termine par 'ville' en utilisant "LIKE" :
```sql
SELECT * FROM cities WHERE name LIKE '%ville';
```

23. Sélectionner toutes les villes dont le nom contient 'New' en utilisant "LIKE" :
```sql
SELECT * FROM cities WHERE name LIKE '%New%';
```

24. Sélectionner toutes les villes dont le code d'état commence par 'T' en utilisant "LIKE" :
```sql
SELECT * FROM cities WHERE state_code LIKE 'T%';
```

25. Sélectionner toutes les villes dont l'id du pays se termine par 9 en utilisant "LIKE" :
```sql
SELECT * FROM cities WHERE state_id LIKE '%9';
```
