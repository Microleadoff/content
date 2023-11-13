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

6. Calculer la somme des latitudes et des longitudes par region_id ainsi que la somme de chaque :
```sql
SELECT SUM(latitude), SUM(longitude), region_id
FROM countries
GROUP BY region_id WITH ROLLUP;
```

7. Calculer la moyenne des latitudes et des longitudes par country_id ainsi que la moyenne en tout :
```sql
SELECT AVG(latitude), AVG(longitude), country_id
from cities
GROUP BY country_id WITH ROLLUP;
```

8. Calculer les latitudes et longitudes minimales de chaque ville ainsi que la valeur minimale globale :
```sql
SELECT state_id, MIN(latitude), MIN(longitude)
FROM cities
GROUP BY state_id WITH ROLLUP;
```

9. Calculer la moyenne des "fips_code" par pays et renvoyer également le total des moyennes :
```sql
SELECT country_id, AVG(fips_code)
FROM states
GROUP BY country_id WITH ROLLUP;
```

10. Calculer la somme des valeurs des sous-régions par région et renvoyer également le total des valeurs :
```sql
SELECT region_id, SUM(subregion_id)
FROM countries
GROUP BY region_id WITH ROLLUP
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

16. Sélectionner les noms des continents dans l'ordre décroissant :
```sql
SELECT name, id
FROM regions
ORDER BY name DESC;
```

17. Sélectionner tous les pays qui ont une latitude supérieure à 20 dans l'ordre croissant :
```sql
SELECT name, latitude, longitude
FROM countries
WHERE latitude > 20
ORDER BY name ASC;
```

18. Sélectionner les Etats dans lequel le mot "Region" apparait par ordre croissant :
```sql
SELECT name 
FROM states
WHERE name LIKE "%Region%"
ORDER BY name ASC;
```

19. Sélectionner tous les pays qui ont un état avec un id compris entre 480 et 500 par ordre décroissant :
```sql
SELECT name, state_id, latitude, longitude
FROM cities
WHERE state_id > 480 AND state_id < 500
ORDER BY name DESC;
```

20. Sélectionner toutes les sous-régions qui appartiennent à la région possédant l'id 2 par ordre décroissant :
```sql
SELECT *
FROM subregions
WHERE region_id = 2
ORDER BY name DESC;
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

30. Sélectionner les 10 villes dans le pays ayant un id inférieur à 456 :
```sql
SELECT * FROM cities WHERE country_id < 456 LIMIT 10;
```

31. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" (si la latitude est supérieure à 50, alors vous devrez retourner "Élevée", si elle est supérieure à 40 retournez "Modérée") :
```sql
SELECT name, 
CASE 
    WHEN latitude > 50 THEN 'Élevée'
    WHEN latitude > 40 THEN 'Modérée'
END AS latitude_category
FROM cities;
```

32. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" (si la latitude est supérieure à 60, retournez "Très élevée", si elle est supérieure à 50, alors vous devrez retourner "Élevée", si elle est supérieure à 40 retournez "Modérée") :
```sql
SELECT name, 
CASE 
    WHEN latitude > 60 THEN 'Très élevée'
    WHEN latitude > 50 THEN 'Élevée'
    WHEN latitude > 40 THEN 'Modérée'
END AS latitude_category
FROM cities;
```

33. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" (si la latitude est supérieure à 45, alors vous devrez retourner "Élevée", si elle est supérieure à 35 retournez "Modérée") :
```sql
SELECT name, 
CASE 
    WHEN latitude > 45 THEN 'Élevée'
    WHEN latitude > 35 THEN 'Modérée'
END AS latitude_category
FROM cities;
```

34. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" (si la latitude est supérieure à 47, retournez "Très élevée", si elle est supérieure à 42, alors vous devrez retourner "Élevée", si elle est supérieure à 37 retournez "Modérée") :
```sql
SELECT name, 
CASE 
    WHEN latitude > 47 THEN 'Très élevée'
    WHEN latitude > 42 THEN 'Élevée'
    WHEN latitude > 37 THEN 'Modérée'
END AS latitude_category
FROM cities;
```

35. Sélectionner les noms des villes et les catégories de latitude en utilisant "CASE" et "WHEN" (si la latitude est supérieure à 55, retournez "Très élevée", si elle est supérieure à 50, alors vous devrez retourner "Élevée", si elle est supérieure à 45 retournez "Modérée") :
```sql
SELECT name, 
CASE 
    WHEN latitude > 55 THEN 'Très élevée'
    WHEN latitude > 50 THEN 'Élevée'
    WHEN latitude > 45 THEN 'Modérée'
END AS latitude_category
FROM cities;
```
