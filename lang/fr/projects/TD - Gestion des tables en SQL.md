## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de gestion des tables en SQL au sein d'un SGBD.

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

- Créer une base de données nommée « golf »
- Créez une table nommée « utilisateurs » qui respectera les colonnes suivantes : 
    - Id, pk, auto_increment
    - Firstname, varchar
    - Lastname, varchar
    - Email, longtext
- Créez une table nommée « golfeurs »
    - Id, pk, auto_increment
    - Firstname, varchar
    - Lastname, varchar
    - Email, longtext
- Créez un nouveau golfeur : John LEGEND, j.legend@gmail.com
- Créez un nouvel utilisateur : Jack SPARROW, jack_sparrow@yahoo.fr
- Créez un nouveau golfeur : Tim COOK, tc@windobe.com
- Créez un nouveau golfeur : Harley DAVIDSON, h-d@suzukiki.fr
- Créez un nouvel utilisateur : david GOLIATH, jaibeaucoupriz@wanadoo.fr
- Modifiez la table « utilisateurs » pour y inclure la colonne suivante : 
    - Age, int, null
- Renseignez l’âge de John LEGEND : 78 ans
- Renseignez l’âge de Jack SPARROW : 2 ans
- Renseignez l’âge de Tim COOK : 30 ans
- Renseignez l’âge de Harley DAVIDSON : 200 ans
- Renseignez l’âge de David GOLIATH : 3000 ans
- Modifier la table « golfeurs » en supprimant la colonne « Email »
- Vider les informations de la table « utilisateurs »
- Vider les informations de la table « golfeurs »
- Supprimer la base de données nommée « golf »

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée