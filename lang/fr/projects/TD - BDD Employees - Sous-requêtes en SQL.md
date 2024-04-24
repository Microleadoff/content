## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développé un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Employees" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Sélectionner les prénoms et noms des employés qui ne sont pas ou n’ont pas été managers, utiliser des alias 
2. Sélectionner les prénoms et noms  des employés qui ont eu plus de 2 titres professionnels différents
3. Sélectionner les numéros, prénoms et noms des employés qui ont eu un salaire compris entre 100000 et 150000
4. Sélectionner les numéros, prénoms et noms des employés qui ont eu un salaire supérieur à 150000 et qui ne sont pas  ou n’ont pas été managers 
5. Sélectionner les numéros des employés managers qui ont un salaire inférieur à 100000 et qui ont eu plus de 2 titres professionnels 
6. Sélectionner les noms des employés ayant été managers d'un département, utiliser des alias pour les résultats et l’appel des tables (EXISTS)
7. Sélectionner les noms des employés pour qui il existe un salaire supérieur à 100000, utiliser des alias pour les résultats et l’appel des tables (EXISTS)
8. Sélectionner les noms des employés féminins ayant occupé un poste de manager, utiliser des alias (EXISTS)
9. Sélectionner les noms et prénoms des employés ayant eu un salaire supérieur à 100000, utiliser des alias (EXISTS)
10. Sélectionner les numéros, noms et prénoms des employés nés le 1er janvier 1960 pour qui il existe exactement deux titres professionnels différents au cours de leur carrière, utiliser des alias (EXISTS)
11. Sélectionner les employés dont la date d'embauche est supérieure ou égale à la dernière prise de poste de manager, utiliser des alias (ALL)
12. Sélectionner l’identifiant de l’employé dont le salaire est le plus élevé, utiliser des alias (ALL)
13. Sélectionner le titre le plus donné aux employés
14. Sélectionner les identifiants des employés dont la période d'emploi est plus longue que celle des autres employés (ALL)
15. Sélectionner les employés qui ont le titre le plus fréquemment donné (ALL)
16. Sélectionner les titres des employés ayant au moins un salaire supérieur à 150000$, utiliser des alias (ANY)
17. Sélectionner le nombre d’employés managers (ANY)
18. Sélectionner les noms des employés ayant été dans au moins un département et ayant eu un salaire supérieur à 150 000$, utiliser des alias (ANY)
19. Sélectionner les prénoms des employés ayant le titre « Senior Engineer » (ANY)
20. Sélectionner le nombre de salariés ayant un salaire supérieur à la moyenne (ANY)


### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée