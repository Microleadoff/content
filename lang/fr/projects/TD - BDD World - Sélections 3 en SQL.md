## Énoncé

### Description courte

L'objectif de ce TD est de mettre en pratique les commandes de sélection de lignes dans une base de données au sein d'un SGBD.

### Éléments donnés 

Afin de pouvoir pratiquer les différentes requêtes SQL, nous avons développer un script python qui va vous permettre d'installer différentes bases de données avec des données intégrées. Pour les installer, vous devez vous réferrer au <a href="https://github.com/Microleadoff/database-installer-py" title="repository du code python d'installation des bases de données" target="_blank">readme de ce repository</a>

Ce TD portera sur la base de données nommée "World" fournie avec le programme python.

**Note** : Si vous ne souhaitez pas installer python, vous pourrez trouver des scripts MySQL dans les fichiers du lien ci-dessus. Libre à vous de les exécuter manuellement !

### Travaux à effectuer

Réaliser les différentes tâches suivantes dans l'ordre grâce aux commandes SQL :


1. Sélectionner toutes les sous-région appartenant aux régions id 1 à 3, ainsi que celles appartenant à la région id 5 en utilisant UNION
2. Sélectionner tous les états avec une latitude comprise entre 20 et 40, ainsi que tous les états avec une longitude comprise entre 20 et 40 en utilisant UNION
3. Sélectionner tous les pays dont le symbole de la monnaie est "€", ainsi que tous les pays dont le symbole de la monnaie est "$" en utilisant UNION
4. Sélectionner toutes les villes dont le code de l'état est "AZ", ainsi que toutes les villes dont le code du pays est "AD" en utilisant UNION
5. Sélectionner tous les pays dont le symbole de la monnaie est "$", ainsi que tous les pays dont le code iso3 contient la lettre "A" en utilisant UNION
6. Sélectionner tous les id des régions, ainsi que tous les champs "region_id" des pays en utilisant UNION ALL
7. Sélectionner tous les noms des sous-régions, ainsi que toutes les sous-régions des pays en utilisant UNION ALL
8. Sélectionner tous les codes iso2 des pays, ainsi que tous les codes des pays depuis la table des états en utilisant UNION ALL
9. Sélectionner toutes les dates de création des pays, ainsi que toutes les dates de création des états en utilisant UNION ALL
10. Sélectionner tous les id des sous-régions, ainsi que tous id des régions en utilisant UNION ALL

### Contraintes

- N'utilisez que du SQL
- Gardez bien trace de chaque instruction rédigée