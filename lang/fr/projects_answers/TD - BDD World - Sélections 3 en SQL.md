## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

1. Sélectionner toutes les sous-région appartenant aux régions id 1 à 3, ainsi que celles appartenant à la région id 5 en utilisant UNION :
```sql
SELECT *
FROM subregions
WHERE region_id < 4
UNION
SELECT *
FROM subregions
WHERE region_id = 5
```

2. Sélectionner tous les états avec une latitude comprise entre 20 et 40, ainsi que tous les états avec une longitude comprise entre 20 et 40 en utilisant UNION :
```sql
SELECT *
FROM states
WHERE latitude BETWEEN 20 AND 40
UNION
SELECT *
FROM states
WHERE longitude BETWEEN 20 AND 40
```

3. Sélectionner tous les pays dont le symbole de la monnaie est "€", ainsi que tous les pays dont le symbole de la monnaie est "$" en utilisant UNION
```sql
SELECT *
FROM countries
WHERE currency_symbol = '€'
UNION
SELECT *
FROM countries
WHERE currency_symbol = '$'
```

4. Sélectionner toutes les villes dont le code de l'état est "AZ", ainsi que toutes les villes dont le code du pays est "AD" en utilisant UNION :
```sql
SELECT *
FROM cities
WHERE state_code = 'AZ'
UNION
SELECT *
FROM cities
WHERE country_code = 'AD'
```

5. Sélectionner tous les pays dont le symbole de la monnaie est "$", ainsi que tous les pays dont le code iso3 contient la lettre "A" en utilisant UNION :
```sql
SELECT *
FROM countries
WHERE currency_symbol = '$'
UNION
SELECT *
FROM countries
WHERE iso3 LIKE "%A%"
```

6. Sélectionner tous les id des régions, ainsi que tous les champs "region_id" des pays en utilisant UNION ALL :
```sql
SELECT id FROM regions
UNION ALL
SELECT region_id FROM countries
```

7. Sélectionner tous les noms des sous-régions, ainsi que toutes les sous-régions des pays en utilisant UNION ALL :
```sql
SELECT name FROM subregions
UNION ALL
SELECT subregion FROM countries
```

8. Sélectionner tous les codes iso2 des pays, ainsi que tous les codes des pays depuis la table des états en utilisant UNION ALL
```sql
SELECT iso2 FROM countries
UNION ALL
SELECT country_code FROM states
```

9. Sélectionner toutes les dates de création des pays, ainsi que toutes les dates de création des états en utilisant UNION ALL
```sql
SELECT created_at FROM countries
UNION ALL
SELECT created_at FROM states
```

10. Sélectionner tous les id des sous-régions, ainsi que tous id des régions en utilisant UNION ALL
```sql
SELECT id FROM subregions
UNION ALL
SELECT id FROM regions
```


```sql
XXX
```


```sql
XXX
```


```sql
XXX
```


```sql
XXX
```


```sql
XXX
```


```sql
XXX
```


```sql
XXX
```


```sql
XXX
```


```sql
XXX
```


```sql
XXX
```


```sql
XXX
```


```sql
XXX
```
