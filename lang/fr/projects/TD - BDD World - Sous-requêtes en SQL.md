## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les sous-requêtes dans une base de données SQL au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développer un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "World" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :

1. Sélectionner les noms des continents (regions) qui ont plus de 2 sous-continents (subregions), utiliser des alias
2. Sélectionner les noms des pays qui ont des États avec des coordonnées de latitude supérieures à 40, utiliser des alias
3. Sélectionner les noms des États qui ont des villes avec des noms commençant par « New »
4. Sélectionner les noms des continents (regions) ayant au moins un sous-continents(subregion), utiliser des alias pour les résultats et l’appel des tables
5. Sélectionner les noms des continents (regions) comprenant des pays ayant une latitude inférieure à 35
6. Sélectionner les noms des continents (regions) pour qui il existe des sous-continents (subregions) existants, utiliser des alias pour les résultats et l’appel des tables (EXISTS)
7. Sélectionner les noms des pays pour qui il existe des États avec une latitude supérieure à 50 existants, utiliser des alias (EXISTS)
8. Sélectionner les noms des États pour lesquels il existe au moins une ville avec un nom commençant par "New", utiliser des alias (EXISTS)
9. Sélectionner les noms des continents (regions) pour lesquels il existe plus de deux sous-continents (subregions), utiliser des alias (EXISTS)
10. Sélectionner les pays pour lesquels il n’existe aucun État, utiliser des alias (EXISTS)
11. Sélectionner les villes qui ont été créées après la création du dernier pays (ALL)
12. Sélectionner les continents avec le plus grand nombre de sous-continents (ALL)
13. Sélectionner les pays avec le plus grand nombre de villes (ALL)
14. Sélectionner le pays avec la latitude la plus élevée (ALL)
15. Sélectionner la région avec le moins de pays (ALL)
16. Sélectionner l’identifiant du pays à qui est associée la ville avec la plus grande latitude (ANY)
17. Séléctionner les noms des continents qui possèdent au moins un sous-sontinent associé (ANY)
18. Sélectionner les noms des villes associées à la « France » (ANY)
19. Sélectionner le nom du pays à qui est associée la ville avec la latitude la plus basse (ANY)
20. Sélectionner les continents qui possèdent plus de 2 sous-continents associés (ANY)

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée