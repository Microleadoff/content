## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développer un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "World" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :


1. Sélectionner tous les États distincts
2. Sélectionner tous les codes d'État distincts
3. Sélectionner tous les pays distincts
4. Sélectionner tous les codes de pays distincts
5. Sélectionner toutes les valeurs distinctes de latitude et longitude
6. Sélectionner toutes les villes dont l'État est "California" ou "Texas" en utilisant "WHERE" et "OR"
7. Sélectionner toutes les villes dont le code d'État est "CA" ou "TX" en utilisant "WHERE" et "OR"
8. Sélectionner toutes les villes dont le pays à l'id numéro 6 ou 231 en utilisant "WHERE" et "OR"
9. Sélectionner toutes les villes dont le code de pays est "US" ou "CA" en utilisant "WHERE" et "OR"
10. Sélectionner toutes les villes dont la latitude est supérieure à 40 ou la longitude est inférieure à -100 en utilisant "WHERE" et "OR"
11. Sélectionner toutes les villes dont l'id de l'état est 3395 ou 3396 en utilisant "IN"
12. Sélectionner toutes les villes dont le code d'État est "CA" ou "TX" en utilisant "IN"
13. Sélectionner toutes les villes dont l'id du pays est 3 ou 12 en utilisant "IN"
14. Sélectionner toutes les villes dont le code de pays est "US" ou "CA" en utilisant "IN"
15. Sélectionner toutes les villes dont la latitude est supérieure à 40 ou la longitude est inférieure à -100 en utilisant "IN"
16. Sélectionner toutes les villes dont la latitude est entre 40 et 45 en utilisant "WHERE" et "BETWEEN"
17. Sélectionner toutes les villes dont la longitude est entre -100 et -90 en utilisant "WHERE" et "BETWEEN"
18. Sélectionner toutes les villes dont l'ID est entre 100 et 200 en utilisant "WHERE" et "BETWEEN"
19. Sélectionner toutes les villes dont la création a eu lieu entre deux dates en utilisant "WHERE" et "BETWEEN"
20. Sélectionner toutes les villes dont la latitude est entre 25 et 26 en utilisant "WHERE" et "BETWEEN"
21. Sélectionner toutes les villes dont le nom commence par 'Los' en utilisant "LIKE"
22. Sélectionner toutes les villes dont le nom se termine par 'ville' en utilisant "LIKE"
23. Sélectionner toutes les villes dont le nom contient 'New' en utilisant "LIKE"
24. Sélectionner toutes les villes dont le code d'état commence par 'T' en utilisant "LIKE"
25. Sélectionner toutes les villes dont l'id du pays se termine par 9 en utilisant "LIKE"

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée