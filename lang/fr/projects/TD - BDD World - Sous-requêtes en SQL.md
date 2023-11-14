## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les sous-requêtes dans une base de données SQL au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développer un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "World" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :


1. Sélectionner toutes les villes qui ont dans leurs country id des noms de pays qui commence par la lettre A
2. Sélectionner la capitale de chaque pays dont l'id de région est un chiffre pair
3. Sélectionner tous les pays qui sont dans la région qui contient la sous-région d'id 1
4. Sélectionner les noms de touutes les villes dont le nom de leur pays est "Algeria" ou "Angola"
5. Sélectionner le nom des états de chaque pays situé dans la région dont le nom est "Europe"
6. Sélectionner tous les noms de ville du pays dont le nom est France si celui-ci existe
7. Sélectionner toutes les régions qui contiennent un pays avec une latitude supérieure à 60 s'il en existe
8. Sélectionner le nom de toutes les sous-régions qui contiennent un pays dont le nom est "Région"
9. Sélectionner toutes les villes dont l'id est plus grand que le nombre de pays qui ont pour devise l'euro
10. Sélectionner tous les pays, le symbole de leur devise et le nom de leur devise si leurs id est inférieur ou égale à l'id le plus grand parmis la table régions
11. Sélectionner les noms et les id des sous régions dont l'id de la région parent est égal à tous les id des régions qui ont pour nom "Americas"
12. Sélectionner les villes si il y a au moins un id plus grand que le nombre de pays qui ont pour devise l'euro
13. Sélectionner les nom, le symbole et le nom des monnaies des pays dont l'id est égal au plus grand id des régions
14. Sélectionner le nom, le fips_code, la latitude et la longitude des états dont le fips_code est égal à l'id de la ville qui s'appelle "Paris"

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée