## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

1. Créer une base de données nommée « golf » :
```sql
CREATE DATABASE golf;
```

2. Créez une table nommée « utilisateurs » qui respectera les colonnes suivantes : 
    - Id, pk, auto_increment
    - Firstname, varchar
    - Lastname, varchar
    - Email, longtext
```sql
CREATE TABLE utilisateurs (Id INT PRIMARY KEY AUTO_INCREMENT,Firstname VARCHAR(255),Lastname VARCHAR(255),Email LONGTEXT);
```

3. Créez une table nommée « golfeurs » qui respectera les colonnes suivantes : 
    - Id, pk, auto_increment
    - Firstname, varchar
    - Lastname, varchar
    - Email, longtext
```sql
CREATE TABLE golfeurs (Id INT PRIMARY KEY AUTO_INCREMENT,Firstname VARCHAR(255),Lastname VARCHAR(255),Email LONGTEXT);
```

4. Créez un nouveau golfeur : John LEGEND, j.legend@gmail.com
```sql
INSERT INTO golfeurs (Firstname, Lastname, Email) VALUES ('John', 'LEGEND', 'j.legend@gmail.com');
```

5. Créez un nouvel utilisateur : Jack SPARROW, jack_sparrow@yahoo.fr
```sql
INSERT INTO utilisateurs (Firstname, Lastname, Email) VALUES ('Jack', 'SPARROW', 'jack_sparrow@yahoo.fr');
```

6. Créez un nouveau golfeur : Tim COOK, tc@windobe.com
```sql
INSERT INTO golfeurs (Firstname, Lastname, Email) VALUES ('Tim', 'COOK', 'tc@windobe.com');
```

7. Créez un nouveau golfeur : Harley DAVIDSON, h-d@suzukiki.fr
```sql
INSERT INTO golfeurs (Firstname, Lastname, Email) VALUES ('Harley', 'DAVIDSON', 'h-d@suzukiki.fr');
```

8. Créez un nouvel utilisateur : david GOLIATH, jaibeaucoupriz@wanadoo.fr
```sql
INSERT INTO utilisateurs (Firstname, Lastname, Email) VALUES ('David', 'GOLIATH', 'jaibeaucoupriz@wanadoo.fr');
```

9. Modifiez les tables « utilisateurs » et « golfeurs » pour y inclure la colonne suivante :
    - Age, int, null
```sql
ALTER TABLE utilisateurs ADD Age INT;
ALTER TABLE golfeurs ADD Age INT;
```

10. Renseignez l’âge de John LEGEND (78 ans) en vous basant sur son nom et son prénom :
```sql
UPDATE utilisateurs SET Age = 78 WHERE Firstname = 'John' AND Lastname = 'LEGEND';
```

11. Renseignez l’âge de Jack SPARROW (2 ans) en vous basant sur son nom et son prénom :
```sql
UPDATE utilisateurs SET Age = 2 WHERE Firstname = 'Jack' AND Lastname = 'SPARROW';
```

12. Renseignez l’âge de Tim COOK (30 ans)  en vous basant sur son nom et son prénom :
```sql
UPDATE golfeurs SET Age = 30 WHERE Firstname = 'Tim' AND Lastname = 'COOK';
```

13. Renseignez l’âge de Harley DAVIDSON (200 ans) en vous basant sur son nom et son prénom :
```sql
UPDATE golfeurs SET Age = 200 WHERE Firstname = 'Harley' AND Lastname = 'DAVIDSON';
```

14. Renseignez l’âge de David GOLIATH (3000 ans) en vous basant sur son nom et son prénom :
```sql
UPDATE utilisateurs SET Age = 3000 WHERE Firstname = 'David' AND Lastname = 'GOLIATH';
```

15. Modifier la table « golfeurs » en supprimant la colonne « Email » :
```sql
ALTER TABLE golfeurs DROP COLUMN Email;
```

16. Supprimer l'utilisateur david GOLIATH :
```sql
DELETE FROM utilisateurs WHERE Firstname = 'David' AND Lastname = 'GOLIATH';
```

17. Supprimer le golfeur Tim COOK en vous basant sur son nom et son prénom :
```sql
DELETE FROM golfeurs WHERE Firstname = 'Tim' AND Lastname = 'COOK';
```

18. Vider les informations de la table « utilisateurs » :
```sql
DELETE FROM utilisateurs;
```

19. Vider les informations de la table « golfeurs » :
```sql
DELETE FROM golfeurs;
```

20. Supprimer la base de données nommée « golf » :
```sql
DROP DATABASE IF EXISTS golf;
```
