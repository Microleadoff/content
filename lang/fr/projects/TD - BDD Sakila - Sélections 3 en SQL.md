## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développer un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Sakila" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Sélectionner les prénoms distincts des employés et des clients sans doublon
2. Sélectionner les identifiants des films associés à des acteurs et à des catégories sans doublon
3. Sélectionner les identifiants d’adresse des employés et des clients sans doublon
4. Sélectionner les identifiants des clients et des employés pour les paiements et les retours de locations effectués entre le 1er et le 2 Janvier 2021 ordonné par identifiant client et employé sans doublon
5. Sélectionner les identifiants des employés ayant reçu des paiements et eu des retours de location pour les identifiants de location commençant par « 28 » sans doublon
6. Sélectionner les prénoms distincts des employés et des clients avec possibles doublons
7. Sélectionner les identifiants des films associés à des acteurs et à des catégories avec possibles doublons
8. Sélectionner les identifiants d’adresse des employés et des clients avec possibles doublons
9. Sélectionner les identifiants des clients et des employés pour les paiements et les retours de locations effectués entre le 1er et le 2 Janvier 2021 ordonné par identifiant client et employé avec possibles doublons
10. Sélectionner les identifiants des employés ayant reçu des paiements et eu des retours de location pour les identifiants de location commençant par « 28 » avec possibles doublons
11. Sélectionner les clients qui ont effectué un retour en Juin 2010 (INTERSECT - VERSION MySQL Workbench)
12. Sélectionner le nombre de film dont la catégorie est « Action » (INTERSECT - VERSION MySQL Workbench)
13. Sélectionner les clients qui ont effectué un paiement entre le 1er et le 5 Janvier 2010 (INTERSECT - VERSION MySQL Workbench)
14. Sélectionner le nombre de films dans les catégories dont le nom commence par un « C », utiliser des alias (INTERSECT)
15. Sélectionner les clients qui ont une somme totale de factures supérieure à 50$ (INTERSECT - VERSION MySQL Workbench)
16. Sélectionner les prénoms distincts des clients à l’exception de ceux étant également présents dans les employés (EXCEPT)
17. Sélectionner les identifiants des clients à l’exception de ceux ayant fait un retour de location en 2010 (EXCEPT)
18. Sélectionner les identifiants des clients à l’exception de ceux ayant effectué un paiement entre le 1er Janvier et le 31 Décembre 2010 (EXCEPT)
19. Sélectionner les identifiants des films à l’exception de ceux qui ont été loués entre le 1er Janvier 2020 et le 31 Décembre 2022 (EXCEPT)
20. Sélectionner les identifiants des adresses des clients à l’exception de ceux également présents pour les employés (EXCEPT)

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée