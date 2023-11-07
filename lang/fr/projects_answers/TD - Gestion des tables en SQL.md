## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

- ```CREATE DATABASE golf;```
- ```CREATE TABLE utilisateurs (Id INT PRIMARY KEY AUTO_INCREMENT,Firstname VARCHAR(255),Lastname VARCHAR(255),Email LONGTEXT);```
- ```CREATE TABLE golfeurs (Id INT PRIMARY KEY AUTO_INCREMENT,Firstname VARCHAR(255),Lastname VARCHAR(255),Email LONGTEXT);```
- ```INSERT INTO golfeurs (Firstname, Lastname, Email) VALUES ('John', 'LEGEND', 'j.legend@gmail.com');```
- ```INSERT INTO utilisateurs (Firstname, Lastname, Email) VALUES ('Jack', 'SPARROW', 'jack_sparrow@yahoo.fr');```
- ```INSERT INTO golfeurs (Firstname, Lastname, Email) VALUES ('Tim', 'COOK', 'tc@windobe.com');```
- ```INSERT INTO golfeurs (Firstname, Lastname, Email) VALUES ('Harley', 'DAVIDSON', 'h-d@suzukiki.fr');```
- ```INSERT INTO utilisateurs (Firstname, Lastname, Email) VALUES ('David', 'GOLIATH', 'jaibeaucoupriz@wanadoo.fr');```
- ```ALTER TABLE utilisateurs ADD Age INT;```
- ```ALTER TABLE golfeur ADD Age INT;```
- ```UPDATE utilisateurs SET Age = 78 WHERE Firstname = 'John' AND Lastname = 'LEGEND';```
- ```UPDATE utilisateurs SET Age = 2 WHERE Firstname = 'Jack' AND Lastname = 'SPARROW';```
- ```UPDATE golfeurs SET Age = 30 WHERE Firstname = 'Tim' AND Lastname = 'COOK';```
- ```UPDATE golfeurs SET Age = 200 WHERE Firstname = 'Harley' AND Lastname = 'DAVIDSON';```
- ```UPDATE utilisateurs SET Age = 3000 WHERE Firstname = 'David' AND Lastname = 'GOLIATH';```
- ```ALTER TABLE golfeurs DROP COLUMN Email;```
- ```DELETE FROM utilisateurs WHERE Firstname = 'David' AND Lastname = 'GOLIATH';```
- ```DELETE FROM golfeurs WHERE Firstname = 'Tim' AND Lastname = 'COOK';```
- ```DELETE FROM utilisateurs;```
- ```DELETE FROM golfeurs;```
- ```DROP DATABASE IF EXISTS golf;```