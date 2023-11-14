## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

1. Sélectionner toutes les villes qui ont dans leurs country id des noms de pays qui commence par la lettre A :
```sql
SELECT name
FROM cities
WHERE country_id IN(
	SELECT id
	FROM countries
	WHERE name LIKE "A%");
```

2. Sélectionner la capitale de chaque pays dont l'id de région est un chiffre pair :
```sql
SELECT capital
FROM countries
WHERE region_id IN(
	SELECT id
	FROM regions
	WHERE id%2 = 0);
```

3. Sélectionner tous les pays qui sont dans la région qui contient la sous-région d'id 1 :
```sql
SELECT name
FROM countries
WHERE region_id IN (
    SELECT region_id
    FROM subregions
    WHERE id =1
)
```

4. Sélectionner les noms de touutes les villes dont le nom de leur pays est "Algeria" ou "Angola" :
```sql
SELECT name
FROM cities
WHERE `country_id` IN (
 	SELECT id
    FROM countries
    WHERE name = "Algeria"
    OR name = "Angola"
)
```

5. Sélectionner le nom des états de chaque pays situé dans la région dont le nom est "Europe" :
```sql
SELECT name
FROM states
WHERE country_id IN(
	SELECT id
	FROM countries
	WHERE region_id =(
		SELECT id
    	FROM regions
    	WHERE name = "Europe"));
```

6. Sélectionner tous les noms de ville du pays dont le nom est France si celui-ci existe :
```sql
SELECT name
FROM cities
WHERE EXISTS (
    SELECT id
    FROM countries
    WHERE name = "France"
);
```

7. Sélectionner toutes les régions qui contiennent un pays avec une latitude supérieure à 60 s'il en existe :
```sql
SELECT name
FROM regions
WHERE EXISTS (
    SELECT latitude
    FROM countries
    WHERE latitude > 60
);
```

8. Sélectionner le nom de toutes les sous-régions qui contiennent un pays dont le nom est "Région" :
```sql
SELECT name
FROM subregions
WHERE EXISTS (
    SELECT id
    FROM states
    WHERE name = "Region"
);
```
**Note** : Cette requête renvoie un résultat vide car aucun pays ne s'appelle "Region" !

9. Sélectionner toutes les villes dont l'id est plus grand que le nombre de pays qui ont pour devise l'euro :
```sql
SELECT *
FROM cities
WHERE state_id > all (
	SELECT id
    FROM countries
    WHERE currency_name = "Euro"
);
```

10. Sélectionner tous les pays, le symbole de leur devise et le nom de leur devise si leurs id est inférieur ou égale à l'id le plus grand parmis la table régions :
```sql
SELECT name, currency_symbol, currency_name
FROM countries
WHERE id <= all (
	SELECT MAX(id)
	FROM regions
);
```

11. Sélectionner les noms et les id des sous régions dont l'id de la région parent est égal à tous les id des régions qui ont pour nom "Americas" :
```sql
SELECT name, id
FROM subregions
WHERE region_id = all (
	SELECT id
	FROM regions
    WHERE name = "Americas"
);
```

12. Sélectionner les villes si il y a au moins un id plus grand que le nombre de pays qui ont pour devise l'euro :
```sql
SELECT *
FROM cities
WHERE state_id > any (
	SELECT id
    FROM countries
    WHERE currency_name = "Euro"
);
```

13. Sélectionner les nom, le symbole et le nom des monnaies des pays dont l'id est égal au plus grand id des régions :
```sql
SELECT name, currency_symbol, currency_name
FROM countries
WHERE id = ANY (
	SELECT MAX(id)
	FROM regions
);
```

14. Sélectionner le nom, le fips_code, la latitude et la longitude des états dont le fips_code est égal à l'id de la ville qui s'appelle "Paris" :
```sql
SELECT name, fips_code, latitude, longitude
FROM states
WHERE fips_code = ANY (
	SELECT id
	FROM cities
    WHERE name = "Paris"
);
```
**Note** : Ne renvoie rien car aucun flips_code ne partage la même valeur que l'id de la ville de Paris


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```


```sql

```
