## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développer un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Chinook" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Sélectionner les noms des artistes qui ont plus de 10 albums, utiliser des alias pour les résultats et les appels des tables
2. Sélectionner les noms des genres musicaux ayant moins de 100 chansons associées, utiliser des alias pour les résultats et les appels des tables
3. Sélectionner les noms et prénoms des clients qui ont un montant total de dépenses supérieur à 40$, utiliser des alias pour l’appel des tables
4. Sélectionner les noms des playlists contenant plus de 50 chansons, utiliser des alias
5. Sélectionner les noms des albums dont le genre est 'Rock', utiliser des alias
6. Sélectionner les noms des chansons avec leur durée (millisecondes à convertir en minutes en divisant par 60000) pour l’artiste « Black Sabbath »
7. Sélectionner les noms des artistes qui ont au moins une chanson associée ordonée par nom, utiliser des alias pour les résultats et les appels des tables (EXISTS)
8. Sélectionner les chansons qui ont été facturées au moins une fois (EXISTS)
9. Sélectionner les chansons qui sont associées à au moins une playlist, utiliser des alias pour les résultats et les appels des tables (EXISTS)
10. Sélectionner les noms des artistes pour qui aucun album n'est répertorié, utiliser des alias (EXISTS)
11. Sélectionner les chansons qui n’ont jamais été facturées (EXISTS)
12. Sélectionner les chansons avec le prix unitaire le plus élevé (ALL)
13. Sélectionner l’identifiant de l’artiste qui a le plus grand nombre d’album associé (ALL)
14. Sélectionner l’album avec la durée d’écoute la plus longue (ALL)
15. Sélectionner le client dont le montant total des factures est supérieur à tous les autres (ALL)
16. Sélectionner l’employé qui a été embauché avant tous les autres (ALL)
17. Sélectionner les titres des albums ayant au moins une chanson avec un prix unitaire supérieur à 0,99$, utiliser des alias (ANY)
18. Sélectionner les noms des genres musicaux ayant au moins une chanson avec une durée inférieure à 2 minutes (120 000 millisecondes), utiliser des alias (ANY)
19. Sélectionner les identifiants des artistes dont la somme des prix unitaires des chansons de l'album est supérieure à 20$, utiliser des alias (ANY)
20. Sélectionner les noms des playlists contenant au moins une chanson avec un prix unitaire inférieur à 1$, utiliser des alias (ANY)
21. Sélectionner les noms des chansons qui ont été facturées pour un montant supérieur à la moyenne des prix unitaires des chansons, utiliser des alias (ANY)


### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée