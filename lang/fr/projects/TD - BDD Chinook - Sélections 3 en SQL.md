## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développé un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "Chinook" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Sélectionner les identifiants des chansons des lignes de factures et des pistes des playlists sans doublon, utiliser des alias
2. Sélectionner les pays distincts des clients et des factures sans doublon
3. Sélectionner les identifiants et prix unitaire des chansons des lignes de factures et des pistes sans doublon
4. Sélectionner les noms des playlists et des albums sans doublon, utiliser des alias
5. Sélectionner les États et les identifiants clients s’ils ne sont pas null des tables : clients et factures ordonnés par État sans doublon
6. Sélectionner les identifiants des chansons des lignes de factures et des pistes des playlists avec possibles doublons
7. Sélectionner les pays des clients et des factures avec possibles doublons
8. Sélectionner les noms des playlists et des albums avec possibles doublons, utiliser des alias
9. Sélectionner les États et les identifiants clients s’ils ne sont pas null des tables : clients et factures ordonnés par État avec possibles doublons
10. Sélectionner les clients qui ont été facturés le 03 Novembre 2013 (INTERSECT - VERSION MySQL Workbench)
11. Sélectionner les clients qui ont été facturés dans les pays suivants : « USA », « France », « Allemagne » (INTERSECT - VERSION MySQL Workbench)
12. Sélectionner les noms et prénoms des clients résidant dans des pays où le montant total des factures dépasse 100$ (INTERSECT - VERSION MySQL Workbench)
13. Sélectionner le nombre d’album dont le genre est « Rock » (INTERSECT - VERSION MySQL Workbench)
14. Sélectionner les clients qui ont une somme totale de factures supérieure à 40$ (INTERSECT - VERSION MySQL Workbench)
15. Sélectionner le nombre de fois que chaque chanson (par son nom) a été ajoutée dans une playlist, si elle apparaît plus de 3 fois. Ordonner par nombre décroissant puis par ordre alphabétique de nom, utiliser des alias pour les résultats et pour l’appel des tables (INTERSECT - VERSION MySQL Workbench)
16. Sélectionner les villes des clients à l’exception de celles des employés (EXCEPT)
17. Sélectionner les identifiants des chansons présents dans les playlists à l’exception de ceux présents dans les lignes de factures (EXCEPT)
18. Sélectionner les identifiants des clients à l’exception de ceux qui ont une moyenne de facturation inférieure à 5,5$ (EXCEPT)
19. Sélectionner les identifiants des artistes à l’exception de ceux associés à des albums (EXCEPT)
20. Sélectionner les villes des clients à l’exception de celles dont la somme de facturation est supérieure 80$ (EXCEPT)


### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée