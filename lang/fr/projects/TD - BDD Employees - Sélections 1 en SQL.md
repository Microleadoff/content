## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développé un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Employees" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :


1. Sélectionner tous les employés
2. Sélectionner tous les employés par leurs noms et prénoms
3. Sélectionner les noms distincts des employés 
4. Sélectionner les noms et prénoms distincts des employés 
5. Sélectionner les noms et prénoms des employés dont le nom est « alencar »
6. Sélectionner les employés dont le nom est « alencar » et de sexe masculin 
7. Sélectionner les employés dont le prénom « Danai » ou « Leen » en utilisant « OR »
8. Sélectionner les employés dont le prénom « Danai » ou « Leen » en utilisant « IN »
9. Sélectionner les employés dont le nom est « alencar » et le prénom « Danai » ou « Leen » en utilisant « OR »
10. Sélectionner les employés dont le nom est « alencar » et le prénom « Danai » ou « Leen » en utilisant « IN »
11. Sélectionner les employés dont le numéro d’employé est compris entre 50000 et 50150
12. Sélectionner les employés dont le nom est « alencar » et le numéro d’employé est compris entre 50000 et 60000
13. Sélectionner les employés dont le nom est « alencar » et le prénom est « danai » ou le numéro d’employé est compris entre 50000 et 60000 
14. Sélectionner les employés dont le nom est « alencar » ou, le prénom est « danai » ou « leen » et le numéro d’employé est compris entre 50000 et 60000
15. Sélectionner les employés dont le prénom commence par un « T » 
16. Sélectionner les employés masculin dont la deuxième lettre du prénom est un « T » 
17. Sélectionner les employés dont le nom est « alencar » et le prénom « danai » ou le numéro d’employé commence par un 5 
18. Sélectionner les employés dont le prénom commence par un « T » et termine par un « B »
19. Sélectionner les employés dont le prénom commence par un « T », la 3ème lettre est un « R »
20. Sélectionner les employés dont le prénom commence par un « T », la 3ème lettre est un « R » et le numéro d’employé est compris entre 50000 et 60000 
21. Sélectionner les employés dont le prénom contient « TZV » 
22. Sélectionner les employés masculin ou dont le numéro d’employé est compris entre 50000 et 60000 et, le prénom contient « TZV »
23. Sélectionner les employés dont le prénom termine par « CAL»
24. Sélectionner les employés dont le prénom termine par « CAL» de genre masculin et dont le numéro d’employé est compris entre 50000 et 60000 
25. Sélectionner les employés dont le prénom est « danai » ou « leen » et le nom se termine par « TH» ou dont le numéro d’employé est compris entre 50000 et 100000 
26. Sélectionner les employés dont la date de naissance est null



### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée