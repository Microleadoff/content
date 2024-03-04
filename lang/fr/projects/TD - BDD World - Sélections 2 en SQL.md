## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développé un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "World" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :


1. Sélectionner le nombre de pays par monnaies
2. Sélectionner la latitude maximum et minimum des villes
3. Sélectionner la latitude maximum et minimum des villes par pays
4. Sélectionner la moyenne de latitude des villes par pays
5. Sélectionner la moyenne de latitude des villes par pays si leur code contient un « A »
6. Sélectionner le nombre de villes par pays avec un résumé général
7. Sélectionner le nombre de villes par pays si leur identifiant d’État est compris entre 10 et 150
8. Sélectionner la moyenne, le maximum et le minimum des latitudes des villes par pays si leur identifiant d’État est compris entre 10 et 150 avec un résumé général
9. Sélectionner le nombre de villes pour les pays ayant les codes « ES » et « FR »
10. Sélectionner le nombre de villes par pays s’il est supérieur à 50000
11. Sélectionner la moyenne de latitude des villes par pays si elle est comprise entre 20 et 25
12. Sélectionner la liste des pays en ordre alphabétique inversé de nom
13. Sélectionner la liste des villes en ordre alphabétique inversé de code de pays et en ordre alphabétique par code d’État
14. Sélectionner le nombre de villes par pays du plus petit au plus grand
15. Sélectionner la latitude moyenne, maximum et minimum des villes par pays, utiliser des alias
16. Sélectionner les 10 premiers pays
17. Sélectionner les noms des 10 premiers pays, utiliser des alias
18. Sélectionner 10 pays à partir du 5ème
19. Sélectionner les noms des 10 premiers pays en ordre alphabétique inversé de nom
20. Sélectionner le nombre de pays par monnaie pour les 10 premières monnaies si leur nombre est supérieur à 2, utiliser des alias
21. Sélectionner le nombre de villes par pays si leur latitude est comprise entre 10 et 50 et le nombre est supérieur à 1000
22. Sélectionner le nombre de villes par pays si leur code d’État contient un « Z » et le nombre est inférieur à 1000
23. Sélectionner les noms des pays et afficher les catégories de monnaie EUR = « Euro », USD = « Dollars », Les autres = « Autre monnaie »
24. Sélectionner le nombre de pays par monnaie ayant un résultat supérieur ou égal à 2 et afficher les catégories : supérieur à 5 = « Très élevé », supérieur à 3 = « Élevé », inférieur à 3 = « Moyen », utiliser des alias
25. Sélectionner les moyennes des latitudes des villes par pays si le code pays contient un « A » comme deuxième lettre et afficher les catégories : supérieur à 10 = « Nord », inférieur à -10 = « Sud », compris entre 10 et -10 = « Équateur », utiliser des alias

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée