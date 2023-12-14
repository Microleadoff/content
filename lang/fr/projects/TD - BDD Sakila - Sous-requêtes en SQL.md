## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développer un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Sakila" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Sélectionner les noms des acteurs ayant joué dans plus de 35 films, utiliser des alias pour les résultats et les appels des tables 
2. Sélectionner les noms des catégories de films ayant moins de 60 films associés, utiliser des alias pour les résultats et les appels des tables
3. Sélectionner les noms et prénoms des clients dont le montant total des paiements est supérieur à 3500$, utiliser des alias
4. Sélectionner les identifiants, noms et prénoms des clients qui ont effectué plus de 80 locations, utiliser des alias
5. Sélectionner les titres des films appartenant au genre « Drama », utiliser des alias
6. Sélectionner le nombre de locations par magasin, utiliser des alias
7. Sélectionner les acteurs ayant joué dans au moins 1 film, utiliser des alias (EXISTS)
8. Sélectionner les villes n’ayant aucune adresse associée, utiliser des alias (EXISTS)
9. Sélectionner les catégories qui ont au moins un film associé, utiliser des alias (EXISTS)
10. Sélectionner les clients ayant effectué au moins une location et dont la date de retour est comprise entre le 1er et le 2 Janvier 2021 ordonné par nom (EXISTS)
11. Sélectionner les films ayant au moins une catégorie et dont la durée est supérieure à 180min (EXISTS)
12. Sélectionner les clients dont la date de dernière mise à jour est antérieure ou égale à la plus récente des mises à jour enregistrées pour les adresses (ALL)
13. Sélectionner les acteurs dont le prénom est plus fréquent que tous les autres prénoms (ALL)
14. Sélectionner les identifiants des films ayant le plus grand nombre de locations (ALL)
15. Sélectionner les employés ayant enregistré le plus grand nombre de locations (ALL)
16. Sélectionner le prénom et le nom du client ayant le montant total de paiement le plus élevé (ALL)
17. Sélectionner les noms des catégories avec au moins un film ayant une durée supérieure à 3 heures (ANY)
18. Sélectionner prénoms des acteurs ayant joué dans au moins un film de la catégorie 5 (« Comedy »), utiliser des alias (ANY)
19. Sélectionner les noms des langues avec un film avec une durée inférieure à 90 minutes, utiliser des alias (ANY)
20. Sélectionner les adresses avec un client dont le nom commence par la lettre « R » (ANY)
21. Sélectionner les titres des films dans lesquels un acteur se nomme est « WOOD » (ANY)

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée