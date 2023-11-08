## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

1. Sélectionner le nombre de villes par État :
```sql
SELECT state_id, COUNT(*) as city_count FROM cities GROUP BY state_id;
```

2. Sélectionner le nombre de villes par code d'État :
```sql
SELECT state_code, COUNT(*) as city_count FROM cities GROUP BY state_code;
```

3. Sélectionner le nombre de villes par pays :
```sql
SELECT country_id, COUNT(*) as city_count FROM cities GROUP BY country_id;
```

4. Sélectionner le nombre de villes par code de pays :
```sql
SELECT country_code, COUNT(*) as city_count FROM cities GROUP BY country_code;
```

5. Sélectionner le nombre de villes par drapeau (flag) :
```sql
SELECT flag, COUNT(*) as city_count FROM cities GROUP BY flag;
```

6. Calculer la somme des latitudes par État avec un total général :
```sql
SELECT state_id, SUM(latitude) as total_latitude FROM cities GROUP BY state_id WITH ROLLUP;
```

7. Calculer la somme des longitudes par État avec un total général :
```sql
SELECT state_id, SUM(longitude) as total_longitude FROM cities GROUP BY state_id WITH ROLLUP;
```

8. Calculer la somme des latitudes par pays avec un total général :
```sql
SELECT country_id, SUM(latitude) as total_latitude FROM cities GROUP BY country_id WITH ROLLUP;
```

9. Calculer la somme des longitudes par pays avec un total général :
```sql
SELECT country_id, SUM(longitude) as total_longitude FROM cities GROUP BY country_id WITH ROLLUP; 
```

10. Calculer la somme des latitudes et longitudes avec un total général :
```sql
SELECT 'Total' as summary, SUM(latitude) as total_latitude, SUM(longitude) as total_longitude FROM cities;
```

11. Calculer la moyenne de la latitude par État ayant une moyenne supérieure à 40 :
```sql
SELECT state_id, AVG(latitude) as avg_latitude FROM cities GROUP BY state_id HAVING AVG(latitude) > 40;
```

12. Calculer la moyenne de la longitude par État ayant une moyenne supérieure à -100 :
```sql
SELECT state_id, AVG(longitude) as avg_longitude FROM cities GROUP BY state_id HAVING AVG(longitude) > -100;
```

13. Calculer la moyenne de la latitude par pays ayant une moyenne supérieure à 35
```sql
SELECT country_id, AVG(latitude) as avg_latitude FROM cities GROUP BY country_id HAVING AVG(latitude) > 35;
```

14. Calculer la moyenne de la longitude par pays ayant une moyenne supérieure à -90
```sql
SELECT country_id, AVG(longitude) as avg_longitude FROM cities GROUP BY country_id HAVING AVG(longitude) > -90;
```

15. Calculer la moyenne de la latitude et longitude avec une moyenne supérieure à 0 :
```sql
SELECT 'Total' as summary, AVG(latitude) as avg_latitude, AVG(longitude) as avg_longitude FROM cities HAVING AVG(latitude) > 0;
```

16. Sélectionner les noms des produits et leurs prix unitaires, triés par prix décroissant :
```sql
SELECT product_name, unit_price FROM products ORDER BY unit_price DESC;
```

17. Sélectionner les noms des produits et leurs prix unitaires, triés par prix décroissant, puis par nom de produit :
```sql
SELECT product_name, unit_price FROM products ORDER BY unit_price DESC, product_name;
```

18. Sélectionner les noms des produits et leurs prix unitaires, triés par prix décroissant, puis par catégorie de produit :
```sql
SELECT product_name, unit_price, category FROM products ORDER BY unit_price DESC, category;
```

19. Sélectionner les noms des produits et leurs prix unitaires, triés par prix décroissant, puis par date d'ajout au catalogue :
```sql
SELECT product_name, unit_price, added_date FROM products ORDER BY unit_price DESC, added_date;
```

20. Sélectionner les noms des produits et leurs prix unitaires, triés par prix décroissant, puis par quantité en stock :
```sql
SELECT product_name, unit_price, stock_quantity FROM products ORDER BY unit_price DESC, stock_quantity;
```

21. Sélectionner les noms des États et des codes d'État en renommant les colonnes "nom_de_l_etat" et "code_de_l_etat" :
```sql
SELECT state_id AS nom_de_l_etat, state_code AS code_de_l_etat FROM cities;
```

22. Sélectionner les noms des pays et des codes de pays en renommant les colonnes "nom_du_pays" et "code_du_pays" :
```sql
SELECT country_id AS nom_du_pays, country_code AS code_du_pays FROM cities;
```

23. Sélectionner les latitudes et longitudes des villes en renommant les colonnes "latitude_de_la_ville" et "longitude_de_la_ville" :
```sql
SELECT latitude AS latitude_de_la_ville, longitude AS longitude_de_la_ville FROM cities;
```

24. Sélectionner les dates de création et de mise à jour des enregistrements en renommant les colonnes "date_de_creation" et "date_de_mise_a_jour" :
```sql
SELECT created_at AS date_de_creation, updated_at AS date_de_mise_a_jour FROM cities;
```

25. Sélectionner les indicateurs de drapeau et les identifiants WikiData en renommant les colonnes "indicateur_de_drapeau" et "identifiant_WikiData" :
```sql
SELECT flag AS indicateur_de_drapeau, wikiDataId AS identifiant_WikiData FROM cities;
```

26. Sélectionner les 10 premières lignes de la table des villes :
```sql
SELECT * FROM cities LIMIT 10;
```

27. Sélectionner les 10 villes avec les latitudes les plus élevées :
```sql
SELECT * FROM cities ORDER BY latitude DESC LIMIT 10;
```

28. Sélectionner les 10 villes avec les longitudes les plus basses :
```sql
SELECT * FROM cities ORDER BY longitude ASC LIMIT 10;
```

29. Sélectionner les 10 villes dans l'état ayant l'id 123 :
```sql
SELECT * FROM cities WHERE state_id = 123 LIMIT 10;
```

30. Sélectionner les 10 villes dans le pays ayant l'id 456 :
```sql
SELECT * FROM cities WHERE country_id = 456 LIMIT 10;
```

31. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" :
```sql
SELECT city_name, 
CASE 
    WHEN latitude > 50 THEN 'Élevée'
    WHEN latitude > 40 THEN 'Modérée'
END AS latitude_category
FROM cities;
```

32. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" :
```sql
SELECT city_name, 
CASE 
    WHEN latitude > 60 THEN 'Très élevée'
    WHEN latitude > 50 THEN 'Élevée'
    WHEN latitude > 40 THEN 'Modérée'
END AS latitude_category
FROM cities;
```

33. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" :
```sql
SELECT city_name, 
CASE 
    WHEN latitude > 45 THEN 'Élevée'
    WHEN latitude > 35 THEN 'Modérée'
END AS latitude_category
FROM cities;
```

34. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" :
```sql
SELECT city_name, 
CASE 
    WHEN latitude > 47 THEN 'Très élevée'
    WHEN latitude > 42 THEN 'Élevée'
    WHEN latitude > 37 THEN 'Modérée'
END AS latitude_category
FROM cities;
```

35. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" :
```sql
SELECT city_name, 
CASE 
    WHEN latitude > 55 THEN 'Très élevée'
    WHEN latitude > 50 THEN 'Élevée'
    WHEN latitude > 45 THEN 'Modérée'
END AS latitude_category
FROM cities;
```
