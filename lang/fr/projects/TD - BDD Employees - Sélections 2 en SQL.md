## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développé un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Employees" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :


1. Sélectionner le nombre d’employés par département
2. Sélectionner le salaire maximum et minimum des employés
3. Sélectionner le salaire maximum et minimum par employés
4. Sélectionner la moyenne de salaire par employés
5. Sélectionner la moyenne de salaire par employés si leur numéro contient « 150 »
6. Sélectionner le nombre d’employés par département avec un résumé général
7. Sélectionner le nombre d’employés par département si leur numéro d’employé est compris entre 10000 et 50000
8. Sélectionner la moyenne, le minimum et le maximum des salaires par employé si leur numéro est compris entre 10005 et 10105 avec un résumé général
9. Sélectionner le nombre d’employés par département pour les départements « d005 » et « d006 »
10. Sélectionner le nombre d’employés par département s’il est inférieur à 50000
11. Sélectionner la moyenne des salaires par employé si elle est comprise entre 40000 et 50000
12. Sélectionner la liste des employées en ordre alphabétique inversé de nom
13. Sélectionner la liste des employés en ordre alphabétique inversé de nom et en ordre alphabétique par prénom
14. Sélectionner le nombre d’employés par département du plus petit au plus grand
15. Sélectionner le salaire maximum et minimum des employés, utiliser des alias
16. Sélectionner les 10 premiers employés
17. Sélectionner les noms et prénoms des 10 premiers employés, utiliser des alias
18. Sélectionner 10 employés à partir du 5ème
19. Sélectionner les noms et prénoms des 10 premiers employés en ordre alphabétique par nom
20. Sélectionner la somme des salaires pour les 10 premiers employés si la somme est inférieure à 50000
21. Sélectionner la somme des salaires par employés si leur numéro est compris entre 10001 et 50000 et la somme est inférieure à 50000
22. Sélectionner la somme des salaires pour les 10 premiers employés si leur numéro est compris entre 10001 et 50000 et la somme est inférieure à 50000
23. Sélectionner les employés et afficher les catégories de département (d001 = « Département n°1 », d002 = « Département n°2 », …, d009 = « Département n°9 » et s’il n’y a pas de département) si le numéro d’employé est compris entre 10150 et 10200
24. Sélectionner le nombre d’employés par département et afficher les catégories : supérieur à 50000 = « Élevé », supérieur ou égale à 20000 = « Correct », inférieur à 20000 = « Faible », utiliser des alias
25. Sélectionner les moyennes des salaires par employés et afficher les catégories : supérieur à 100000 = « Très élevée », supérieur ou égale à 80000 = « Élevée », inférieur à 80000 = « Faible », utiliser des alias

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée