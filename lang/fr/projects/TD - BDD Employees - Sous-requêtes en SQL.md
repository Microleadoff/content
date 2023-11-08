## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les sous-requêtes dans une base de données SQL au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développer un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Employees" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :


1. Sélectionner les prénoms des employés qui ont effectué des ventes (commandes)
2. Sélectionner les noms de famille des employés qui ont des ventes confirmées
3. Sélectionner les prénoms des employés masculins ayant effectué des ventes
4. Sélectionner les noms de famille des employés féminins ayant effectué des ventes confirmées
5. Sélectionner les prénoms des employés qui ont été embauchés en 2022 et ont effectué des ventes
6. Sélectionner les noms des employés dont le salaire est supérieur ou égal au salaire de tous les employés du département 'Sales'
7. Sélectionner les prénoms des employés masculins dont le salaire est supérieur ou égal au salaire de tous les employés masculins du département 'Marketing'
8. Sélectionner les noms de famille des employés dont le salaire est supérieur ou égal au salaire de tous les employés du département 'Ressources humaines'
9. Sélectionner les prénoms des employés féminins dont le salaire est supérieur ou égal au salaire de toutes les employées féminines du département 'Finance'
10. Sélectionner les noms de famille des employés dont le salaire est supérieur ou égal au salaire de tous les employés du département 'Développement'
11. Sélectionner les prénoms des employés dont au moins un enregistrement a un salaire supérieur à 50000
12. Sélectionner les noms de famille des employés dont au moins un enregistrement a un salaire égal à 60000
13. Sélectionner les prénoms des employés masculins dont au moins un enregistrement a un salaire supérieur à 55000
14. Sélectionner les noms de famille des employés dont au moins un enregistrement a un salaire égal à 58000
15. Sélectionner les prénoms des employés féminins dont au moins un enregistrement a un salaire supérieur à 53000

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée