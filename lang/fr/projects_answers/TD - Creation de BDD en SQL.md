## Corrigé

### Voici la liste des commandes qu'il fallait effectuer dans l'ordre

1. Créer une base de données nommée "Toto":
```sql
CREATE DATABASE Toto
```

2. Créer une base de données nommée "Tata" :
```sql
CREATE DATABASE Tata
```

3. Supprimer la base de données "Toto" :
```sql
DROP DATABASE Toto
```

4. Créer une base de données nommée "toto" :
```sql
CREATE DATABASE toto
```

5. Créer une base de données nommée "toto" (la BDD ne devra être créée que si une autre possédant le même nom n'existe pas déjà)
```sql
CREATE DATABASE IF NOT EXISTS toto;
```
**Note** : le ```IF NOT EXISTS``` permet de ne créer la BDD que si celle-ci n'existe pas déjà.

6. Supprimer la base de données "Tata" :
```sql
DROP DATABASE Tata
```

7. Supprimer la base de données "toto" :
```sql
DROP DATABASE toto
```

