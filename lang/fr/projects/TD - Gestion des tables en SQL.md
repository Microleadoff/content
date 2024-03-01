## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de gestion des tables en SQL au sein d'un SGBD.

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Créer une base de données nommée « golf »
2. Créez une table nommée « utilisateurs » qui respectera les colonnes suivantes : 
    - Id, pk, auto_increment
    - Firstname, varchar
    - Lastname, varchar
    - Email, longtext
3. Créez une table nommée « golfeurs » qui respectera les colonnes suivantes : 
    - Id, pk, auto_increment
    - Firstname, varchar
    - Lastname, varchar
    - Email, longtext
4. Créez un nouveau golfeur : John LEGEND, j.legend@gmail.com
5. Créez un nouvel utilisateur : Jack SPARROW, jack_sparrow@yahoo.fr
6. Créez un nouveau golfeur : Tim COOK, tc@windobe.com
7. Créez un nouveau golfeur : Harley DAVIDSON, h-d@suzukiki.fr
8. Créez un nouvel utilisateur : david GOLIATH, jaibeaucoupriz@wanadoo.fr
9. Modifiez les tables « utilisateurs » et « golfeurs » pour y inclure la colonne suivante : 
    - Age, int, null
10. Renseignez l’âge de John LEGEND (78 ans) en vous basant sur son nom et son prénom
11. Renseignez l’âge de Jack SPARROW (2 ans) en vous basant sur son nom et son prénom
12. Renseignez l’âge de Tim COOK (30 ans)  en vous basant sur son nom et son prénom
13. Renseignez l’âge de Harley DAVIDSON (200 ans) en vous basant sur son nom et son prénom
14. Renseignez l’âge de David GOLIATH (3000 ans) en vous basant sur son nom et son prénom
15. Modifier la table « golfeurs » en supprimant la colonne « Email »
16. Supprimer l'utilisateur david GOLIATH en vous basant sur son nom et son prénom
17. Supprimer le golfeur Tim COOK en vous basant sur son nom et son prénom
18. Vider les informations de la table « utilisateurs »
19. Vider les informations de la table « golfeurs »
20. Supprimer la base de données nommée « golf »

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée