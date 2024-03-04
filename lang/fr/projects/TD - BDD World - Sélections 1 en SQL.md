## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développé un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "World" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Sélectionner tous les Pays
2. Sélectionner tous les Pays par leur nom et leur code iso3
3. Sélectionner les monnaies distinctes des pays 
4. Sélectionner les monnaies et les symboles des monnaies distinctes des pays 
5. Sélectionner les nom des villes et le code pays dont le code pays est « AO » 
6. Sélectionner les villes dont le code pays est « AO» et le code d'État « HUI»
7. Sélectionner les villes et le code pays dont le code pays est « AO » ou « AZ » en utilisant « OR »
8. Sélectionner les villes et le code pays dont le code pays est « AO » ou « AZ » en utilisant « IN »
9. Sélectionner les villes dont le code pays est « AO» et le code d’État « HUI» ou « MOX » en utilisant « OR »
10. Sélectionner les villes dont le code pays est « AO» et le code d’État « HUI» ou « MOX » en utilisant « IN »
11. Sélectionner les pays dont le code numérique est compris entre 50 et 100 
12. Sélectionner les pays dont le la monnaie est « USD » et le code numérique est compris entre 50 et 100
13. Sélectionner les villes dont le code pays est « AO » et, le code d’État est « BIE» ou la longitude est comprise entre 13 et 14
14. Sélectionner les villes dont le code pays est « AO » ou, le code d’État est « BIE» ou « HUI » et la longitude est comprise entre 13 et 14
15. Sélectionner les pays dont le nom commence par un « C»
16. Sélectionner les pays dont la monnaie est « EUR » et la deuxième lettre du nom est un « A »
17. Sélectionner les pays dont la monnaie est « EUR » et la deuxième lettre du nom est un « A » ou le code numérique est compris entre 200 et 300
18. Sélectionner les pays dont le nom commence et termine par un « A» 
19. Sélectionner les pays dont le nom commence par un « A» et la 3ème lettre est un « G »
20. Sélectionner les pays dont le nom commence par un « F» , la 3ème lettre est un « E» et la monnaie est « EUR » 
21. Sélectionner les pays dont le nom contient « ENC »
22. Sélectionner les pays dont la monnaie est « USD » ou dont le code numérique est compris entre 300 et 500 et, le nom contient « NE »
23. Sélectionner les pays dont l’avant-dernière lettre est un « E »
24. Sélectionner les pays dont l’avant-dernière lettre du nom est un « E », la monnaie est « EUR » et le code numérique est compris entre 0 et 300
25. Sélectionner les villes dont le code pays est « AD» ou « AE » et le nom se termine par « A» ou dont la latitude est comprise entre 40 et 50 
26. Sélectionner les pays pour lesquels l’id région est null

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée